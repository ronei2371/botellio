"""
Serviço de integração com OpenAI para processamento de linguagem natural
"""
import openai
import logging
from config.settings import Config

logger = logging.getLogger(__name__)


class AIService:
    """Serviço para interagir com a API da OpenAI"""
    
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        self.model = Config.OPENAI_MODEL
        openai.api_key = self.api_key
    
    def get_response(self, prompt, context=None, max_tokens=150, temperature=0.7):
        """
        Gera uma resposta usando o modelo de linguagem da OpenAI
        
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
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                n=1,
                stop=None
            )
            
            answer = response.choices[0].message.content.strip()
            logger.info(f"Resposta da IA gerada com sucesso.")
            return answer
        except Exception as e:
            logger.error(f"Erro ao chamar a API da OpenAI: {e}")
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
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=10,
                temperature=0.0
            )
            
            category = response.choices[0].message.content.strip().lower()
            logger.info(f"Problema classificado como: {category}")
            return category
        except Exception as e:
            logger.error(f"Erro ao classificar problema: {e}")
            raise
    
    def analyze_image(self, image_url, prompt):
        """
        Analisa uma imagem em busca de problemas
        
        Args:
            image_url (str): URL da imagem a ser analisada
            prompt (str): Pergunta sobre a imagem
            
        Returns:
            str: Análise da imagem
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
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
                max_tokens=300,
            )
            
            analysis = response.choices[0].message.content.strip()
            logger.info("Análise de imagem concluída.")
            return analysis
        except Exception as e:
            logger.error(f"Erro ao analisar imagem: {e}")
            raise
