"""
Base de Conhecimento Completa de Erros e Soluções - Impressão 3D SLA
Compilado de Conhecimento Mundial + Experiência Técnica Quanton3D
"""

# Estrutura de resposta em 3 etapas
RESPONSE_STRUCTURE = {
    "step_1": "🔍 DIAGNÓSTICO PRIMÁRIO",
    "step_2": "🛠 SOLUÇÃO IMEDIATA",
    "step_3": "⚙ PROTOCOLO AVANÇADO"
}

# Base de dados de erros categorizados
ERRORS_DATABASE = {
    # CATEGORIA 1: PROBLEMAS CRÍTICOS DE ADESÃO
    "peca_nao_gruda": {
        "categoria": "Adesão Crítica",
        "diagnostico": "Problema de tensão superficial, contaminação microscópica, ou subexposição da base",
        "solucao_imediata": "Aumente o Bottom Exposure Time em 20% e re-nivele a plataforma com folha de calibração",
        "protocolo_avancado": {
            "1": "Teste de gota d'água: Pingue água na base - se formar bolha, há contaminação oleosa",
            "2": "Limpeza com acetona: Use acetona pura (não álcool) para remover óleos residuais",
            "3": "Texturização microscópica: Lixe levemente com lixa 400 em movimentos circulares",
            "4": "Aquecimento da base: Aqueça base a 40-50°C antes da impressão"
        },
        "configuracoes": {
            "bottom_exposure_time": "120-180s",
            "bottom_layers": "15-20",
            "lift_speed": "0.5mm/s",
            "light_off_delay": "5-10s"
        }
    },
    
    "base_afunda": {
        "categoria": "Adesão Crítica",
        "diagnostico": "Problema mecânico no eixo Z ou perda de passos do motor",
        "solucao_imediata": "Reduza a velocidade Z para 50% do padrão e verifique lubrificação do fuso",
        "protocolo_avancado": {
            "1": "Calibração de steps/mm: Verificar se motor Z está configurado corretamente",
            "2": "Lubrificação específica: Usar graxa de lítio no fuso (não óleo comum)",
            "3": "Verificação de backlash: Testar folga no acoplamento motor-fuso",
            "4": "Tensão da correia: Ajustar tensão se usar sistema de correia"
        },
        "configuracoes": {
            "z_speed": "50% do padrão",
            "motor_current": "Aumentar com cuidado",
            "delay_between_moves": "Adicionar extra"
        }
    },
    
    # CATEGORIA 2: PROBLEMAS DE CURA E DELAMINAÇÃO
    "separacao_camadas": {
        "categoria": "Tensão e Cura Intercamada",
        "diagnostico": "Subexposição da camada normal ou tensão excessiva de descolamento (Peel Force)",
        "solucao_imediata": "Aumente o tempo de exposição da camada normal em 0.5s",
        "protocolo_avancado": {
            "1": "Otimização de Ângulo: Reposicione a peça para ter o menor volume de seção transversal possível (ângulos de 15° a 45°)",
            "2": "Controle de Movimento: Reduza a LiftSpeed para 40 mm/min para as primeiras 20 camadas",
            "3": "Manutenção Crítica: Verifique se o FEP está sem clouding na área de impressão"
        },
        "configuracoes": {
            "normal_exposure_time": "+0.5s",
            "lift_speed": "40 mm/min",
            "light_off_delay": "+0.5-1s"
        }
    },
    
    "zebra_striping": {
        "categoria": "Cura e Resina",
        "diagnostico": "Variação de potência do LED ou problema térmico",
        "solucao_imediata": "Aumente exposição em 20-30% para compensar perda de potência",
        "protocolo_avancado": {
            "1": "Mapeamento térmico: Verificar temperatura do LED durante impressão longa",
            "2": "Calibração de potência: Usar luxímetro para medir uniformidade da luz",
            "3": "Cooling forçado: Adicionar ventilação extra no LED",
            "4": "Substituição do LED: LEDs degradam com uso - verificar vida útil"
        },
        "configuracoes": {
            "exposure_time": "+20-30%",
            "anti_aliasing": "Nível 4-8",
            "layer_height": "0.03mm"
        }
    },
    
    "resina_cozinha": {
        "categoria": "Cura e Resina",
        "diagnostico": "Vazamento de luz UV ou contaminação por partículas curadas",
        "solucao_imediata": "Filtre a resina com malha 40 microns e verifique vedação da tampa",
        "protocolo_avancado": {
            "1": "Vedação completa: Verificar se tampa está vedando 100% a luz",
            "2": "Filtração urgente: Filtrar resina com malha 40 microns",
            "3": "Teste de vazamento: Usar papel fotossensível para detectar vazamentos",
            "4": "Limpeza profunda: Limpar tanque com álcool + ultrassom",
            "5": "Substituição do FEP: FEP riscado pode causar dispersão de luz"
        },
        "configuracoes": {
            "preventivo": "Cobrir tanque com papel alumínio",
            "manutencao": "Trocar FEP a cada 15-20 impressões",
            "armazenamento": "Recipiente opaco"
        }
    },
    
    # CATEGORIA 3: PROBLEMAS DE SUPORTES
    "suportes_falham": {
        "categoria": "Suportes e Estruturas",
        "diagnostico": "Pontos de contato muito pequenos, pouca densidade de suporte ou falta de penetração",
        "solucao_imediata": "Aumente a penetração da ponta do suporte na malha da peça (de 0.2mm para 0.4mm)",
        "protocolo_avancado": {
            "1": "Diâmetro do Ponto de Contato: Aumentar para 0.4mm ou 0.5mm",
            "2": "Ângulo de Suporte: Adicionar suportes manuais nos pontos mais íngremes",
            "3": "Estabilidade: Adicionar suportes pesados ou médios na base",
            "4": "Angulação da Peça: Inclinar a peça em 15° a 45°"
        },
        "configuracoes": {
            "penetration": "0.4mm",
            "tip_diameter": "0.4-0.5mm",
            "angle": "15-45°"
        }
    },
    
    "suportes_derretem": {
        "categoria": "Suportes e Estruturas",
        "diagnostico": "Superexposição localizada ou problema de dissipação de calor",
        "solucao_imediata": "Reduza exposição dos suportes em 20-30%",
        "protocolo_avancado": {
            "1": "Suportes graduais: Usar suportes que aumentam de espessura gradualmente",
            "2": "Cooling localizado: Direcionar ventilação para área dos suportes",
            "3": "Resina específica: Usar resina com menor contração térmica",
            "4": "Orientação otimizada: Inclinar peça para reduzir área de suporte"
        },
        "configuracoes": {
            "support_exposure": "-20-30%",
            "support_size": "Médios (0.4-0.5mm)",
            "density": "80-90%"
        }
    },
    
    # CATEGORIA 4: PROBLEMAS DE DETALHES E GEOMETRIA
    "detalhes_ausentes": {
        "categoria": "Detalhe e Geometria",
        "diagnostico": "Super-exposição (cura em excesso arredonda as quinas) ou Anti-Aliasing agressivo",
        "solucao_imediata": "Reduza o tempo de exposição em 0.1s e verifique o Anti-Aliasing",
        "protocolo_avancado": {
            "1": "Reduzir exposição: Passos de 0.1s até encontrar o ponto ideal",
            "2": "Verificar AA/Grayscale: Manter AA baixo (nível 2-4) ou desativar",
            "3": "Layer Height: Reduzir para 0.025mm para melhor resolução"
        },
        "configuracoes": {
            "exposure_time": "-0.1s por vez",
            "anti_aliasing": "Nível 2-4 ou OFF",
            "layer_height": "0.025mm"
        }
    },
    
    "layer_lines": {
        "categoria": "Detalhe e Geometria",
        "diagnostico": "Super-exposição (expansão lateral da cura) ou Velocidade de Lift/Retract muito alta",
        "solucao_imediata": "Diminua o tempo de exposição e reduza a velocidade do motor Z",
        "protocolo_avancado": {
            "1": "Calibração do Eixo Z: Verificar folgas ou sujeira no fuso",
            "2": "Reduzir velocidade: Lift Speed/Retract Speed para 60 mm/min ou menos",
            "3": "Layer Height: Usar 0.03mm para maior detalhe"
        },
        "configuracoes": {
            "lift_speed": "60 mm/min ou menos",
            "retract_speed": "60 mm/min ou menos",
            "layer_height": "0.03mm"
        }
    },
    
    # CATEGORIA 5: PROBLEMAS DE PÓS-PROCESSAMENTO
    "peca_quebradica": {
        "categoria": "Pós-Processamento",
        "diagnostico": "Lavagem insuficiente (monômeros residuais) ou super-cura UV",
        "solucao_imediata": "Lave em dois banhos de IPA (sujo inicial e limpo final) e seque completamente",
        "protocolo_avancado": {
            "1": "Lavagem em Duas Etapas: IPA sujo inicial + IPA limpo final",
            "2": "Secagem Completa: Ar comprimido ou esperar 30 minutos",
            "3": "Tempo de Cura Otimizado: 5-15 minutos dependendo da resina",
            "4": "Cura Submersa: Para algumas resinas, curar submersa em água melhora a cura"
        },
        "configuracoes": {
            "ipa_concentration": "90-99%",
            "cure_time": "5-15 minutos",
            "drying": "Completa antes da cura"
        }
    },
    
    "superficie_aspera": {
        "categoria": "Pós-Processamento",
        "diagnostico": "Lavagem insuficiente ou super-cura UV",
        "solucao_imediata": "Lave em dois estágios de IPA e reduza o tempo de cura UV",
        "protocolo_avancado": {
            "1": "IPA Concentration: Usar 95% ou 99%",
            "2": "Post-Cure Time: Reduzir para 5-10 minutos",
            "3": "Secar completamente antes da cura final"
        },
        "configuracoes": {
            "ipa": "95-99%",
            "cure_time": "5-10 minutos"
        }
    },
    
    # CATEGORIA 6: PROBLEMAS MECÂNICOS E HARDWARE
    "z_wobble": {
        "categoria": "Hardware e Mecânica",
        "diagnostico": "Desalinhamento do acoplador motor/fuso ou parafusos-guia desgastados",
        "solucao_imediata": "Limpe o fuso com IPA e aplique graxa de lítio branca",
        "protocolo_avancado": {
            "1": "Desmontagem e Limpeza: Limpar fuso e aplicar graxa de lítio",
            "2": "Aperto: Verificar se acoplador está firme e centralizado",
            "3": "Firmware/Calibração: Rodar rotinas de calibração do motor Z"
        },
        "configuracoes": {
            "lubrication": "Graxa de lítio branca",
            "calibration": "Steps/mm"
        }
    },
    
    "fep_pop": {
        "categoria": "Hardware e Mecânica",
        "diagnostico": "Pressão negativa excessiva (vácuo) dentro de modelos ocos e grandes",
        "solucao_imediata": "Adicione 2-4 furos de alívio de pressão na parte superior e inferior do modelo oco",
        "protocolo_avancado": {
            "1": "Orifícios de Respiro: Adicionar furos de 2mm de diâmetro",
            "2": "Angulação: Otimizar para área de contato FEP-camada mínima",
            "3": "Retract Speed: Reduzir para 150-200 mm/min",
            "4": "Lift Distance: Aumentar em 1-2mm"
        },
        "configuracoes": {
            "retract_speed": "150-200 mm/min",
            "lift_distance": "+1-2mm",
            "wait_before_lift": "2-5s"
        }
    },
    
    # CATEGORIA 7: RESINAS ESPECIAIS
    "resina_flexivel_quebra": {
        "categoria": "Resinas Especiais",
        "diagnostico": "Sub-cura ou resina não atingiu temperatura ideal de transição vítrea (Tg)",
        "solucao_imediata": "Aumente exposição em 2-3x e use aquecedor de tanque para manter 30-35°C",
        "protocolo_avancado": {
            "1": "Aumento Extremo da Exposição: 2-3x mais tempo (ex: 4s para 12s)",
            "2": "Pré-aquecimento: Manter resina a 30-35°C durante impressão",
            "3": "Pós-Cura em Água Quente: Curar submersa em água morna (50°C)"
        },
        "configuracoes": {
            "exposure_time": "2-3x normal",
            "resin_temp": "30-35°C",
            "post_cure": "Água quente 50°C"
        }
    },
    
    "peca_transparente_turva": {
        "categoria": "Resinas Especiais",
        "diagnostico": "Lavagem incompleta, super-cura UV ou água/IPA residual",
        "solucao_imediata": "Use IPA 99% e reduza tempo de pós-cura UV para 5 minutos",
        "protocolo_avancado": {
            "1": "Lavagem: IPA 99% e trocar frequentemente",
            "2": "Cura Controlada: Reduzir para 5 minutos",
            "3": "Clareamento: Aplicar verniz transparente UV após cura",
            "4": "Lixamento e Polimento: Lixar do grão 400 ao 3000 + polimento"
        },
        "configuracoes": {
            "ipa": "99%",
            "cure_time": "5 minutos",
            "polishing": "Grão 400-3000"
        }
    }
}

# Problemas comuns e suas categorias
COMMON_PROBLEMS = {
    "peça não gruda": "peca_nao_gruda",
    "descola": "peca_nao_gruda",
    "não adere": "peca_nao_gruda",
    "base afunda": "base_afunda",
    "z-axis drift": "base_afunda",
    "camadas separam": "separacao_camadas",
    "delaminação": "separacao_camadas",
    "layer splitting": "separacao_camadas",
    "listras": "zebra_striping",
    "zebra": "zebra_striping",
    "resina cura no tanque": "resina_cozinha",
    "suportes quebram": "suportes_falham",
    "suportes falham": "suportes_falham",
    "suportes derretem": "suportes_derretem",
    "detalhes finos": "detalhes_ausentes",
    "perda de detalhe": "detalhes_ausentes",
    "linhas de camada": "layer_lines",
    "layer lines": "layer_lines",
    "peça quebradiça": "peca_quebradica",
    "peça melada": "peca_quebradica",
    "superfície áspera": "superficie_aspera",
    "superfície grudenta": "superficie_aspera",
    "z-wobble": "z_wobble",
    "oscilação z": "z_wobble",
    "fep pop": "fep_pop",
    "estalo": "fep_pop",
    "resina flexível quebra": "resina_flexivel_quebra",
    "transparente turva": "peca_transparente_turva",
    "amarelada": "peca_transparente_turva"
}

def get_error_info(problem_description):
    """
    Retorna informações sobre um erro baseado na descrição do problema
    """
    problem_lower = problem_description.lower()
    
    # Procura por palavras-chave
    for keyword, error_key in COMMON_PROBLEMS.items():
        if keyword in problem_lower:
            return ERRORS_DATABASE.get(error_key)
    
    return None

def format_response(error_info):
    """
    Formata a resposta no padrão de 3 etapas
    """
    if not error_info:
        return None
    
    response = f"""
{RESPONSE_STRUCTURE['step_1']}: {error_info['diagnostico']}

{RESPONSE_STRUCTURE['step_2']}: {error_info['solucao_imediata']}

{RESPONSE_STRUCTURE['step_3']}:
"""
    
    for key, value in error_info['protocolo_avancado'].items():
        response += f"\n{key}. {value}"
    
    response += "\n\n⚙️ CONFIGURAÇÕES RECOMENDADAS:\n"
    for key, value in error_info['configuracoes'].items():
        response += f"• {key.replace('_', ' ').title()}: {value}\n"
    
    return response

