# -*- coding: utf-8 -*-
"""
Base de Conhecimento Avançado - Botellio v2.0
Conhecimento técnico mundial sobre impressão 3D SLA
Compilado de múltiplas fontes e 10+ anos de experiência técnica
"""

# Conhecimento expandido sobre problemas e soluções SLA
ADVANCED_KNOWLEDGE = {
    "problemas_criticos_adesao": {
        "peca_nao_gruda": {
            "diagnostico": "Problema de tensão superficial ou contaminação microscópica",
            "solucoes": [
                "Teste de gota d'água: Pingue água na base - se formar bolha, há contaminação oleosa",
                "Limpeza com acetona: Use acetona pura (não álcool) para remover óleos residuais",
                "Aquecimento da base: Aqueça base a 40-50°C antes da impressão",
                "Texturização microscópica: Lixe levemente com lixa 400 em movimentos circulares",
                "Limpeza final com IPA: Álcool Isopropílico 99% para desengordurar completamente"
            ],
            "configuracoes_extremas": {
                "primeira_camada": "120-180s (muito acima do normal)",
                "camadas_base": "15-20 (dobro do padrão)",
                "lift_speed": "0.5mm/s (extremamente lento)",
                "light_off_delay": "5-10s entre camadas"
            }
        },
        "z_axis_drift": {
            "diagnostico": "Problema mecânico no eixo Z ou perda de passos do motor",
            "solucoes": [
                "Calibração de steps/mm: Verificar se motor Z está configurado corretamente",
                "Lubrificação específica: Usar graxa de lítio no fuso (não óleo comum)",
                "Verificação de backlash: Testar folga no acoplamento motor-fuso",
                "Tensão da correia: Ajustar tensão se usar sistema de correia",
                "Temperatura do driver: Verificar aquecimento excessivo do driver do motor"
            ],
            "configuracoes_emergencia": {
                "velocidade_z": "50% do padrão",
                "corrente_motor": "Aumentar (cuidado com aquecimento)",
                "delay_movimentos": "Adicionar delay extra"
            }
        }
    },
    
    "problemas_cura_resina": {
        "zebra_striping": {
            "diagnostico": "Variação de potência do LED ou problema térmico",
            "solucoes": [
                "Mapeamento térmico: Verificar temperatura do LED durante impressão longa",
                "Calibração de potência: Usar luxímetro para medir uniformidade da luz",
                "Cooling forçado: Adicionar ventilação extra no LED",
                "Substituição do LED: LEDs degradam com uso - verificar vida útil",
                "Filtro UV: Verificar se filtro UV não está degradado"
            ],
            "configuracoes_compensatorias": {
                "exposicao": "+20-30% para compensar perda de potência",
                "anti_aliasing": "Nível 4-8 para suavizar transições",
                "altura_camada": "0.03mm"
            }
        },
        "resina_cozinha": {
            "diagnostico": "Vazamento de luz UV ou contaminação por partículas curadas",
            "solucoes": [
                "Vedação completa: Verificar se tampa está vedando 100% a luz",
                "Filtração urgente: Filtrar resina com malha 40 microns",
                "Teste de vazamento: Usar papel fotossensível para detectar vazamentos",
                "Limpeza profunda: Limpar tanque com álcool + ultrassom se disponível",
                "Substituição do FEP: FEP riscado pode causar dispersão de luz"
            ],
            "medidas_preventivas": [
                "Cobrir tanque com papel alumínio se necessário",
                "Trocar FEP a cada 15-20 impressões",
                "Armazenar resina em recipiente opaco"
            ]
        },
        "delaminacao": {
            "diagnostico": "Problema de adesão intercamadas ou contaminação pontual",
            "solucoes": [
                "Análise do arquivo: Verificar se há erro no G-code em altura específica",
                "Teste de temperatura: Medir temperatura ambiente durante impressão",
                "Limpeza do LCD: Limpar tela LCD - sujeira causa exposição irregular",
                "Verificação de vibração: Eliminar vibrações externas",
                "Mudança de orientação: Rotar peça 45° para distribuir tensões"
            ],
            "configuracoes_corretivas": {
                "lift_speed": "1mm/s na região problemática",
                "pause": "3-5s entre camadas críticas"
            }
        }
    },
    
    "problemas_suportes": {
        "suportes_derretem": {
            "diagnostico": "Superexposição localizada ou problema de dissipação de calor",
            "solucoes": [
                "Suportes graduais: Usar suportes que aumentam de espessura gradualmente",
                "Cooling localizado: Direcionar ventilação para área dos suportes",
                "Resina específica: Usar resina com menor contração térmica",
                "Orientação otimizada: Inclinar peça para reduzir área de suporte",
                "Suportes híbridos: Combinar suportes automáticos + manuais"
            ],
            "configuracoes_especiais": {
                "exposicao_suportes": "-20-30%",
                "espessura": "0.4-0.5mm (médios)",
                "densidade": "80-90%"
            }
        },
        "elephant_foot_suportes": {
            "diagnostico": "Deformação por peso próprio ou força de sucção excessiva",
            "solucoes": [
                "Suportes em árvore: Usar padrão de suporte ramificado",
                "Base expandida: Criar base mais larga para suportes principais",
                "Suportes duplos: Usar dois suportes paralelos em pontos críticos",
                "Hollow com drenos: Fazer peça oca com furos de drenagem",
                "Impressão em partes: Dividir peça grande em seções menores"
            ],
            "configuracoes_pecas_grandes": {
                "lift_speed": "0.8-1.2mm/s (muito lento)",
                "retract_speed": "1.5-2mm/s",
                "rest_before_lift": "3-5s",
                "rest_after_retract": "2-3s"
            }
        }
    },
    
    "problemas_qualidade": {
        "distorcao_dimensional": {
            "diagnostico": "Tensões internas da resina ou problema de calibração XY",
            "solucoes": [
                "Calibração XY: Imprimir cubo de calibração e medir dimensões reais",
                "Compensação de shrinkage: Aplicar fator de correção no slicer (101-103%)",
                "Pós-cura controlada: Usar câmara de cura com temperatura controlada",
                "Orientação estratégica: Orientar dimensões críticas no eixo Z",
                "Resina dimensional: Usar resina específica para precisão dimensional"
            ],
            "configuracoes_precisao": {
                "anti_aliasing": "Nível 2-4 (não muito alto)",
                "altura_camada": "0.025-0.035mm",
                "teste_exposicao": "XP2"
            }
        },
        "orange_peel": {
            "diagnostico": "Vibração, temperatura inadequada ou problema de viscosidade",
            "solucoes": [
                "Isolamento de vibração: Colocar impressora em base de concreto/granito",
                "Controle térmico rigoroso: Manter ±1°C de variação máxima",
                "Viscosidade otimizada: Aquecer resina a 25-27°C antes do uso",
                "Filtração fina: Usar filtro de 25 microns",
                "Velocidade otimizada: Reduzir todas as velocidades em 50%"
            ],
            "configuracoes_anti_vibracao": {
                "lift_speed": "1mm/s máximo",
                "retract_speed": "2mm/s máximo",
                "pause": "1-2s entre movimentos"
            }
        }
    },
    
    "problemas_hardware": {
        "stuck_pixels": {
            "diagnostico": "Degradação do LCD ou problema no driver de vídeo",
            "solucoes": [
                "Pixel refresh: Executar ciclo de refresh completo do LCD",
                "Teste de stress: Rodar padrão de teste por 30 minutos",
                "Verificação de cabo: Verificar conexão do cabo flat do LCD",
                "Atualização de firmware: Atualizar firmware da impressora",
                "Substituição preventiva: LCD tem vida útil limitada (500-1000h)"
            ],
            "configuracoes_compensatorias": {
                "exposicao": "+10-15%",
                "anti_aliasing": "Para suavizar bordas"
            }
        },
        "aquecimento_excessivo": {
            "diagnostico": "Problema de dissipação térmica ou sobrecarga elétrica",
            "solucoes": [
                "Ventilação forçada: Adicionar ventiladores extras",
                "Dissipadores extras: Instalar dissipadores nos drivers de motor",
                "Relocação: Mover eletrônica para fora da câmara aquecida",
                "Verificação elétrica: Medir corrente dos motores",
                "Pasta térmica: Reaplicar pasta térmica nos componentes críticos"
            ],
            "configuracoes_protecao": {
                "corrente_motores": "80% do máximo",
                "pause": "5 minutos a cada 2 horas"
            }
        }
    },
    
    "problemas_ambientais": {
        "alta_umidade": {
            "diagnostico": "Absorção de umidade pela resina ou condensação no LCD",
            "solucoes": [
                "Desumidificação: Usar desumidificador no ambiente (manter <50%)",
                "Aquecimento preventivo: Aquecer impressora 30min antes do uso",
                "Vedação: Vedar completamente a câmara da impressora",
                "Sílica gel: Colocar sachês de sílica gel próximo à resina",
                "Pré-aquecimento da resina: Aquecer resina a 30°C antes do uso"
            ],
            "configuracoes": {
                "exposicao": "+15-20%",
                "teste_calibracao": "Diário"
            }
        },
        "variacao_temperatura": {
            "diagnostico": "Expansão térmica diferencial ou mudança de viscosidade",
            "solucoes": [
                "Isolamento térmico: Isolar impressora com espuma ou caixa térmica",
                "Aquecimento ativo: Instalar aquecedor com termostato",
                "Compensação automática: Usar sensor de temperatura + ajuste automático",
                "Massa térmica: Adicionar massa térmica (água) para estabilizar",
                "Programação horária: Imprimir apenas em horários estáveis"
            ],
            "configuracoes_termicas": {
                "ajuste_exposicao": "-10% para cada 5°C acima de 25°C"
            }
        }
    },
    
    "problemas_software": {
        "corrupcao_arquivo": {
            "diagnostico": "Problema no cartão SD, USB ou memória da impressora",
            "solucoes": [
                "Verificação de integridade: Usar checksum MD5",
                "Cartão SD industrial: Usar cartão SD de alta durabilidade (SLC)",
                "Backup redundante: Salvar arquivo em múltiplas localizações",
                "Fragmentação: Desfragmentar cartão SD regularmente",
                "Teste de stress: Testar cartão SD com software específico"
            ],
            "configuracoes_seguranca": [
                "Usar cartão SD classe 10 ou superior",
                "Formatar cartão a cada 10 impressões",
                "Manter backup dos arquivos críticos"
            ]
        },
        "layers_perdidas": {
            "diagnostico": "Problema de processamento do slicer ou limitação de memória",
            "solucoes": [
                "Simplificação de mesh: Reduzir número de polígonos do STL",
                "Divisão de arquivo: Dividir modelo complexo em partes menores",
                "Slicer alternativo: Testar com diferentes slicers",
                "Aumento de RAM: Usar computador com mais memória para fatiar",
                "Verificação de STL: Usar Netfabb ou 3D Builder para reparar"
            ],
            "configuracoes_otimizacao": {
                "anti_aliasing": "Reduzir para modelos complexos",
                "altura_camada": "0.05-0.08mm"
            }
        }
    },
    
    "problemas_mecanicos": {
        "desgaste_fep": {
            "diagnostico": "Tensão inadequada, química incompatível ou abrasão excessiva",
            "solucoes": [
                "Tensão otimizada: Usar medidor de tensão ou app de frequência sonora",
                "Lubrificação: Aplicar PTFE spray no FEP (muito pouco)",
                "Química compatível: Verificar compatibilidade resina-FEP",
                "Limpeza suave: Usar apenas espátula de plástico macio",
                "Substituição por nFEP: Usar nFEP (mais durável que FEP comum)"
            ],
            "configuracoes_preservar_fep": {
                "lift_speed": "Máximo 2mm/s",
                "area_impressao": "Evitar >50% da área"
            }
        },
        "ruido_excessivo": {
            "diagnostico": "Desgaste de componentes mecânicos ou desalinhamento",
            "solucoes": [
                "Lubrificação completa: Lubrificar todos os pontos de atrito",
                "Alinhamento de eixos: Verificar alinhamento de guias lineares",
                "Substituição de rolamentos: Trocar rolamentos desgastados",
                "Isolamento acústico: Usar espuma acústica na carcaça",
                "Balanceamento: Verificar balanceamento de partes móveis"
            ],
            "configuracoes_silenciosas": {
                "velocidades": "-30-50%",
                "aceleracao": "Suave"
            }
        }
    },
    
    "resinas_especiais": {
        "flexivel": {
            "diagnostico": "Inibição por oxigênio ou configuração inadequada para elastômeros",
            "solucoes": [
                "Atmosfera inerte: Usar câmara com nitrogênio para cura final",
                "Exposição prolongada: Aumentar tempo em 50-100%",
                "Pós-cura específica: Usar comprimento de onda específico (405nm)",
                "Temperatura controlada: Manter 20-22°C",
                "Suportes especiais: Usar suportes mais densos e finos"
            ],
            "configuracoes": {
                "lift_speed": "0.5-1mm/s (muito lento)",
                "exposicao": "2-3x o tempo de resina rígida",
                "camadas_base": "10-15"
            }
        },
        "ceramica": {
            "diagnostico": "Separação de fases ou agitação inadequada",
            "solucoes": [
                "Agitação contínua: Usar agitador magnético durante impressão",
                "Homogeneização: Misturar por 10-15 minutos antes do uso",
                "Viscosidade ajustada: Aquecer a 30-35°C",
                "Filtração cuidadosa: Usar filtro de 100 microns",
                "Armazenamento vertical: Armazenar em pé para evitar sedimentação"
            ],
            "configuracoes": {
                "exposicao": "+30-50%",
                "agitacao": "A cada 30 minutos"
            }
        }
    },
    
    "pos_processamento": {
        "deformacao_pos_cura": {
            "diagnostico": "Tensões internas liberadas pelo calor ou cura não uniforme",
            "solucoes": [
                "Cura gradual: Aumentar tempo gradualmente (2min → 4min → 6min)",
                "Suporte durante cura: Manter peça suportada durante cura UV",
                "Temperatura controlada: Manter <40°C durante cura",
                "Rotação contínua: Usar plataforma giratória para cura uniforme",
                "Pré-aquecimento: Aquecer peça gradualmente antes da cura"
            ],
            "configuracoes": {
                "ciclos": "Múltiplos ciclos curtos",
                "pausas": "5 minutos entre ciclos",
                "monitoramento": "Termômetro IR"
            }
        },
        "opacidade_apos_lavagem": {
            "diagnostico": "Resíduo de álcool ou reação química com a resina",
            "solucoes": [
                "Álcool de alta pureza: Usar IPA 99.9% (não 70%)",
                "Lavagem em etapas: 1ª lavagem (álcool sujo) → 2ª lavagem (álcool limpo)",
                "Secagem forçada: Usar ar comprimido para remover álcool residual",
                "Alternativa ao álcool: Usar Mean Green ou Simple Green",
                "Banho ultrassônico: 3-5 minutos em álcool com ultrassom"
            ],
            "processo_otimizado": {
                "tempo_maximo": "5 minutos por banho",
                "temperatura": "Ambiente (não aquecer álcool)",
                "secagem": "10 minutos ao ar antes da cura UV"
            }
        }
    },
    
    "diagnostico_rapido": {
        "falha_mesma_altura": {
            "causa": "Arquivo corrompido ou eixo Z",
            "solucao_imediata": "Refatiar + verificar mecânica",
            "configuracao": "Reduzir velocidade Z 50%"
        },
        "cura_apenas_bordas": {
            "causa": "LCD com pixels mortos",
            "solucao_imediata": "Mapear pixels + compensar",
            "configuracao": "Aumentar exposição 15%"
        },
        "separacao_camadas": {
            "causa": "Contaminação ou vibração",
            "solucao_imediata": "Filtrar resina + isolar vibração",
            "configuracao": "Lift speed 1mm/s"
        }
    },
    
    "protocolos_manutencao": {
        "diagnostico_sistematico": [
            "1. Verificação básica: Nivelamento, limpeza, arquivo",
            "2. Teste de hardware: Dry run, teste de LCD, movimento de eixos",
            "3. Teste de resina: Gota ao sol, teste no tanque vazio",
            "4. Análise ambiental: Temperatura, umidade, vibração",
            "5. Verificação eletrônica: Tensões, correntes, aquecimento",
            "6. Análise de arquivo: Integridade, complexidade, compatibilidade"
        ],
        "calibracao_mensal": [
            "1. Calibração XY: Imprimir cubo de teste e medir",
            "2. Calibração Z: Verificar altura de camadas reais",
            "3. Teste de exposição: XP2 Validation Matrix completo",
            "4. Verificação de LCD: Mapa de pixels e uniformidade",
            "5. Manutenção mecânica: Lubrificação e ajustes",
            "6. Limpeza profunda: Tanque, FEP, LCD, filtros"
        ],
        "prevencao_falhas": [
            "1. Monitoramento contínuo: Temperatura, umidade, vibração",
            "2. Manutenção preventiva: Cronograma de substituições",
            "3. Backup de configurações: Perfis testados e aprovados",
            "4. Documentação de falhas: Registro para análise futura",
            "5. Treinamento contínuo: Atualização de conhecimento técnico"
        ]
    }
}

# Dicas e melhores práticas gerais
BEST_PRACTICES = {
    "limpeza_manutencao": [
        "Limpar LCD com microfibra e álcool isopropílico 99.9%",
        "Trocar FEP a cada 15-20 impressões ou ao primeiro sinal de opacidade",
        "Filtrar resina com malha 40 microns após cada impressão falhada",
        "Lubrificar eixo Z mensalmente com graxa de lítio",
        "Verificar nivelamento da base semanalmente"
    ],
    "armazenamento_resina": [
        "Armazenar em local escuro e fresco (15-25°C)",
        "Usar recipientes opacos e herméticos",
        "Agitar suavemente antes do uso (não criar bolhas)",
        "Não misturar resinas de marcas diferentes",
        "Verificar prazo de validade (geralmente 12 meses)"
    ],
    "configuracoes_iniciais": [
        "Sempre fazer teste de exposição (XP2) com resina nova",
        "Começar com configurações do fabricante e ajustar gradualmente",
        "Documentar todas as alterações e resultados",
        "Usar perfis diferentes para cada tipo de resina",
        "Salvar backup das configurações que funcionam"
    ],
    "seguranca": [
        "Usar luvas de nitrilo (não látex) ao manusear resina",
        "Trabalhar em ambiente ventilado",
        "Usar óculos de proteção durante limpeza",
        "Nunca descartar resina no ralo - curar ao sol antes do descarte",
        "Lavar mãos após manuseio mesmo com luvas"
    ]
}

def get_solution_for_problem(problem_keyword):
    """
    Busca soluções baseadas em palavra-chave do problema
    """
    solutions = []
    
    for category, problems in ADVANCED_KNOWLEDGE.items():
        for problem_name, problem_data in problems.items():
            if problem_keyword.lower() in problem_name.lower() or problem_keyword.lower() in str(problem_data).lower():
                solutions.append({
                    "categoria": category,
                    "problema": problem_name,
                    "dados": problem_data
                })
    
    return solutions

def get_quick_diagnosis(symptom):
    """
    Diagnóstico rápido baseado em sintoma
    """
    quick_diag = ADVANCED_KNOWLEDGE.get("diagnostico_rapido", {})
    
    for key, data in quick_diag.items():
        if symptom.lower() in key.lower():
            return data
    
    return None

