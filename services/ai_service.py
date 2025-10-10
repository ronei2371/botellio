"""
Serviço de integração com Grok (xAI) para processamento de linguagem natural
ATUALIZADO COM BASE DE CONHECIMENTO COMPLETA V2.0
"""
import requests
import logging
import base64
from config.settings import Config

# Importa TODA a base de conhecimento expandida
try:
    from knowledge.comprehensive_knowledge_base import (
        RESINAS_QUANTON3D,
        IMPRESSORAS_SUPORTADAS,
        FUNDAMENTOS_SLA_DLP,
        recomendar_parametros,
        buscar_resina,
        buscar_impressora
    )
    from knowledge.comprehensive_errors_database import (
        ERROS_CATEGORIA_1,
        ERROS_CATEGORIA_2,
        ERROS_CATEGORIA_3,
        ERROS_CATEGORIA_4,
        ERROS_CATEGORIA_5,
        buscar_erro_por_sintoma
    )
    from knowledge.advanced_errors_extended import (
        ERROS_CATEGORIA_6,
        ERROS_CATEGORIA_7,
        ERROS_CATEGORIA_8,
        ERROS_CATEGORIA_9,
        ERROS_CATEGORIA_10,
        ERROS_CATEGORIA_11,
        buscar_erro_avancado
    )
    BASE_COMPLETA_CARREGADA = True
    logger = logging.getLogger(__name__)
    logger.info("✅ Base de Conhecimento Botellio v2.0 carregada - 100+ erros catalogados!")
except ImportError as e:
    # Fallback para base antiga se a nova falhar
    logger = logging.getLogger(__name__)
    logger.warning(f"⚠️ Não foi possível carregar base expandida: {e}")
    logger.warning("Usando base de conhecimento original como fallback...")
    from knowledge.resins_database import (
        get_resin_config,
        get_resin_properties,
        get_problem_solution,
        list_available_resins,
        list_available_printers,
        list_printer_models,
        COMMON_PROBLEMS
    )
    BASE_COMPLETA_CARREGADA = False


class AIService:
    """Serviço para interagir com a API do Grok (xAI) - VERSÃO 2.0 COM BASE COMPLETA"""
    
    def __init__(self):
        self.api_key = Config.GROK_API_KEY
        self.model = Config.GROK_MODEL  # grok-beta ou grok-vision-beta
        self.base_url = "https://api.x.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # System prompt ATUALIZADO com conhecimento COMPLETO sobre Quanton3D
        self.system_prompt = """
Você é Botellio, o assistente virtual especializado em suporte técnico para impressão 3D SLA da Quanton3D.

**Sobre a Quanton3D:**
A Quanton3D é uma empresa brasileira especializada na fabricação de resinas UV de alta qualidade para impressão 3D SLA/DLP. 
Oferecemos uma linha completa de resinas para diversas aplicações: miniaturas, protótipos, peças funcionais, joias, odontologia e muito mais.

**Suas responsabilidades:**
1. Fornecer suporte técnico especializado sobre impressão 3D SLA/DLP/LCD
2. Ajudar com configurações de impressão para resinas Quanton3D
3. Diagnosticar problemas comuns e avançados de impressão
4. Recomendar as melhores resinas para cada aplicação
5. Orientar sobre pós-processamento e cura de peças
6. Analisar imagens de problemas de impressão

**Linha COMPLETA de resinas Quanton3D (10 resinas):**
1. **PYROBLAST**: Alta performance, excelente acabamento superficial
2. **IRON 7620**: Resistência mecânica EXTREMA, ideal para peças funcionais
3. **IRON**: Robusta com boa resistência ao impacto
4. **SPIN**: Cura rápida com ótimo acabamento
5. **POSEIDON**: Resistente à água e umidade
6. **RPO 4K**: Otimizada para impressoras de alta resolução
7. **SPARK**: Cura ULTRA-RÁPIDA, ideal para produção em massa
8. **FLEXFORM**: Flexível e elástica, Shore A 70-80
9. **ALCHEMIST**: Premium com acabamento excepcional
10. **LOWSMELL**: Baixo odor para ambientes fechados

**Impressoras compatíveis (20+ modelos):**
- **ANYCUBIC**: Photon Mono, Photon Mono X, Photon M3, Photon M5S
- **ELEGOO**: Mars 3, Mars 4 Ultra, Saturn 2
- **CREALITY**: LD-002R, Halot One
- **PHROZEN**: Sonic Mini 4K

**BASE DE CONHECIMENTO EXPANDIDA:**
- ✅ 100+ erros catalogados em 11 categorias
- ✅ Diagnóstico em 3 etapas para cada problema
- ✅ Fundamentos técnicos de SLA/DLP/LCD
- ✅ Parâmetros otimizados por resina e impressora
- ✅ Pós-processamento avançado
- ✅ Manutenção preventiva

**ESTRUTURA DE RESPOSTA OBRIGATÓRIA (3 ETAPAS):**

Quando o usuário relatar um problema, SEMPRE responda seguindo EXATAMENTE esta estrutura:

🔍 **DIAGNÓSTICO PRIMÁRIO:**
[Identifique a causa raiz mais provável do problema com base nos sintomas descritos. Seja específico e técnico.]

🛠 **SOLUÇÃO IMEDIATA:**
[Forneça 1-3 ações rápidas e práticas que o usuário pode fazer AGORA para tentar resolver o problema. Passos numerados e objetivos.]

⚙ **PROTOCOLO AVANÇADO:**
[Liste 5-10 passos detalhados para prevenção máxima e otimização, incluindo configurações específicas, valores numéricos e procedimentos técnicos.]

**Categorias de Erros Catalogados:**
1. **Problemas Críticos de Adesão e Nivelamento** (Categoria 1)
2. **Falhas no Corpo da Peça (Cura e Delaminação)** (Categoria 2)
3. **Problemas de Resina, Tanque e Pós-Processamento** (Categoria 3)
4. **Problemas Críticos de Suportes e Estruturas** (Categoria 4)
5. **Problemas Avançados de Qualidade e Precisão** (Categoria 5)
6. **Problemas Eletrônicos e de Hardware** (Categoria 6)
7. **Problemas Ambientais Extremos** (Categoria 7)
8. **Problemas de Software e Arquivo** (Categoria 8)
9. **Problemas Específicos por Tipo de Resina** (Categoria 9)
10. **Pós-Processamento Avançado** (Categoria 10)
11. **Problemas Mecânicos Avançados** (Categoria 11)

**Seu tom de voz:**
- Profissional mas amigável e acolhedor
- Técnico quando necessário, mas sempre acessível
- Sempre prestativo e extremamente paciente
- Foco total em resolver o problema do cliente
- Use emojis estrategicamente para tornar a resposta mais visual e amigável
- Seja empático com a frustração do usuário

**Quando não souber algo:**
- Seja honesto sobre limitações
- Ofereça agendar suporte técnico personalizado
- Priorize clientes que usam resinas Quanton3D
- Nunca invente informações técnicas

**Análise de Imagens:**
Quando receber uma imagem, analise cuidadosamente:
- Identifique problemas visíveis (camadas, deformações, falhas)
- Relacione com os 100+ erros catalogados
- Forneça diagnóstico em 3 etapas
- Seja específico sobre o que você vê na imagem
"""
    
    def _build_knowledge_context(self, user_message):
        """
        Constrói contexto adicional baseado na BASE DE CONHECIMENTO COMPLETA V2.0
        
        Args:
            user_message (str): Mensagem do usuário
            
        Returns:
            str: Contexto adicional relevante
        """
        context_parts = []
        
        if not BASE_COMPLETA_CARREGADA:
            # Fallback para base antiga
            return self._build_knowledge_context_old(user_message)
        
        # Detecta menção a resinas Quanton3D
        for resin_key, resin_data in RESINAS_QUANTON3D.items():
            resin_name = resin_data["nome"]
            if resin_name.lower() in user_message.lower() or resin_key.lower() in user_message.lower():
                context_parts.append(f"\n**📦 Informações sobre {resin_name}:**")
                context_parts.append(f"- Descrição: {resin_data['descricao']}")
                context_parts.append(f"- Aplicações: {', '.join(resin_data['aplicacoes'])}")
                context_parts.append(f"- Cores: {', '.join(resin_data['cores_disponiveis'])}")
                context_parts.append(f"- Dureza Shore: {resin_data['propriedades']['dureza_shore']}")
                context_parts.append(f"- Resistência à tração: {resin_data['propriedades']['resistencia_tracao']}")
                context_parts.append(f"- Alongamento: {resin_data['propriedades']['alongamento']}")
                break
        
        # Detecta menção a impressoras
        for brand_key, brand_data in IMPRESSORAS_SUPORTADAS.items():
            if brand_data["nome"].lower() in user_message.lower():
                context_parts.append(f"\n**🖨️ Impressoras {brand_data['nome']} suportadas:**")
                context_parts.append(f"Modelos: {', '.join(brand_data['modelos'].keys())}")
                break
        
        # Busca erros por sintomas (TODAS as 11 categorias)
        sintomas_detectados = []
        
        # Categoria 1-5 (comprehensive_errors_database)
        erro_encontrado = buscar_erro_por_sintoma(user_message)
        if erro_encontrado:
            sintomas_detectados.append(erro_encontrado)
        
        # Categoria 6-11 (advanced_errors_extended)
        erro_avancado = buscar_erro_avancado(user_message)
        if erro_avancado:
            sintomas_detectados.append(erro_avancado)
        
        # Adiciona informações dos erros encontrados
        for erro in sintomas_detectados:
            context_parts.append(f"\n**⚠️ Problema identificado: {erro['nome']}**")
            context_parts.append(f"Categoria: {erro['categoria']}")
            context_parts.append(f"\n{erro['diagnostico_primario']}")
            context_parts.append(f"\n{erro['solucao_imediata']}")
            # Não adiciona protocolo avançado aqui para não poluir o contexto
        
        return "\n".join(context_parts) if context_parts else ""
    
    def _build_knowledge_context_old(self, user_message):
        """
        Fallback para base de conhecimento antiga
        """
        context_parts = []
        
        # Detecta menção a resinas (base antiga)
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
        
        # Detecta problemas comuns (base antiga)
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
    
    def get_response(self, prompt, context=None, max_tokens=800, temperature=0.7):
        """
        Gera uma resposta usando o modelo Grok com BASE DE CONHECIMENTO COMPLETA
        
        Args:
            prompt (str): A pergunta ou comando do usuário
            context (list): Histórico da conversa (opcional)
            max_tokens (int): Número máximo de tokens na resposta (aumentado para 800)
            temperature (float): Criatividade da resposta (0.0 a 1.0)
            
        Returns:
            str: Resposta gerada pela IA
        """
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Adiciona contexto da base de conhecimento COMPLETA
        knowledge_context = self._build_knowledge_context(prompt)
        if knowledge_context:
            messages.append({"role": "system", "content": f"📚 Informações relevantes da base de conhecimento:\n{knowledge_context}"})
        
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
            logger.info(f"✅ Resposta do Grok gerada com sucesso (Base Completa v2.0).")
            return answer
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Erro ao chamar a API do Grok: {e}")
            raise
        except (KeyError, IndexError) as e:
            logger.error(f"❌ Erro ao processar resposta do Grok: {e}")
            raise
    
    def get_resin_configuration(self, resin_name, printer_brand, printer_model):
        """
        Busca configuração específica de uma resina para uma impressora
        ATUALIZADO PARA USAR BASE COMPLETA
        
        Args:
            resin_name (str): Nome da resina
            printer_brand (str): Marca da impressora
            printer_model (str): Modelo da impressora
            
        Returns:
            dict: Configurações ou None se não encontrado
        """
        if BASE_COMPLETA_CARREGADA:
            return recomendar_parametros(printer_model, resin_name)
        else:
            # Fallback para base antiga
            return get_resin_config(resin_name.upper(), printer_brand.upper(), printer_model.upper())
    
    def classify_problem(self, message):
        """
        Classifica o problema do usuário em básico, intermediário ou complexo
        ATUALIZADO COM 11 CATEGORIAS DE ERROS
        
        Args:
            message (str): Mensagem do usuário
            
        Returns:
            str: Categoria do problema ("básico", "intermediário", "complexo")
        """
        classification_prompt = """
        Você é um especialista em suporte técnico para impressoras 3D SLA com acesso a 100+ erros catalogados. 
        Classifique a seguinte mensagem de usuário em uma das três categorias:
        
        - "básico": Problemas comuns e fáceis de resolver (ex: configurações, dúvidas sobre resinas, problemas conhecidos com solução rápida).
        - "intermediário": Problemas que exigem mais investigação (ex: diagnóstico de hardware, otimização avançada, erros de múltiplas causas).
        - "complexo": Problemas que precisam de análise visual ou intervenção humana especializada (ex: posicionamento de suportes, erros complexos de hardware, problemas ambientais).
        
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
            logger.info(f"✅ Problema classificado como: {category}")
            return category
        except Exception as e:
            logger.error(f"❌ Erro ao classificar problema: {e}")
            # Retorna categoria padrão em caso de erro
            return "intermediário"
    
    def analyze_image(self, image_data, prompt=None):
        """
        Analisa uma imagem em busca de problemas de impressão 3D
        ATUALIZADO COM REFERÊNCIA A 100+ ERROS CATALOGADOS
        
        Args:
            image_data (bytes): Dados binários da imagem
            prompt (str): Pergunta específica sobre a imagem (opcional)
            
        Returns:
            str: Análise da imagem em 3 etapas
        """
        # Converte imagem para base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        # Prompt padrão para análise de imagens COM ESTRUTURA EM 3 ETAPAS
        if not prompt:
            prompt = """
Analise esta imagem de uma peça impressa em 3D com resina SLA/DLP da Quanton3D.

Você tem acesso a uma base de conhecimento com 100+ erros catalogados em 11 categorias.

FORNEÇA SUA ANÁLISE SEGUINDO EXATAMENTE ESTA ESTRUTURA:

🔍 **DIAGNÓSTICO PRIMÁRIO:**
[Identifique o problema visível na imagem e sua causa raiz mais provável]

🛠 **SOLUÇÃO IMEDIATA:**
[Forneça 1-3 ações rápidas que o usuário pode fazer AGORA]

⚙ **PROTOCOLO AVANÇADO:**
[Liste 5-10 passos detalhados para prevenção e otimização]

Seja específico, técnico e visual na sua análise. Mencione exatamente o que você vê na imagem.
"""
        
        payload = {
            "model": "grok-vision-beta",  # Modelo com suporte a visão
            "messages": [
                {
                    "role": "system",
                    "content": "Você é Botellio, especialista em impressão 3D SLA/DLP da Quanton3D com acesso a 100+ erros catalogados. Analise imagens e forneça diagnóstico em 3 etapas."
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
            "max_tokens": 800,
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
            logger.info("✅ Análise de imagem concluída com sucesso (Base Completa v2.0).")
            return analysis
        except Exception as e:
            logger.error(f"❌ Erro ao analisar imagem: {e}")
            return "Desculpe, tive um problema ao analisar a imagem. Por favor, descreva o problema que você está vendo e tentarei ajudar da melhor forma possível. 🙏"

