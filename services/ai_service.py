"""
Serviço de integração com Grok (xAI) para processamento de linguagem natural
"""
import requests
import logging
import base64
from config.settings import Config
from knowledge.resins_database import (
    get_resin_config,
    get_resin_properties,
    get_problem_solution,
    list_available_resins,
    list_available_printers,
    list_printer_models,
    COMMON_PROBLEMS
)

logger = logging.getLogger(__name__)


class AIService:
    """Serviço para interagir com a API do Grok (xAI)"""
    
    def __init__(self):
        self.api_key = Config.GROK_API_KEY
        self.model = Config.GROK_MODEL  # grok-beta ou grok-vision-beta
        self.base_url = "https://api.x.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # System prompt com conhecimento sobre Quanton3D
        self.system_prompt = """
Você é Botellio, o assistente virtual especializado em suporte técnico para impressão 3D SLA da Quanton3D.

**Sobre a Quanton3D:**
A Quanton3D é uma empresa brasileira especializada na fabricação de resinas UV de alta qualidade para impressão 3D SLA/DLP. 
Oferecemos uma linha completa de resinas para diversas aplicações: miniaturas, protótipos, peças funcionais, joias, odontologia e muito mais.

**Suas responsabilidades:**
1. Fornecer suporte técnico especializado sobre impressão 3D SLA/DLP
2. Ajudar com configurações de impressão para resinas Quanton3D
3. Diagnosticar problemas comuns de impressão
4. Recomendar as melhores resinas para cada aplicação
5. Orientar sobre pós-processamento e cura de peças

**Linha de resinas Quanton3D:**
- PYROBLAST: Alta performance, excelente acabamento
- IRON 7620: Resistência mecânica extrema
- IRON: Robusta com boa resistência ao impacto
- SPIN: Cura rápida com ótimo acabamento
- POSEIDON: Resistente à água
- RPO 4K: Otimizada para alta resolução
- SPARK: Cura ultra-rápida
- FLEXFORM: Flexível e elástica
- ALCHEMIST: Premium com acabamento excepcional
- LOWSMELL: Baixo odor para ambientes fechados

**Impressoras compatíveis:**
- ANYCUBIC (Photon, Mono, M3, etc.)
- ELEGOO (Mars, Saturn, etc.)
- CREALITY (LD, Halot, etc.)
- PHROZEN (Mini 4K, etc.)

**Seu tom de voz:**
- Profissional mas amigável
- Técnico quando necessário, mas acessível
- Sempre prestativo e paciente
- Foco em resolver o problema do cliente

**Quando não souber algo:**
- Seja honesto sobre limitações
- Ofereça agendar suporte técnico personalizado
- Priorize clientes que usam resinas Quanton3D
"""
    
    def _build_knowledge_context(self, user_message):
        """
        Constrói contexto adicional baseado na base de conhecimento
        
        Args:
            user_message (str): Mensagem do usuário
            
        Returns:
            str: Contexto adicional relevante
        """
        context_parts = []
        
        # Detecta menção a resinas
        for resin in list_available_resins():
            if resin.lower() in user_message.lower() or resin.replace("_", " ").lower() in user_message.lower():
                props = get_resin_properties(resin)
                if props:
                    context_parts.append(f"\n**Informações sobre {resin}:**")
                    context_parts.append(f"- Descrição: {props['descricao']}")
                    context_parts.append(f"- Aplicações: {', '.join(props['aplicacoes'])}")
                    context_parts.append(f"- Cores disponíveis: {', '.join(props['cor_disponivel'])}")
                    context_parts.append(f"- Dureza Shore: {props['dureza_shore']}")
                    context_parts.append(f"- Resistência à tração: {props['resistencia_tracao']}")
        
        # Detecta problemas comuns
        problem_keywords = {
            "camadas": "camadas_visiveis",
            "linhas": "camadas_visiveis",
            "não adere": "peca_nao_adere",
            "nao adere": "peca_nao_adere",
            "descolou": "peca_nao_adere",
            "quebra": "peca_quebra_facilmente",
            "frágil": "peca_quebra_facilmente",
            "fragil": "peca_quebra_facilmente",
            "deformou": "deformacao",
            "empenado": "deformacao",
            "pegajosa": "superficie_pegajosa",
            "grudenta": "superficie_pegajosa"
        }
        
        for keyword, problem_key in problem_keywords.items():
            if keyword in user_message.lower():
                problem = get_problem_solution(problem_key)
                if problem:
                    context_parts.append(f"\n**Problema identificado: {problem['descricao']}**")
                    context_parts.append(f"Causas comuns:")
                    for causa in problem['causas']:
                        context_parts.append(f"  - {causa}")
                    context_parts.append(f"Soluções recomendadas:")
                    for solucao in problem['solucoes']:
                        context_parts.append(f"  - {solucao}")
                break
        
        return "\n".join(context_parts) if context_parts else ""
    
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
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Adiciona contexto da base de conhecimento
        knowledge_context = self._build_knowledge_context(prompt)
        if knowledge_context:
            messages.append({"role": "system", "content": f"Informações relevantes da base de conhecimento:\n{knowledge_context}"})
        
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
    
    def get_resin_configuration(self, resin_name, printer_brand, printer_model):
        """
        Busca configuração específica de uma resina para uma impressora
        
        Args:
            resin_name (str): Nome da resina
            printer_brand (str): Marca da impressora
            printer_model (str): Modelo da impressora
            
        Returns:
            dict: Configurações ou None se não encontrado
        """
        return get_resin_config(resin_name.upper(), printer_brand.upper(), printer_model.upper())
    
    def classify_problem(self, message):
        """
        Classifica o problema do usuário em básico, intermediário ou complexo
        
        Args:
            message (str): Mensagem do usuário
            
        Returns:
            str: Categoria do problema ("básico", "intermediário", "complexo")
        """
        classification_prompt = """
        Você é um especialista em suporte técnico para impressoras 3D SLA. 
        Classifique a seguinte mensagem de usuário em uma das três categorias:
        - "básico": Problemas comuns e fáceis de resolver (ex: configurações, dúvidas sobre resinas, problemas conhecidos).
        - "intermediário": Problemas que exigem mais investigação (ex: diagnóstico de hardware, otimização avançada).
        - "complexo": Problemas que precisam de análise visual ou intervenção humana (ex: posicionamento de suportes, erros complexos).
        
        Responda apenas com a categoria em letra minúscula.
        """
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": classification_prompt},
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
    
    def analyze_image(self, image_data, prompt=None):
        """
        Analisa uma imagem em busca de problemas de impressão 3D
        
        Args:
            image_data (bytes): Dados binários da imagem
            prompt (str): Pergunta específica sobre a imagem (opcional)
            
        Returns:
            str: Análise da imagem
        """
        # Converte imagem para base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        # Prompt padrão para análise de imagens
        if not prompt:
            prompt = """
Analise esta imagem de uma peça impressa em 3D com resina SLA/DLP.

Identifique:
1. Problemas visíveis (camadas visíveis, deformações, falhas de adesão, superfície pegajosa, etc.)
2. Possíveis causas dos problemas
3. Soluções recomendadas

Seja específico e técnico na sua análise.
"""
        
        payload = {
            "model": "grok-vision-beta",  # Modelo com suporte a visão
            "messages": [
                {
                    "role": "system",
                    "content": "Você é um especialista em impressão 3D SLA/DLP da Quanton3D. Analise imagens de peças impressas e identifique problemas e soluções."
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}",
                            },
                        },
                    ],
                }
            ],
            "max_tokens": 500,
            "temperature": 0.3
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            data = response.json()
            analysis = data['choices'][0]['message']['content'].strip()
            logger.info("Análise de imagem concluída com sucesso.")
            return analysis
        except Exception as e:
            logger.error(f"Erro ao analisar imagem: {e}")
            return "Desculpe, tive um problema ao analisar a imagem. Por favor, descreva o problema que você está vendo e tentarei ajudar da melhor forma possível."

