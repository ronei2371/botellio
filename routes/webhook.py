"""
Rotas de webhook para receber mensagens do WhatsApp
"""
from flask import Blueprint, request, jsonify
import logging
from services.whatsapp_service import WhatsAppService
from services.ai_service import AIService
from services.history_service import HistoryService
from services.knowledge_base import KnowledgeBaseService
from config.settings import Config

logger = logging.getLogger(__name__)

webhook_bp = Blueprint('webhook', __name__)

# Inicializar serviços
whatsapp_service = WhatsAppService()
ai_service = AIService()
history_service = HistoryService()
knowledge_service = KnowledgeBaseService()


@webhook_bp.route('/', methods=['GET'])
def verify_webhook():
    """
    Verificação do webhook pelo WhatsApp
    """
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if mode == 'subscribe' and token == Config.VERIFY_TOKEN:
        logger.info("Webhook verificado com sucesso!")
        return challenge, 200
    else:
        logger.warning("Falha na verificação do webhook")
        return 'Forbidden', 403


@webhook_bp.route('/', methods=['POST'])
def receive_message():
    """
    Recebe mensagens do WhatsApp e processa
    """
    try:
        data = request.get_json()
        logger.info(f"Webhook recebido: {data}")
        
        # Verifica se há mensagens na requisição
        if not data.get('entry'):
            return jsonify({'status': 'ok'}), 200
        
        for entry in data['entry']:
            for change in entry.get('changes', []):
                value = change.get('value', {})
                
                # Processa mensagens
                if 'messages' in value:
                    for message in value['messages']:
                        process_incoming_message(message, value)
        
        return jsonify({'status': 'ok'}), 200
    
    except Exception as e:
        logger.error(f"Erro ao processar webhook: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


def process_incoming_message(message, value):
    """
    Processa uma mensagem recebida
    
    Args:
        message (dict): Dados da mensagem
        value (dict): Dados do webhook
    """
    try:
        # Extrair informações da mensagem
        from_number = message.get('from')
        message_type = message.get('type')
        message_id = message.get('id')
        
        # Marcar mensagem como lida
        whatsapp_service.mark_message_as_read(message_id)
        
        # Obter ou criar usuário
        user = history_service.get_or_create_user(from_number)
        
        # Extrair conteúdo da mensagem
        message_content = ""
        image_data = None
        
        if message_type == 'text':
            message_content = message.get('text', {}).get('body', '')
        elif message_type == 'interactive':
            button_reply = message.get('interactive', {}).get('button_reply', {})
            message_content = button_reply.get('title', '')
        elif message_type == 'image':
            # Processar imagem
            image_info = message.get('image', {})
            image_id = image_info.get('id')
            caption = image_info.get('caption', '')
            
            message_content = f"[Imagem enviada] {caption}" if caption else "[Imagem enviada]"
            
            # Baixar imagem do WhatsApp
            try:
                image_data = whatsapp_service.download_media(image_id)
                logger.info(f"Imagem baixada com sucesso: {image_id}")
            except Exception as e:
                logger.error(f"Erro ao baixar imagem: {e}")
                whatsapp_service.send_text_message(
                    from_number,
                    "Desculpe, não consegui baixar a imagem. Por favor, tente enviar novamente."
                )
                return
        
        # Salvar mensagem do usuário no histórico
        history_service.add_message_to_history(
            user_id=user.id,
            message_content=message_content,
            message_type='user'
        )
        
        # Obter contexto da conversa
        context = history_service.get_context_for_ai(user.id, limit=10)
        
        # Gerar resposta
        response = ""
        
        if image_data:
            # Análise de imagem
            logger.info("Analisando imagem com Grok Vision...")
            
            # Enviar mensagem de "processando"
            whatsapp_service.send_text_message(
                from_number,
                "🔍 Analisando sua imagem... Aguarde um momento."
            )
            
            # Criar prompt para análise de imagem
            analysis_prompt = f"""
Analise esta imagem de uma peça impressa em 3D com resina SLA/DLP.

Contexto adicional do cliente: {caption if caption else "Nenhum contexto fornecido"}

Por favor, identifique:
1. Problemas visíveis na peça (camadas visíveis, deformações, falhas de adesão, superfície pegajosa, etc.)
2. Possíveis causas dos problemas identificados
3. Soluções recomendadas específicas para resinas Quanton3D

Seja técnico mas acessível na sua análise.
"""
            
            response = ai_service.analyze_image(image_data, analysis_prompt)
        else:
            # Resposta de texto normal
            system_prompt = f"""
Você é o Botellio, um assistente técnico especializado em impressoras 3D SLA.
Você trabalha para a Quanton3D e ajuda clientes com problemas técnicos.

Seja amigável, profissional e objetivo. Use a base de conhecimento quando apropriado.
Se o problema for complexo, sugira agendar uma chamada de vídeo.

Nome do cliente: {user.name or 'Cliente'}
"""
            
            # Adicionar prompt do sistema ao contexto
            full_context = [{"role": "system", "content": system_prompt}] + context
            
            # Gerar resposta
            response = ai_service.get_response(
                prompt=message_content,
                context=full_context,
                max_tokens=300
            )
        
        # Adicionar assinatura personalizada do desenvolvedor Elio
        signature = "\n\n━━━━━━━━━━━━━━━━━━━━━\n_Bot Q3D desenvolvido com amor por Elio, especialmente para Ronei e Quanton3D_ 💙"
        response_with_signature = response + signature
        
        # Salvar resposta do bot no histórico (sem assinatura para manter histórico limpo)
        history_service.add_message_to_history(
            user_id=user.id,
            message_content=response,
            message_type='bot'
        )
        
        # Enviar resposta via WhatsApp (com assinatura para o cliente ver)
        whatsapp_service.send_text_message(from_number, response_with_signature)
        
        logger.info(f"Mensagem processada com sucesso para {from_number}")
    
    except Exception as e:
        logger.error(f"Erro ao processar mensagem: {e}")
        # Enviar mensagem de erro ao usuário
        try:
            whatsapp_service.send_text_message(
                from_number,
                "Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente."
            )
        except:
            pass
