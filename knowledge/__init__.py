"""
Módulo de Base de Conhecimento - Botellio
Contém todas as informações sobre resinas, impressoras e problemas técnicos
"""
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

__all__ = [
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
    'list_printer_models'
]

