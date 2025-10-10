"""
Sistema de Diagnóstico e Resposta Estruturada - Botellio
"""

from knowledge.errors_database import get_error_info, format_response
from services.ai_service import get_grok_analysis

def get_structured_response(problem_description, image_url=None):
    """
    Gera uma resposta estruturada em 3 etapas para um problema.
    """
    # 1. Tenta encontrar o erro na base de dados local
    error_info = get_error_info(problem_description)
    
    if error_info:
        return format_response(error_info)
    
    # 2. Se não encontrar, usa a IA para uma análise mais profunda
    # (especialmente útil para problemas complexos ou não catalogados)
    prompt = f"""
    Analise o seguinte problema de impressão 3D SLA e forneça uma resposta técnica completa seguindo a estrutura de 3 etapas:
    
    **Problema:** {problem_description}
    
    **Estrutura da Resposta:**
    1. **DIAGNÓSTICO PRIMÁRIO:** Qual a causa raiz mais provável?
    2. **SOLUÇÃO IMEDIATA:** O que o usuário deve fazer agora para tentar resolver?
    3. **PROTOCOLO AVANÇADO:** Quais são os passos avançados para prevenção e otimização máxima?
    """
    
    if image_url:
        prompt += f"\n\n**Análise de Imagem:** Analise a imagem em {image_url} para ajudar no diagnóstico."
        
    # Chama o serviço da IA (Grok)
    ai_response = get_grok_analysis(prompt, image_url)
    
    return ai_response

