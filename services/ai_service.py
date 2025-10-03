"""
Serviço de integração com Grok (xAI) para processamento de linguagem natural
"""
import requests
import logging
from config.settings import Config

logger = logging.getLogger(__name__)


class AIService:
    """Serviço para interagir com a API do Grok (xAI)"""
    
    def __init__(self):
        self.api_key = Config.GROK_API_KEY
        self.model = Config.GROK_MODEL  # grok-beta ou outro modelo disponível
        self.base_url = "https://api.x.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def get_response(self, prompt, context=None, max_tokens=500, temperature=0.7):
        """
        Gera uma resposta usando o modelo Grok
        
        Args:
            prompt (str): A pergunta ou comando do usuário
            context (list): Histórico da conversa (opcional)
            max_tokens (int): Número máximo de tokens na resposta
            temperature (float): Criatividade da resposta (0.0 a 1.0)
            
        Returns:
            str: Resposta gerada pela IA
        """
        messages = []
        
        # Adiciona o contexto da conversa, se houver
        if context:
            messages.extend(context)
        
        # Adiciona o prompt do usuário
        messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": False
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            answer = data['choices'][0]['message']['content'].strip()
            logger.info(f"Resposta do Grok gerada com sucesso.")
            return answer
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao chamar a API do Grok: {e}")
            raise
        except (KeyError, IndexError) as e:
            logger.error(f"Erro ao processar resposta do Grok: {e}")
            raise
    
    def classify_problem(self, message):
        """
        Classifica o problema do usuário em básico, intermediário ou complexo
        
        Args:
            message (str): Mensagem do usuário
            
        Returns:
            str: Categoria do problema ("básico", "intermediário", "complexo")
        """
        system_prompt = """
        Você é um especialista em suporte técnico para impressoras 3D SLA. 
        Classifique a seguinte mensagem de usuário em uma das três categorias:
        - "básico": Problemas comuns e fáceis de resolver (ex: nivelamento, calibração, configurações simples).
        - "intermediário": Problemas que exigem mais investigação (ex: diagnóstico de hardware, otimização avançada).
        - "complexo": Problemas que precisam de análise visual ou intervenção humana (ex: posicionamento de suportes, erros complexos).
        
        Responda apenas com a categoria em letra minúscula.
        """
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            "max_tokens": 10,
            "temperature": 0.0
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            category = data['choices'][0]['message']['content'].strip().lower()
            logger.info(f"Problema classificado como: {category}")
            return category
        except Exception as e:
            logger.error(f"Erro ao classificar problema: {e}")
            # Retorna categoria padrão em caso de erro
            return "intermediário"
    
    def analyze_image(self, image_url, prompt):
        """
        Analisa uma imagem em busca de problemas
        
        Args:
            image_url (str): URL da imagem a ser analisada
            prompt (str): Pergunta sobre a imagem
            
        Returns:
            str: Análise da imagem
        """
        # Nota: Verificar se o Grok suporta análise de imagens
        # Se não suportar, pode usar outra API ou retornar mensagem apropriada
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                            },
                        },
                    ],
                }
            ],
            "max_tokens": 300,
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            analysis = data['choices'][0]['message']['content'].strip()
            logger.info("Análise de imagem concluída.")
            return analysis
        except Exception as e:
            logger.error(f"Erro ao analisar imagem: {e}")
            # Retorna mensagem padrão se análise de imagem não estiver disponível
            return "Desculpe, no momento não consigo analisar imagens. Por favor, descreva o problema que você está vendo."
