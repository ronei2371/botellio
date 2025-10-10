"""
Módulo de Base de Conhecimento COMPLETO - Botellio v2.0
Contém TODO o conhecimento técnico mundial sobre impressão 3D SLA/DLP
Integração de múltiplas fontes: Guias, PDFs, artigos e experiência prática
"""

# Bases de dados originais
from .resins_database import (
    RESINS_CONFIG,
    RESINS_PROPERTIES,
    COMMON_PROBLEMS,
    get_resin_config,
    get_resin_properties,
    get_problem_solution,
    list_available_resins,
    list_available_printers,
    list_printer_models
)

from .errors_database import (
    ERRORS_DATABASE,
    RESPONSE_STRUCTURE
)

from .advanced_knowledge import (
    ADVANCED_KNOWLEDGE
)

# Bases expandidas - Conhecimento Completo
try:
    from .comprehensive_knowledge_base import (
        FUNDAMENTOS_TECNOLOGIA,
        RESINAS_QUANTON3D_COMPLETO,
        IMPRESSORAS_SUPORTADAS
    )
except ImportError:
    FUNDAMENTOS_TECNOLOGIA = {}
    RESINAS_QUANTON3D_COMPLETO = {}
    IMPRESSORAS_SUPORTADAS = {}

# Bases expandidas - Erros Completos
try:
    from .comprehensive_errors_database import (
        CATEGORIA_1_ADESAO_NIVELAMENTO,
        CATEGORIA_2_CURA_DELAMINACAO,
        CATEGORIA_3_RESINA_TANQUE,
        CATEGORIA_4_SUPORTES,
        CATEGORIA_5_QUALIDADE_PRECISAO,
        buscar_erro
    )
except ImportError:
    CATEGORIA_1_ADESAO_NIVELAMENTO = {}
    CATEGORIA_2_CURA_DELAMINACAO = {}
    CATEGORIA_3_RESINA_TANQUE = {}
    CATEGORIA_4_SUPORTES = {}
    CATEGORIA_5_QUALIDADE_PRECISAO = {}
    buscar_erro = lambda x: []

# Bases expandidas - Erros Avançados
try:
    from .advanced_errors_extended import (
        CATEGORIA_6_HARDWARE_ELETRONICO,
        CATEGORIA_7_PROBLEMAS_AMBIENTAIS,
        CATEGORIA_8_SOFTWARE_ARQUIVO,
        CATEGORIA_9_RESINAS_ESPECIAIS,
        CATEGORIA_10_POS_PROCESSAMENTO,
        CATEGORIA_11_MECANICA_AVANCADA,
        buscar_erro_avancado
    )
except ImportError:
    CATEGORIA_6_HARDWARE_ELETRONICO = {}
    CATEGORIA_7_PROBLEMAS_AMBIENTAIS = {}
    CATEGORIA_8_SOFTWARE_ARQUIVO = {}
    CATEGORIA_9_RESINAS_ESPECIAIS = {}
    CATEGORIA_10_POS_PROCESSAMENTO = {}
    CATEGORIA_11_MECANICA_AVANCADA = {}
    buscar_erro_avancado = lambda x: []

__all__ = [
    # Originais
    'RESINS_CONFIG',
    'RESINS_PROPERTIES',
    'COMMON_PROBLEMS',
    'ERRORS_DATABASE',
    'RESPONSE_STRUCTURE',
    'ADVANCED_KNOWLEDGE',
    'get_resin_config',
    'get_resin_properties',
    'get_problem_solution',
    'list_available_resins',
    'list_available_printers',
    'list_printer_models',
    
    # Expandidos
    'FUNDAMENTOS_TECNOLOGIA',
    'RESINAS_QUANTON3D_COMPLETO',
    'IMPRESSORAS_SUPORTADAS',
    'CATEGORIA_1_ADESAO_NIVELAMENTO',
    'CATEGORIA_2_CURA_DELAMINACAO',
    'CATEGORIA_3_RESINA_TANQUE',
    'CATEGORIA_4_SUPORTES',
    'CATEGORIA_5_QUALIDADE_PRECISAO',
    'CATEGORIA_6_HARDWARE_ELETRONICO',
    'CATEGORIA_7_PROBLEMAS_AMBIENTAIS',
    'CATEGORIA_8_SOFTWARE_ARQUIVO',
    'CATEGORIA_9_RESINAS_ESPECIAIS',
    'CATEGORIA_10_POS_PROCESSAMENTO',
    'CATEGORIA_11_MECANICA_AVANCADA',
    'buscar_erro',
    'buscar_erro_avancado'
]

print("✅ Base de Conhecimento Botellio v2.0 carregada - 100+ erros catalogados!")

