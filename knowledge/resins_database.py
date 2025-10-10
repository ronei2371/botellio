"""
Base de Conhecimento Completa - Resinas e Impressoras Quanton3D
Atualizado em: Outubro 2025
"""

# Estrutura de dados para todas as configurações de resinas por impressora
RESINS_CONFIG = {
    "PYROBLAST": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 8, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2, "tempo_exposicao_base": 70},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 35},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 35},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 1.9, "tempo_exposicao_base": 35},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2, "tempo_exposicao_base": 35},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 1.9, "tempo_exposicao_base": 40},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2, "tempo_exposicao_base": 35},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.1, "tempo_exposicao_base": 35},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 1.9, "tempo_exposicao_base": 35},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 1.9, "tempo_exposicao_base": 35},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 8, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2, "tempo_exposicao_base": 35},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2, "tempo_exposicao_base": 35},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 1.8, "tempo_exposicao_base": 35},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 8, "tempo_exposicao_base": 60},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 6, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
        }
    },
    "IRON_7620": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 80},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 80},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 80},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 30},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 30},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 11, "tempo_exposicao_base": 80},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 30},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 30},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 30},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        }
    },
    "IRON": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 25},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 25},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 25},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 25},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "HALOT LITE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
        }
    },
    "SPIN": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.7, "tempo_exposicao_base": 30},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.7, "tempo_exposicao_base": 30},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "SKY ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT LITE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        }
    },
    "POSEIDON": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.9, "tempo_exposicao_base": 50},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.7, "tempo_exposicao_base": 50},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.7, "tempo_exposicao_base": 50},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.9, "tempo_exposicao_base": 50},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.9, "tempo_exposicao_base": 50},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.7, "tempo_exposicao_base": 50},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.8, "tempo_exposicao_base": 50},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.7, "tempo_exposicao_base": 50},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.7, "tempo_exposicao_base": 50},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 50},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 50},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.3, "tempo_exposicao_base": 50},
            "SKY ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 11, "tempo_exposicao_base": 70},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
            "HALOT LITE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 50},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2.5, "tempo_exposicao_base": 50},
        }
    },
    "RPO_4K": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.7, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "SKY ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        }
    },
    "SPARK": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 9.7, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 9.7, "tempo_exposicao_base": 70},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 9.7, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 30},
            "SKY ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 9.7, "tempo_exposicao_base": 70},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
        }
    },
    "FLEXFORM": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 12, "tempo_exposicao_base": 80},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 12, "tempo_exposicao_base": 80},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 12, "tempo_exposicao_base": 80},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 35},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 35},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.3, "tempo_exposicao_base": 35},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 12, "tempo_exposicao_base": 80},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 35},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 35},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 3, "tempo_exposicao_base": 35},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2.5, "tempo_exposicao_base": 35},
        }
    },
    "ALCHEMIST": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 9, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 9, "tempo_exposicao_base": 70},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 25},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 9, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 25},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 25},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 25},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 9, "tempo_exposicao_base": 70},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
            "HALOT LITE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 25},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 1.9, "tempo_exposicao_base": 25},
        }
    },
    "LOWSMELL": {
        "ANYCUBIC": {
            "PHOTON CLÁSSICA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "PHOTON SE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "PHOTON MONO 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO X 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO X 6K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON M3 4K": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON M3 MAX": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.7, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
            "PHOTON MONO M5S PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
        },
        "ELEGOO": {
            "MARS 1": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "MARS 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "MARS 3 PRO": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "SATURN 2": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2, "tempo_exposicao_base": 30},
            "SATURN 3 ULTRA": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 1.8, "tempo_exposicao_base": 30},
        },
        "CREALITY": {
            "LD-002R": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 10, "tempo_exposicao_base": 70},
            "LD-006": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT ONE": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
            "HALOT SKY": {"altura_camada": "0.05mm", "camadas_base": 8, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        },
        "PHROZEN": {
            "MINI 4K": {"altura_camada": "0.05mm", "camadas_base": 10, "tempo_exposicao": 2.5, "tempo_exposicao_base": 30},
        }
    },
}

# Informações sobre características das resinas
RESIN_PROPERTIES = {
    "PYROBLAST": {
        "descricao": "Resina de alta performance com excelente acabamento superficial",
        "aplicacoes": ["Miniaturas", "Protótipos", "Peças decorativas"],
        "cor_disponivel": ["Cinza", "Branco", "Preto", "Transparente"],
        "dureza_shore": "80D",
        "resistencia_tracao": "Alta"
    },
    "IRON_7620": {
        "descricao": "Resina técnica de alta resistência mecânica",
        "aplicacoes": ["Peças funcionais", "Protótipos industriais", "Ferramentas"],
        "cor_disponivel": ["Cinza"],
        "dureza_shore": "85D",
        "resistencia_tracao": "Muito Alta"
    },
    "IRON": {
        "descricao": "Resina robusta com boa resistência ao impacto",
        "aplicacoes": ["Peças funcionais", "Protótipos", "Ferramentas"],
        "cor_disponivel": ["Cinza", "Preto"],
        "dureza_shore": "82D",
        "resistencia_tracao": "Alta"
    },
    "SPIN": {
        "descricao": "Resina de cura rápida com ótimo acabamento",
        "aplicacoes": ["Miniaturas", "Joias", "Protótipos"],
        "cor_disponivel": ["Cinza", "Branco", "Preto"],
        "dureza_shore": "78D",
        "resistencia_tracao": "Média-Alta"
    },
    "POSEIDON": {
        "descricao": "Resina resistente à água com excelente estabilidade dimensional",
        "aplicacoes": ["Peças expostas à umidade", "Protótipos", "Moldes"],
        "cor_disponivel": ["Azul", "Cinza"],
        "dureza_shore": "80D",
        "resistencia_tracao": "Alta"
    },
    "RPO_4K": {
        "descricao": "Resina otimizada para impressoras 4K com alta resolução",
        "aplicacoes": ["Miniaturas detalhadas", "Joias", "Odontologia"],
        "cor_disponivel": ["Cinza", "Branco"],
        "dureza_shore": "75D",
        "resistencia_tracao": "Média"
    },
    "SPARK": {
        "descricao": "Resina de cura ultra-rápida com excelente fluidez",
        "aplicacoes": ["Produção em massa", "Protótipos rápidos"],
        "cor_disponivel": ["Cinza", "Branco", "Preto"],
        "dureza_shore": "77D",
        "resistencia_tracao": "Média-Alta"
    },
    "FLEXFORM": {
        "descricao": "Resina flexível com alta elasticidade",
        "aplicacoes": ["Peças flexíveis", "Vedações", "Protótipos elásticos"],
        "cor_disponivel": ["Transparente", "Preto"],
        "dureza_shore": "60A-80A",
        "resistencia_tracao": "Média (flexível)"
    },
    "ALCHEMIST": {
        "descricao": "Resina premium com acabamento excepcional",
        "aplicacoes": ["Joias", "Miniaturas premium", "Protótipos de alta qualidade"],
        "cor_disponivel": ["Cinza", "Branco", "Transparente"],
        "dureza_shore": "83D",
        "resistencia_tracao": "Muito Alta"
    },
    "LOWSMELL": {
        "descricao": "Resina com baixo odor, ideal para ambientes fechados",
        "aplicacoes": ["Uso doméstico", "Escritórios", "Protótipos"],
        "cor_disponivel": ["Cinza", "Branco"],
        "dureza_shore": "79D",
        "resistencia_tracao": "Alta"
    },
}

# Problemas comuns e soluções
COMMON_PROBLEMS = {
    "camadas_visiveis": {
        "descricao": "Linhas horizontais visíveis na superfície da peça",
        "causas": [
            "Altura de camada muito grande",
            "Tempo de exposição inadequado",
            "Resina de baixa qualidade"
        ],
        "solucoes": [
            "Reduzir altura de camada para 0.025mm ou 0.03mm",
            "Ajustar tempo de exposição conforme tabela",
            "Usar resina de qualidade Quanton3D"
        ]
    },
    "peca_nao_adere": {
        "descricao": "Peça não adere à plataforma de construção",
        "causas": [
            "Plataforma mal nivelada",
            "Tempo de exposição base muito baixo",
            "Plataforma suja ou com resina curada"
        ],
        "solucoes": [
            "Nivelar plataforma corretamente",
            "Aumentar tempo de exposição base",
            "Limpar plataforma com álcool isopropílico"
        ]
    },
    "peca_quebra_facilmente": {
        "descricao": "Peça impressa é frágil e quebra com facilidade",
        "causas": [
            "Tempo de exposição muito baixo",
            "Resina vencida ou mal armazenada",
            "Pós-cura insuficiente"
        ],
        "solucoes": [
            "Aumentar tempo de exposição em 10-20%",
            "Verificar validade da resina",
            "Fazer pós-cura adequada (UV por 5-10 minutos)"
        ]
    },
    "deformacao": {
        "descricao": "Peça apresenta deformações ou empenamento",
        "causas": [
            "Tensões internas durante a cura",
            "Resfriamento desigual",
            "Suportes insuficientes"
        ],
        "solucoes": [
            "Adicionar mais suportes",
            "Orientar peça de forma adequada",
            "Fazer pós-cura gradual"
        ]
    },
    "superficie_pegajosa": {
        "descricao": "Superfície da peça permanece pegajosa após impressão",
        "causas": [
            "Limpeza inadequada",
            "Pós-cura insuficiente",
            "Resina não totalmente curada"
        ],
        "solucoes": [
            "Lavar bem com álcool isopropílico",
            "Aumentar tempo de pós-cura",
            "Verificar se resina está dentro da validade"
        ]
    }
}

def get_resin_config(resin_name, printer_brand, printer_model):
    """
    Retorna a configuração de impressão para uma resina específica em uma impressora específica
    
    Args:
        resin_name: Nome da resina (ex: "PYROBLAST")
        printer_brand: Marca da impressora (ex: "ANYCUBIC")
        printer_model: Modelo da impressora (ex: "PHOTON MONO 4K")
    
    Returns:
        dict: Configurações de impressão ou None se não encontrado
    """
    try:
        return RESINS_CONFIG[resin_name][printer_brand][printer_model]
    except KeyError:
        return None

def get_resin_properties(resin_name):
    """
    Retorna as propriedades de uma resina específica
    
    Args:
        resin_name: Nome da resina (ex: "PYROBLAST")
    
    Returns:
        dict: Propriedades da resina ou None se não encontrado
    """
    return RESIN_PROPERTIES.get(resin_name)

def get_problem_solution(problem_key):
    """
    Retorna informações sobre um problema comum e suas soluções
    
    Args:
        problem_key: Chave do problema (ex: "camadas_visiveis")
    
    Returns:
        dict: Informações sobre o problema ou None se não encontrado
    """
    return COMMON_PROBLEMS.get(problem_key)

def list_available_resins():
    """Retorna lista de todas as resinas disponíveis"""
    return list(RESINS_CONFIG.keys())

def list_available_printers(resin_name):
    """Retorna lista de marcas de impressoras disponíveis para uma resina"""
    if resin_name in RESINS_CONFIG:
        return list(RESINS_CONFIG[resin_name].keys())
    return []

def list_printer_models(resin_name, printer_brand):
    """Retorna lista de modelos de impressoras disponíveis para uma resina e marca"""
    try:
        return list(RESINS_CONFIG[resin_name][printer_brand].keys())
    except KeyError:
        return []

