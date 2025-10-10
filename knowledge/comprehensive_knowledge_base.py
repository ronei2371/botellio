"""
BASE DE CONHECIMENTO COMPLETA E EXPANDIDA - BOTELLIO
Integração de TODO o conhecimento técnico mundial sobre impressão 3D SLA/DLP
Compilado de múltiplas fontes: Guias técnicos, PDFs, artigos científicos e experiência prática
"""

# =============================================================================
# CONHECIMENTO FUNDAMENTAL SOBRE IMPRESSORAS SLA/DLP
# =============================================================================

FUNDAMENTOS_TECNOLOGIA = {
    "principio_funcionamento": {
        "fotopolimerizacao": "Resinas líquidas fotossensíveis solidificadas por exposição à luz UV (355nm, 375nm ou 405nm)",
        "resolucao": "Precisão dimensional excepcional: 0.01mm de camada e tolerâncias < 0.1mm",
        "tecnologias": {
            "SLA": "Stereolithography - Laser UV de alta precisão percorre superfície da resina",
            "DLP": "Digital Light Processing - Projetores digitais com matriz DMD para cura simultânea",
            "LCD": "Painéis de cristal líquido mascaram luz de arrays LED UV (melhor custo-benefício)"
        }
    },
    
    "componentes_principais": {
        "sistema_projecao": {
            "SLA": "Laser UV 50-250mW em comprimentos 355nm, 375nm ou 405nm",
            "DLP": "Projetores digitais modificados com matriz de microespelhos (DMD)",
            "LCD": "Painéis LCD + arrays LED UV - excelente relação custo-benefício"
        },
        
        "plataforma_construcao": {
            "material": "Alumínio anodizado ou aço inoxidável",
            "planicidade": "Tolerância de paralelismo < 0.02mm em relação ao tanque",
            "textura": "Rugosidade controlada (jateamento ou texturização química) para adesão",
            "nivelamento": "Sistema de ajuste fino em múltiplos eixos com sensores de proximidade"
        },
        
        "tanque_resina_fep": {
            "material_tanque": "PTFE ou polipropileno (resistente a solventes)",
            "filme_fep": {
                "descricao": "Fluorinated Ethylene Propylene - filme transparente e flexível",
                "espessura": "0.1mm a 0.2mm",
                "funcao": "Permite passagem de luz UV e fornece superfície antiaderente",
                "tensao": "Fundamental para sucesso - tensão inadequada causa distorções",
                "durabilidade": "15-20 impressões em média, trocar ao primeiro sinal de turvação"
            },
            "alternativa_nfep": "Mais durável que FEP comum, recomendado para uso intensivo"
        },
        
        "sistema_movimentacao_z": {
            "motor": "Motor de passo ou servomotor acoplado a fuso de esferas",
            "precisao": "< 0.01mm para espessuras de camada consistentes",
            "encoders": "Feedback de posição em tempo real para correções automáticas",
            "rigidez": "Crucial para minimizar vibrações e deflexões"
        },
        
        "sistema_controle": {
            "processador": "ARM 32 bits para aplicações de tempo real",
            "interface": "LCD simples até touchscreen coloridas de alta resolução",
            "conectividade": "Wi-Fi e Ethernet para controle remoto",
            "cameras": "Supervisão visual remota do processo (modelos avançados)"
        }
    },
    
    "componentes_auxiliares": {
        "aquecimento": {
            "temperatura_ideal": "25°C a 35°C",
            "controle": "Resistências elétricas + termostatos precisos",
            "importancia": "Melhora fluidez, reduz viscosidade, otimiza cura"
        },
        
        "filtragem_ar": {
            "tipo": "Filtros de carvão ativado",
            "funcao": "Remover vapores orgânicos voláteis durante cura",
            "saude": "Essencial para segurança em ambientes fechados"
        }
    }
}

# =============================================================================
# RESINAS QUANTON3D - ESPECIFICAÇÕES COMPLETAS
# =============================================================================

RESINAS_QUANTON3D_COMPLETO = {
    "PYROBLAST": {
        "categoria": "Alta Performance",
        "caracteristicas": {
            "acabamento": "Excelente acabamento superficial",
            "resistencia": "Alta resistência mecânica",
            "aplicacoes": "Peças funcionais, protótipos de engenharia, modelos de apresentação"
        },
        "parametros_base": {
            "bottom_exposure": "25-30s",
            "normal_exposure": "2.5-3.5s",
            "bottom_layers": "6-8",
            "lift_speed": "60-80 mm/min",
            "retract_speed": "150-180 mm/min"
        },
        "temperatura": "25-30°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 3-5 minutos",
            "cura_uv": "10-15 minutos em câmara UV"
        }
    },
    
    "IRON_7620": {
        "categoria": "Resistência Extrema",
        "caracteristicas": {
            "resistencia_mecanica": "Extrema resistência ao impacto",
            "dureza": "Alta dureza Shore D",
            "aplicacoes": "Peças de engenharia, ferramental, componentes mecânicos"
        },
        "parametros_base": {
            "bottom_exposure": "30-35s",
            "normal_exposure": "3.0-4.0s",
            "bottom_layers": "8-10",
            "lift_speed": "50-70 mm/min",
            "retract_speed": "150-180 mm/min"
        },
        "temperatura": "28-32°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 5-7 minutos",
            "cura_uv": "15-20 minutos",
            "pos_cura_termica": "Opcional: 60°C por 2 horas para máximas propriedades"
        }
    },
    
    "IRON": {
        "categoria": "Robusta",
        "caracteristicas": {
            "resistencia": "Boa resistência ao impacto",
            "versatilidade": "Versátil para diversas aplicações",
            "aplicacoes": "Protótipos funcionais, peças de uso geral"
        },
        "parametros_base": {
            "bottom_exposure": "25-30s",
            "normal_exposure": "2.5-3.5s",
            "bottom_layers": "6-8",
            "lift_speed": "60-80 mm/min",
            "retract_speed": "150-180 mm/min"
        },
        "temperatura": "25-30°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 3-5 minutos",
            "cura_uv": "10-15 minutos"
        }
    },
    
    "SPIN": {
        "categoria": "Cura Rápida",
        "caracteristicas": {
            "velocidade": "Cura ultra-rápida",
            "acabamento": "Ótimo acabamento superficial",
            "aplicacoes": "Produção em série, protótipos rápidos"
        },
        "parametros_base": {
            "bottom_exposure": "20-25s",
            "normal_exposure": "1.8-2.5s",
            "bottom_layers": "5-6",
            "lift_speed": "80-100 mm/min",
            "retract_speed": "180-200 mm/min"
        },
        "temperatura": "23-28°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 2-4 minutos",
            "cura_uv": "8-12 minutos"
        }
    },
    
    "POSEIDON": {
        "categoria": "Resistente à Água",
        "caracteristicas": {
            "resistencia_agua": "Excelente resistência à água e umidade",
            "estabilidade": "Estabilidade dimensional em ambientes úmidos",
            "aplicacoes": "Peças para ambientes externos, componentes náuticos"
        },
        "parametros_base": {
            "bottom_exposure": "28-33s",
            "normal_exposure": "2.8-3.8s",
            "bottom_layers": "7-9",
            "lift_speed": "60-80 mm/min",
            "retract_speed": "150-180 mm/min"
        },
        "temperatura": "25-30°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 4-6 minutos",
            "cura_uv": "12-18 minutos",
            "cura_submersa": "Opcional: curar submerso em água para melhor acabamento"
        }
    },
    
    "RPO_4K": {
        "categoria": "Alta Resolução",
        "caracteristicas": {
            "resolucao": "Otimizada para impressoras 4K e superiores",
            "detalhes": "Captura de detalhes ultra-finos",
            "aplicacoes": "Miniaturas, joias, modelos de alta precisão"
        },
        "parametros_base": {
            "bottom_exposure": "25-30s",
            "normal_exposure": "2.0-2.8s",
            "bottom_layers": "6-8",
            "lift_speed": "70-90 mm/min",
            "retract_speed": "160-190 mm/min",
            "layer_height": "0.025-0.035mm (para máxima resolução)"
        },
        "temperatura": "24-28°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 3-5 minutos (cuidado com detalhes finos)",
            "cura_uv": "10-15 minutos"
        }
    },
    
    "SPARK": {
        "categoria": "Ultra-Rápida",
        "caracteristicas": {
            "velocidade": "Cura ultra-rápida - a mais rápida da linha",
            "produtividade": "Máxima produtividade",
            "aplicacoes": "Produção em massa, prototipagem rápida"
        },
        "parametros_base": {
            "bottom_exposure": "18-23s",
            "normal_exposure": "1.5-2.2s",
            "bottom_layers": "5-6",
            "lift_speed": "90-120 mm/min",
            "retract_speed": "200-250 mm/min"
        },
        "temperatura": "23-28°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 2-3 minutos",
            "cura_uv": "6-10 minutos"
        }
    },
    
    "FLEXFORM": {
        "categoria": "Flexível",
        "caracteristicas": {
            "flexibilidade": "Alta flexibilidade e elasticidade",
            "shore": "Shore A 60-80",
            "aplicacoes": "Vedações, gaxetas, peças flexíveis"
        },
        "parametros_base": {
            "bottom_exposure": "35-45s",
            "normal_exposure": "8.0-12.0s (muito maior que resinas rígidas)",
            "bottom_layers": "10-15",
            "lift_speed": "30-50 mm/min (muito lento)",
            "retract_speed": "100-150 mm/min"
        },
        "temperatura": "28-32°C (aquecimento essencial)",
        "pos_processamento": {
            "lavagem": "IPA 99% - 5-8 minutos (cuidado para não deformar)",
            "cura_uv": "15-25 minutos",
            "pos_cura_agua": "Curar submerso em água morna (50°C) para melhores propriedades"
        },
        "observacoes": "Requer suportes mais densos e finos. Lift speed muito lento é crítico."
    },
    
    "ALCHEMIST": {
        "categoria": "Premium",
        "caracteristicas": {
            "acabamento": "Acabamento excepcional",
            "qualidade": "Máxima qualidade superficial",
            "aplicacoes": "Modelos de apresentação, joias, peças de exposição"
        },
        "parametros_base": {
            "bottom_exposure": "25-30s",
            "normal_exposure": "2.3-3.0s",
            "bottom_layers": "6-8",
            "lift_speed": "60-80 mm/min",
            "retract_speed": "150-180 mm/min"
        },
        "temperatura": "25-30°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 3-5 minutos",
            "cura_uv": "12-18 minutos",
            "polimento": "Responde muito bem a lixamento e polimento para transparência"
        }
    },
    
    "LOWSMELL": {
        "categoria": "Baixo Odor",
        "caracteristicas": {
            "odor": "Baixíssimo odor - ideal para ambientes fechados",
            "conforto": "Maior conforto durante impressão",
            "aplicacoes": "Uso em escritórios, ambientes sem ventilação forçada"
        },
        "parametros_base": {
            "bottom_exposure": "25-30s",
            "normal_exposure": "2.5-3.5s",
            "bottom_layers": "6-8",
            "lift_speed": "60-80 mm/min",
            "retract_speed": "150-180 mm/min"
        },
        "temperatura": "25-30°C",
        "pos_processamento": {
            "lavagem": "IPA 99% - 3-5 minutos",
            "cura_uv": "10-15 minutos"
        },
        "observacoes": "Ideal para ambientes sem sistema de filtragem de ar"
    }
}

# =============================================================================
# IMPRESSORAS SUPORTADAS - CONFIGURAÇÕES ESPECÍFICAS
# =============================================================================

IMPRESSORAS_SUPORTADAS = {
    "ANYCUBIC": {
        "Photon_Mono": {
            "resolucao_xy": "0.051mm",
            "resolucao_z": "0.01mm",
            "volume": "130 x 80 x 165mm",
            "tela": "LCD 6.08\" 2K",
            "ajustes_resinas_quanton": {
                "PYROBLAST": {"bottom": "28s", "normal": "2.8s"},
                "IRON_7620": {"bottom": "32s", "normal": "3.5s"},
                "SPIN": {"bottom": "22s", "normal": "2.0s"}
            }
        },
        
        "Photon_Mono_X": {
            "resolucao_xy": "0.05mm",
            "resolucao_z": "0.01mm",
            "volume": "192 x 120 x 245mm",
            "tela": "LCD 8.9\" 4K",
            "ajustes_resinas_quanton": {
                "PYROBLAST": {"bottom": "30s", "normal": "3.0s"},
                "RPO_4K": {"bottom": "28s", "normal": "2.5s"},
                "ALCHEMIST": {"bottom": "28s", "normal": "2.8s"}
            }
        },
        
        "Photon_M3": {
            "resolucao_xy": "0.035mm",
            "resolucao_z": "0.01mm",
            "volume": "180 x 163 x 102mm",
            "tela": "LCD 7.6\" 4K+",
            "ajustes_resinas_quanton": {
                "RPO_4K": {"bottom": "25s", "normal": "2.3s"},
                "ALCHEMIST": {"bottom": "26s", "normal": "2.5s"}
            }
        },
        
        "Photon_M5S": {
            "resolucao_xy": "0.030mm",
            "resolucao_z": "0.01mm",
            "volume": "218 x 123 x 210mm",
            "tela": "LCD 10.1\" 12K",
            "ajustes_resinas_quanton": {
                "RPO_4K": {"bottom": "23s", "normal": "2.0s"},
                "ALCHEMIST": {"bottom": "24s", "normal": "2.2s"},
                "SPARK": {"bottom": "20s", "normal": "1.8s"}
            }
        }
    },
    
    "ELEGOO": {
        "Mars_3": {
            "resolucao_xy": "0.035mm",
            "resolucao_z": "0.01mm",
            "volume": "143 x 90 x 175mm",
            "tela": "LCD 6.66\" 4K",
            "ajustes_resinas_quanton": {
                "PYROBLAST": {"bottom": "27s", "normal": "2.7s"},
                "IRON": {"bottom": "28s", "normal": "2.9s"},
                "SPIN": {"bottom": "21s", "normal": "1.9s"}
            }
        },
        
        "Mars_4_Ultra": {
            "resolucao_xy": "0.018mm",
            "resolucao_z": "0.01mm",
            "volume": "153 x 77 x 165mm",
            "tela": "LCD 7\" 9K",
            "ajustes_resinas_quanton": {
                "RPO_4K": {"bottom": "22s", "normal": "1.9s"},
                "ALCHEMIST": {"bottom": "23s", "normal": "2.1s"},
                "SPARK": {"bottom": "19s", "normal": "1.6s"}
            }
        },
        
        "Saturn_2": {
            "resolucao_xy": "0.029mm",
            "resolucao_z": "0.01mm",
            "volume": "219 x 123 x 250mm",
            "tela": "LCD 10\" 8K",
            "ajustes_resinas_quanton": {
                "PYROBLAST": {"bottom": "29s", "normal": "2.9s"},
                "IRON_7620": {"bottom": "33s", "normal": "3.7s"},
                "POSEIDON": {"bottom": "31s", "normal": "3.3s"}
            }
        }
    },
    
    "CREALITY": {
        "LD_002R": {
            "resolucao_xy": "0.047mm",
            "resolucao_z": "0.01mm",
            "volume": "119 x 65 x 160mm",
            "tela": "LCD 5.5\" 2K",
            "ajustes_resinas_quanton": {
                "PYROBLAST": {"bottom": "30s", "normal": "3.2s"},
                "IRON": {"bottom": "31s", "normal": "3.4s"}
            }
        },
        
        "Halot_One": {
            "resolucao_xy": "0.05mm",
            "resolucao_z": "0.01mm",
            "volume": "127 x 80 x 160mm",
            "tela": "LCD 6.08\" 2K",
            "ajustes_resinas_quanton": {
                "PYROBLAST": {"bottom": "28s", "normal": "2.9s"},
                "SPIN": {"bottom": "22s", "normal": "2.1s"}
            }
        }
    },
    
    "PHROZEN": {
        "Sonic_Mini_4K": {
            "resolucao_xy": "0.035mm",
            "resolucao_z": "0.01mm",
            "volume": "134 x 75 x 130mm",
            "tela": "LCD 6.1\" 4K",
            "ajustes_resinas_quanton": {
                "RPO_4K": {"bottom": "25s", "normal": "2.4s"},
                "ALCHEMIST": {"bottom": "26s", "normal": "2.6s"}
            }
        }
    }
}

# Continua na próxima parte...

