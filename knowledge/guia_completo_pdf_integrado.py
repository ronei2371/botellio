"""
GUIA COMPLETO DE IMPRESSÃO 3D DE RESINA - INTEGRAÇÃO TOTAL
Baseado no PDF de 98 páginas criado por Elio para Ronei

Este módulo contém TODOS os 14 módulos do guia completo:
1. Explicação sobre partes de uma impressora
2. Equipamentos de segurança
3. Fatiadores e tipos de resina
4. Como calibrar resina
5. Como fazer suportes
6. Como separar modelos
7. Como nivelar impressora
8. Como colocar para imprimir
9. Lavagem e cura
10. Cuidados pós-impressão
11. Polimento e remoção de suportes
12. Erros e soluções (já integrado via CONHECIMENTO.txt)
13. Sugestões de investimentos
14. Marcas confiáveis
"""

# ============================================================================
# MÓDULO 1: PARTES DA IMPRESSORA 3D DE RESINA
# ============================================================================

PARTES_IMPRESSORA = {
    "fonte_de_luz": {
        "nome": "Fonte de Luz UV (LCD/DLP)",
        "funcao": "Emite luz ultravioleta para curar a resina fotopolimerizável",
        "tipos": {
            "LCD": "Tela LCD monocromática que bloqueia luz seletivamente",
            "DLP": "Projetor digital que projeta imagem completa da camada",
            "LASER": "Laser que traça o contorno da camada (tecnologia SLA clássica)"
        },
        "cuidados": [
            "Nunca olhe diretamente para a luz UV",
            "Limpe regularmente com pano de microfibra",
            "Substitua quando perder intensidade (geralmente após 2000-4000h)"
        ]
    },
    "tanque_de_resina": {
        "nome": "Tanque de Resina (Vat/Cuba)",
        "funcao": "Contém a resina líquida durante a impressão",
        "componentes": {
            "filme_fep": "Filme transparente no fundo que permite passagem da luz UV",
            "estrutura": "Moldura de alumínio ou plástico que segura o filme FEP",
            "niveladores": "Parafusos para nivelar o tanque"
        },
        "cuidados": [
            "Limpe após cada impressão com IPA 99%",
            "Verifique rasgos no filme FEP regularmente",
            "Substitua FEP a cada 20-50 impressões ou quando opaco",
            "Nunca deixe resina parada no tanque por mais de 1 semana"
        ],
        "substituicao_fep": {
            "frequencia": "A cada 20-50 impressões ou quando apresentar opacidade/rasgos",
            "sinais": [
                "Opacidade ou manchas no filme",
                "Rasgos ou furos",
                "Peças grudando no FEP com frequência",
                "Perda de detalhes nas impressões"
            ],
            "procedimento": [
                "1. Remova resina do tanque e limpe completamente",
                "2. Desparafuse a moldura inferior",
                "3. Remova FEP antigo",
                "4. Limpe moldura com IPA",
                "5. Corte novo FEP no tamanho correto",
                "6. Estique FEP uniformemente (tensão média)",
                "7. Aparafuse moldura gradualmente em cruz",
                "8. Teste batendo levemente - deve soar como tambor"
            ]
        }
    },
    "plataforma_de_construcao": {
        "nome": "Plataforma de Construção (Build Plate)",
        "funcao": "Superfície onde a peça é construída camada por camada",
        "materiais": ["Alumínio anodizado", "Aço inoxidável", "Alumínio com textura"],
        "cuidados": [
            "Limpe com acetona antes de cada impressão",
            "Lixe levemente com lixa 400-600 para melhorar adesão",
            "Nivele precisamente antes de imprimir",
            "Nunca use força excessiva ao remover peças"
        ],
        "nivelamento": {
            "frequencia": "Antes de cada impressão ou a cada 5-10 impressões",
            "metodo_papel": [
                "1. Coloque folha de papel A4 entre plataforma e FEP",
                "2. Abaixe plataforma até encostar no papel",
                "3. Papel deve ter resistência leve ao puxar",
                "4. Trave a plataforma nessa posição",
                "5. Defina Z=0 no menu da impressora"
            ],
            "metodo_flint_read": [
                "1. Limpe FEP e plataforma",
                "2. Coloque 2-3 gotas de resina no centro do FEP",
                "3. Abaixe plataforma até encostar na resina",
                "4. Resina deve se espalhar uniformemente",
                "5. Levante plataforma e limpe resina",
                "6. Defina Z=0"
            ]
        }
    },
    "eixo_z": {
        "nome": "Eixo Z (Eixo Vertical)",
        "funcao": "Move a plataforma para cima e para baixo",
        "componentes": {
            "motor_de_passo": "Motor que controla movimento preciso",
            "fuso_trapezoidal": "Haste roscada que converte rotação em movimento linear",
            "guias_lineares": "Trilhos que garantem movimento suave e preciso"
        },
        "cuidados": [
            "Lubrifique fuso a cada 50 impressões com graxa PTFE",
            "Limpe guias lineares com pano seco",
            "Verifique folgas e aperte parafusos se necessário",
            "Nunca force movimento manual quando ligado"
        ]
    },
    "placa_controladora": {
        "nome": "Placa Controladora (Mainboard)",
        "funcao": "Cérebro da impressora que controla todos os componentes",
        "cuidados": [
            "Mantenha longe de umidade",
            "Não toque nos componentes eletrônicos",
            "Use estabilizador de tensão",
            "Atualize firmware apenas se necessário"
        ]
    },
    "tela_touch": {
        "nome": "Tela Touch/Interface",
        "funcao": "Interface para controlar a impressora e iniciar impressões",
        "cuidados": [
            "Limpe com pano de microfibra seco",
            "Não pressione com força excessiva",
            "Proteja de respingos de resina"
        ]
    }
}

# ============================================================================
# MÓDULO 2: EQUIPAMENTOS DE SEGURANÇA
# ============================================================================

EQUIPAMENTOS_SEGURANCA = {
    "epi_obrigatorios": {
        "luvas_nitrilo": {
            "importancia": "CRÍTICA",
            "motivo": "Resina não curada é tóxica e pode causar dermatite de contato",
            "tipo": "Luvas de nitrilo (NÃO use látex - resina dissolve)",
            "quando_usar": "SEMPRE que manusear resina líquida",
            "descarte": "Após cada uso ou se rasgarem"
        },
        "oculos_protecao": {
            "importancia": "CRÍTICA",
            "motivo": "Luz UV pode danificar retina, resina pode espirrar nos olhos",
            "tipo": "Óculos de proteção UV com vedação lateral",
            "quando_usar": "Durante impressão e limpeza",
            "cuidados": ["Limpe com água e sabão", "Não use se arranhados"]
        },
        "mascara_respiratoria": {
            "importancia": "ALTA",
            "motivo": "Vapores de resina podem causar irritação respiratória e sensibilização",
            "tipo": "Máscara com filtro para vapores orgânicos (P2/P3)",
            "quando_usar": "Em ambientes fechados ou ao lixar peças",
            "troca_filtro": "A cada 40-80 horas de uso ou quando sentir odor"
        },
        "avental": {
            "importancia": "MÉDIA",
            "motivo": "Protege roupas de respingos de resina",
            "tipo": "Avental de PVC ou silicone",
            "quando_usar": "Durante toda manipulação de resina",
            "limpeza": "Lave com água e sabão após cada uso"
        }
    },
    "equipamentos_ambiente": {
        "exaustor": {
            "importancia": "ALTA",
            "funcao": "Remove vapores tóxicos do ambiente",
            "tipos": ["Exaustor de janela", "Sistema de ventilação forçada", "Cabine com filtro de carvão"],
            "recomendacao": "Mantenha ligado durante e 30min após impressão"
        },
        "organizador_ferramentas": {
            "importancia": "MÉDIA",
            "funcao": "Mantém área organizada e segura",
            "itens": ["Espátulas", "Alicate de corte", "Pinças", "Pincéis", "Recipientes para IPA"]
        },
        "tapete_absorvente": {
            "importancia": "MÉDIA",
            "funcao": "Absorve respingos de resina e IPA",
            "tipo": "Tapete descartável ou lavável",
            "troca": "Quando saturado ou a cada 2-3 semanas"
        }
    },
    "primeiros_socorros": {
        "contato_pele": [
            "1. Remova luvas contaminadas imediatamente",
            "2. Lave área com água e sabão por 15 minutos",
            "3. NÃO use álcool ou solventes",
            "4. Se irritação persistir, procure médico",
            "5. Informe que é resina fotopolimerizável"
        ],
        "contato_olhos": [
            "1. Lave olhos com água corrente por 15 minutos",
            "2. Mantenha olhos abertos durante lavagem",
            "3. Procure médico IMEDIATAMENTE",
            "4. Leve ficha de segurança (FISPQ) da resina"
        ],
        "ingestao": [
            "1. NÃO induza vômito",
            "2. Beba água",
            "3. Procure médico IMEDIATAMENTE",
            "4. Leve embalagem da resina"
        ],
        "inalacao": [
            "1. Saia para área ventilada",
            "2. Respire ar fresco",
            "3. Se sintomas persistirem, procure médico"
        ]
    }
}

# ============================================================================
# MÓDULO 3: FATIADORES E TIPOS DE RESINA
# ============================================================================

FATIADORES = {
    "chitubox": {
        "nome": "Chitubox",
        "fabricante": "Chitu Systems",
        "versoes": ["Free", "Pro ($169/ano)", "Basic ($8.90/mês)"],
        "vantagens": [
            "Interface intuitiva e fácil de usar",
            "Suporta maioria das impressoras do mercado",
            "Geração automática de suportes eficiente",
            "Visualização 3D em tempo real",
            "Biblioteca de perfis de impressoras"
        ],
        "desvantagens": [
            "Versão gratuita tem limitações",
            "Suportes automáticos nem sempre ideais",
            "Pode travar com modelos muito grandes"
        ],
        "recomendado_para": "Iniciantes e usuários intermediários",
        "download": "https://www.chitubox.com"
    },
    "lychee_slicer": {
        "nome": "Lychee Slicer",
        "fabricante": "Mango 3D",
        "versoes": ["Free", "Pro ($8/mês)", "Indie ($60/ano)"],
        "vantagens": [
            "Interface moderna e bonita",
            "Algoritmo de suportes inteligente",
            "Modo 'Magic' para suportes automáticos otimizados",
            "Visualização de ilhas (áreas sem suporte)",
            "Cálculo preciso de custo e tempo"
        ],
        "desvantagens": [
            "Versão gratuita muito limitada",
            "Curva de aprendizado média",
            "Requer assinatura para recursos avançados"
        ],
        "recomendado_para": "Usuários intermediários e avançados",
        "download": "https://mango3d.io/lychee-slicer"
    },
    "prusa_slicer": {
        "nome": "PrusaSlicer (para resina)",
        "fabricante": "Prusa Research",
        "versoes": ["Free (Open Source)"],
        "vantagens": [
            "100% gratuito e open source",
            "Muito estável e confiável",
            "Suporte ativo da comunidade",
            "Perfis pré-configurados para várias impressoras"
        ],
        "desvantagens": [
            "Interface menos moderna",
            "Suportes automáticos básicos",
            "Menos recursos que concorrentes pagos"
        ],
        "recomendado_para": "Usuários que preferem software livre",
        "download": "https://www.prusa3d.com/prusaslicer"
    },
    "voxeldance_tango": {
        "nome": "VoxelDance Tango",
        "fabricante": "VoxelDance",
        "versoes": ["Free", "Pro"],
        "vantagens": [
            "Geração de suportes muito avançada",
            "Otimização automática de orientação",
            "Análise de tensões e deformações",
            "Suportes árvore (tree supports)"
        ],
        "desvantagens": [
            "Interface complexa",
            "Curva de aprendizado alta",
            "Requer PC potente"
        ],
        "recomendado_para": "Usuários profissionais e avançados",
        "download": "https://www.voxeldance.com"
    }
}

TIPOS_RESINA = {
    "resina_padrao": {
        "nome": "Resina Padrão (Standard)",
        "caracteristicas": {
            "dureza": "Média (Shore D 80-85)",
            "resistencia": "Média",
            "flexibilidade": "Baixa",
            "temperatura_max": "50-60°C"
        },
        "aplicacoes": [
            "Miniaturas e estatuetas",
            "Protótipos visuais",
            "Peças decorativas",
            "Modelos arquitetônicos"
        ],
        "vantagens": ["Mais barata", "Fácil de imprimir", "Boa resolução"],
        "desvantagens": ["Quebradiça", "Amarela com UV", "Baixa resistência mecânica"],
        "marcas_recomendadas": ["PYROBLAST (Quanton3D)", "Elegoo Standard", "Anycubic Basic"]
    },
    "resina_abs_like": {
        "nome": "Resina ABS-Like",
        "caracteristicas": {
            "dureza": "Alta (Shore D 85-88)",
            "resistencia": "Alta",
            "flexibilidade": "Baixa",
            "temperatura_max": "70-80°C"
        },
        "aplicacoes": [
            "Peças funcionais",
            "Protótipos mecânicos",
            "Encaixes e dobradiças",
            "Peças que sofrem impacto"
        ],
        "vantagens": ["Alta resistência", "Menos quebradiça", "Boa para roscas"],
        "desvantagens": ["Mais cara", "Pode deformar se mal curada"],
        "marcas_recomendadas": ["IRON 7030 (Quanton3D)", "Siraya Tech Blu", "Anycubic Tough"]
    },
    "resina_flexivel": {
        "nome": "Resina Flexível (Flexible/TPU-Like)",
        "caracteristicas": {
            "dureza": "Baixa (Shore A 60-90)",
            "resistencia": "Média",
            "flexibilidade": "Alta",
            "temperatura_max": "40-50°C"
        },
        "aplicacoes": [
            "Solas de sapato",
            "Vedações e juntas",
            "Peças que precisam dobrar",
            "Grips e empunhaduras"
        ],
        "vantagens": ["Flexível", "Absorve impactos", "Não quebra"],
        "desvantagens": ["Difícil de imprimir", "Requer suportes pesados", "Mais lenta"],
        "marcas_recomendadas": ["FLEXFORM (Quanton3D)", "Siraya Tech Tenacious", "Elegoo Flexible"]
    },
    "resina_transparente": {
        "nome": "Resina Transparente (Clear/Water Clear)",
        "caracteristicas": {
            "dureza": "Média (Shore D 80-83)",
            "resistencia": "Média",
            "transparencia": "Alta (após polimento)",
            "temperatura_max": "50-60°C"
        },
        "aplicacoes": [
            "Lentes e óptica",
            "Peças decorativas transparentes",
            "Moldes para resina epóxi",
            "Displays e vitrines"
        ],
        "vantagens": ["Transparente", "Boa resolução", "Polível"],
        "desvantagens": ["Amarela com tempo", "Layer lines visíveis", "Difícil polir perfeitamente"],
        "marcas_recomendadas": ["POSEIDON (Quanton3D)", "Siraya Tech Sculpt", "Elegoo Water Washable Clear"],
        "dicas_impressao": [
            "Use altura de camada 0.025mm para menos layer lines",
            "Aumente exposição em 10-15% para melhor transparência",
            "Cure em água para evitar amarelamento",
            "Lixe com lixas 400>800>1200>2000>3000",
            "Polimento final com pasta de polir"
        ]
    },
    "resina_dental": {
        "nome": "Resina Dental",
        "caracteristicas": {
            "dureza": "Alta (Shore D 85-90)",
            "resistencia": "Alta",
            "biocompatibilidade": "Classe I ou IIa",
            "temperatura_max": "80-100°C"
        },
        "aplicacoes": [
            "Modelos dentários",
            "Guias cirúrgicas",
            "Alinhadores ortodônticos",
            "Próteses temporárias"
        ],
        "vantagens": ["Biocompatível", "Alta precisão", "Resistente a saliva"],
        "desvantagens": ["Muito cara", "Requer certificação", "Cura específica"],
        "marcas_recomendadas": ["ATHOM Dental (Quanton3D)", "NextDent", "Formlabs Dental"],
        "cuidados_especiais": [
            "Use apenas para aplicações aprovadas",
            "Siga protocolos de esterilização",
            "Cure conforme especificações do fabricante",
            "Mantenha certificados de biocompatibilidade"
        ]
    },
    "resina_castavel": {
        "nome": "Resina Castável (Castable)",
        "caracteristicas": {
            "dureza": "Média",
            "resistencia": "Média",
            "queima_limpa": "Sim (sem resíduos)",
            "temperatura_queima": "700-800°C"
        },
        "aplicacoes": [
            "Joias (anéis, brincos, pingentes)",
            "Protótipos para fundição",
            "Peças de precisão em metal"
        ],
        "vantagens": ["Queima sem resíduos", "Alta precisão", "Acabamento liso"],
        "desvantagens": ["Muito cara", "Frágil antes da fundição", "Requer forno"],
        "marcas_recomendadas": ["ATHOM Castable (Quanton3D)", "Formlabs Castable Wax", "BlueCast X10"],
        "processo_fundicao": [
            "1. Imprima peça com suportes mínimos",
            "2. Lave com IPA 99% por 10 minutos",
            "3. Cure por 30 minutos a 60°C",
            "4. Monte em árvore de fundição",
            "5. Faça molde de gesso",
            "6. Queime em forno (rampa lenta até 700°C)",
            "7. Funda metal (ouro, prata, bronze)",
            "8. Quebre molde e finalize peça"
        ]
    }
}

# ============================================================================
# MÓDULO 4: CALIBRAÇÃO DE RESINA
# ============================================================================

CALIBRACAO_RESINA = {
    "por_que_calibrar": {
        "motivo": "Cada resina tem propriedades diferentes e requer tempos de exposição específicos",
        "fatores": [
            "Cor da resina (escuras precisam mais tempo)",
            "Tipo de resina (flexível, rígida, transparente)",
            "Potência da fonte UV da impressora",
            "Idade da fonte UV (perde potência com tempo)",
            "Temperatura ambiente (afeta viscosidade)"
        ],
        "consequencias_nao_calibrar": [
            "Subexposição: Peças frágeis, camadas se separam",
            "Superexposição: Perda de detalhes, peças inchadas, difícil remover suportes"
        ]
    },
    "teste_xp2": {
        "nome": "Teste XP2 Validation Matrix",
        "arquivo": "Disponível em grupos de impressão 3D e Thingiverse",
        "como_funciona": "Imprime 9 quadrados com tempos de exposição diferentes",
        "procedimento": [
            "1. Baixe arquivo XP2 para sua impressora",
            "2. Fatiar com tempo de exposição médio recomendado",
            "3. Imprimir teste",
            "4. Lavar com IPA por 5 minutos",
            "5. Secar completamente",
            "6. Analisar resultados SEM curar",
            "7. Escolher quadrado com melhor definição",
            "8. Usar tempo de exposição daquele quadrado"
        ],
        "interpretacao": {
            "subexposto": "Quadrado se desfaz, muito frágil, não segura",
            "ideal": "Quadrado firme, detalhes nítidos, não quebra ao dobrar levemente",
            "superexposto": "Quadrado muito rígido, detalhes borrados, difícil remover"
        }
    },
    "teste_cones_ameralabs": {
        "nome": "Teste de Cones Ameralabs",
        "arquivo": "Ameralabs Town ou Ameralabs Calibration Part",
        "como_funciona": "Imprime estruturas com detalhes finos para validar calibração",
        "procedimento": [
            "1. Baixe Ameralabs Town",
            "2. Fatiar com tempo de exposição do teste XP2",
            "3. Imprimir",
            "4. Lavar e curar normalmente",
            "5. Analisar detalhes: letras, furos, cones"
        ],
        "interpretacao": {
            "ideal": "Todas as letras legíveis, furos limpos, cones completos",
            "subexposto": "Cones quebrados, letras incompletas",
            "superexposto": "Letras borradas, furos menores que deveriam"
        }
    },
    "ajuste_fino": {
        "quando": "Após testes iniciais, para otimização",
        "parametros": {
            "tempo_exposicao": {
                "ajuste": "±0.2s por vez",
                "sintoma_baixo": "Camadas se separam, peça frágil",
                "sintoma_alto": "Perda de detalhes, elefantiase (peça inchada)"
            },
            "tempo_exposicao_base": {
                "ajuste": "±5s por vez",
                "sintoma_baixo": "Peça não gruda na plataforma",
                "sintoma_alto": "Muito difícil remover peça da plataforma"
            },
            "lift_speed": {
                "ajuste": "±10mm/min por vez",
                "sintoma_baixo": "Impressão muito lenta",
                "sintoma_alto": "Peça se solta dos suportes, falhas"
            }
        }
    },
    "tabela_referencia_rapida": {
        "resinas_quanton3d": {
            "PYROBLAST": {"exposicao": "1.8-2.2s", "base": "30-35s"},
            "IRON_7030": {"exposicao": "2.0-2.5s", "base": "35-40s"},
            "IRON": {"exposicao": "1.9-2.3s", "base": "32-37s"},
            "SPIN": {"exposicao": "1.8-2.2s", "base": "30-35s"},
            "POSEIDON": {"exposicao": "2.2-2.8s", "base": "35-45s"},
            "RPG_4K": {"exposicao": "1.7-2.1s", "base": "28-33s"},
            "SPARK": {"exposicao": "1.9-2.3s", "base": "32-37s"},
            "FLEXFORM": {"exposicao": "2.0-2.5s", "base": "35-45s"},
            "ALCHEMIST": {"exposicao": "1.8-2.2s", "base": "30-35s"},
            "LOWSMELL": {"exposicao": "2.0-2.4s", "base": "33-38s"}
        },
        "nota": "Valores são referência inicial. SEMPRE faça teste XP2 para sua impressora específica!"
    }
}

# ============================================================================
# MÓDULO 5: COMO FAZER SUPORTES
# ============================================================================

SUPORTES = {
    "por_que_usar_suportes": {
        "motivo": "Resina líquida não se sustenta sozinha - precisa de estrutura",
        "funcoes": [
            "Sustentar áreas sem apoio (overhangs)",
            "Evitar que peça se solte durante impressão",
            "Drenar resina de áreas ocas",
            "Reduzir forças de sucção no FEP"
        ]
    },
    "tipos_suportes": {
        "suporte_leve": {
            "diametro_ponta": "0.2-0.3mm",
            "diametro_corpo": "0.4-0.6mm",
            "uso": "Detalhes finos, áreas visíveis, miniaturas",
            "vantagens": ["Fácil remover", "Marca pouco"],
            "desvantagens": ["Pode quebrar", "Não suporta peso"]
        },
        "suporte_medio": {
            "diametro_ponta": "0.3-0.4mm",
            "diametro_corpo": "0.6-0.8mm",
            "uso": "Uso geral, maioria das peças",
            "vantagens": ["Equilíbrio entre força e marca"],
            "desvantagens": ["Marca moderada"]
        },
        "suporte_pesado": {
            "diametro_ponta": "0.4-0.6mm",
            "diametro_corpo": "0.8-1.2mm",
            "uso": "Peças grandes, áreas de muito peso",
            "vantagens": ["Muito forte", "Não quebra"],
            "desvantagens": ["Marca muito", "Difícil remover"]
        }
    },
    "regras_ouro": {
        "regra_45_graus": {
            "descricao": "Ângulos acima de 45° em relação à plataforma precisam de suporte",
            "exemplo": "Parede vertical (90°) = PRECISA suporte | Rampa 30° = NÃO precisa"
        },
        "regra_ilhas": {
            "descricao": "Toda área que aparece do nada (ilha) PRECISA de suporte",
            "como_identificar": "Use visualização de camadas no fatiador e procure pixels isolados"
        },
        "regra_drenagem": {
            "descricao": "Peças ocas PRECISAM de furos de drenagem",
            "tamanho_furos": "Mínimo 2mm de diâmetro",
            "quantidade": "Pelo menos 2 furos (entrada e saída de ar)"
        },
        "regra_orientacao": {
            "descricao": "Oriente peça para minimizar área de contato com FEP",
            "angulo_ideal": "15-30° em relação à plataforma",
            "motivo": "Reduz força de sucção e melhora qualidade"
        }
    },
    "tecnicas_avancadas": {
        "suportes_arvore": {
            "descricao": "Suportes que se ramificam como árvore",
            "vantagens": ["Usa menos material", "Mais fácil remover", "Menos marcas"],
            "disponivel_em": ["Lychee Slicer Pro", "VoxelDance Tango"],
            "quando_usar": "Peças orgânicas, miniaturas, esculturas"
        },
        "suportes_internos": {
            "descricao": "Suportes dentro de peças ocas",
            "quando_usar": "Peças grandes e ocas que podem colapsar",
            "cuidado": "Difícil remover - planeje antes!"
        },
        "suportes_manuais": {
            "descricao": "Adicionar suportes manualmente em pontos críticos",
            "quando_usar": "Quando automático falha ou para controle preciso",
            "dica": "Use suportes leves em áreas visíveis"
        }
    },
    "checklist_antes_imprimir": [
        "☐ Todas as ilhas têm suporte?",
        "☐ Ângulos >45° têm suporte?",
        "☐ Peça oca tem furos de drenagem?",
        "☐ Suportes não estão em áreas muito visíveis?",
        "☐ Orientação minimiza área de contato com FEP?",
        "☐ Suportes têm contato firme com peça?",
        "☐ Densidade de suportes é adequada?",
        "☐ Visualizou camada por camada?"
    ]
}

# ============================================================================
# MÓDULO 6: COMO SEPARAR MODELOS (HOLLOW/OCA)
# ============================================================================

SEPARACAO_MODELOS = {
    "por_que_ocar": {
        "economia_resina": "Peças ocas usam 50-90% menos resina",
        "reducao_tempo": "Menos camadas = impressão mais rápida",
        "reducao_peso": "Peças mais leves",
        "reducao_tensao": "Menos tensão interna = menos deformação"
    },
    "quando_ocar": {
        "recomendado": [
            "Peças grandes (>5cm em qualquer dimensão)",
            "Estátuas e bustos",
            "Vasos e recipientes",
            "Peças decorativas",
            "Protótipos não funcionais"
        ],
        "nao_recomendado": [
            "Peças pequenas (<3cm)",
            "Peças funcionais com roscas",
            "Peças que sofrerão impacto",
            "Miniaturas de jogos",
            "Peças com detalhes internos"
        ]
    },
    "como_ocar": {
        "chitubox": [
            "1. Selecione modelo",
            "2. Clique em 'Hollow' (ícone de cubo oco)",
            "3. Defina espessura da parede (2-3mm recomendado)",
            "4. Clique em 'Hollow'",
            "5. Adicione furos de drenagem (botão 'Drain Hole')",
            "6. Posicione furos na parte inferior e superior"
        ],
        "lychee": [
            "1. Selecione modelo",
            "2. Vá em 'Edit' > 'Hollow'",
            "3. Defina espessura (2-3mm)",
            "4. Ative 'Auto Drain Holes'",
            "5. Ajuste posição dos furos se necessário"
        ],
        "meshmixer": [
            "1. Importe modelo",
            "2. Edit > Hollow",
            "3. Defina offset (espessura negativa, ex: -2mm)",
            "4. Apply",
            "5. Adicione cilindros para furos de drenagem",
            "6. Boolean Difference para criar furos"
        ]
    },
    "parametros_ideais": {
        "espessura_parede": {
            "minimo": "1.5mm (muito frágil)",
            "ideal": "2-3mm (equilíbrio)",
            "maximo": "5mm (muito pesado)"
        },
        "tamanho_furos": {
            "minimo": "2mm (pode entupir)",
            "ideal": "3-4mm",
            "maximo": "6mm (pode enfraquecer)"
        },
        "quantidade_furos": {
            "minimo": "2 furos (entrada e saída)",
            "ideal": "3-4 furos para peças grandes",
            "posicionamento": "1 no ponto mais baixo + 1-2 no ponto mais alto"
        }
    },
    "drenagem_pos_impressao": {
        "procedimento": [
            "1. Remova peça da plataforma",
            "2. Lave externamente com IPA",
            "3. Encha peça com IPA pelos furos",
            "4. Agite vigorosamente por 30 segundos",
            "5. Despeje IPA pelos furos",
            "6. Repita 2-3 vezes até IPA sair limpo",
            "7. Deixe drenar completamente (pode levar horas)",
            "8. Cure normalmente"
        ],
        "dica_pro": "Use seringa com agulha longa para injetar IPA em cantos difíceis"
    },
    "problemas_comuns": {
        "resina_presa_dentro": {
            "causa": "Furos muito pequenos ou mal posicionados",
            "solucao": "Faça furos maiores (3-4mm) e em pontos opostos"
        },
        "parede_muito_fina": {
            "causa": "Espessura <1.5mm",
            "solucao": "Aumente para 2-3mm"
        },
        "colapso_interno": {
            "causa": "Peça muito grande sem suportes internos",
            "solucao": "Adicione suportes internos ou aumente espessura"
        }
    }
}

# ============================================================================
# MÓDULO 7: COMO NIVELAR IMPRESSORA
# ============================================================================

NIVELAMENTO = {
    "importancia": {
        "descricao": "Nivelamento é O FATOR MAIS CRÍTICO para adesão da primeira camada",
        "consequencias_mal_nivelado": [
            "Peça não gruda na plataforma",
            "Adesão desigual (gruda só em um lado)",
            "Primeira camada com falhas",
            "Impressão falha completamente"
        ]
    },
    "frequencia": {
        "ideal": "Antes de CADA impressão",
        "minimo": "A cada 5-10 impressões",
        "obrigatorio": [
            "Após mover impressora",
            "Após trocar plataforma",
            "Após trocar FEP",
            "Após falha de adesão"
        ]
    },
    "metodo_papel": {
        "nome": "Método do Papel A4 (Mais Comum)",
        "materiais": ["1 folha de papel A4 (75g/m²)"],
        "procedimento": [
            "1. Limpe plataforma com acetona",
            "2. Limpe FEP com IPA",
            "3. Remova tanque de resina",
            "4. Vá em Menu > Ferramentas > Nivelar/Home",
            "5. Solte parafuso de trava da plataforma",
            "6. Coloque papel A4 sobre LCD",
            "7. Abaixe plataforma até Z=0",
            "8. Papel deve ter resistência LEVE ao puxar",
            "9. Aperte parafuso de trava (sem mover plataforma)",
            "10. Teste puxando papel - deve ter resistência uniforme",
            "11. Se muito apertado: levante 0.05mm",
            "12. Se muito solto: abaixe 0.05mm",
            "13. Defina Z=0 no menu"
        ],
        "dica": "Papel deve ter resistência como se estivesse preso entre duas folhas de lixa fina"
    },
    "metodo_flint_read": {
        "nome": "Método Flint Read (Mais Preciso)",
        "materiais": ["Resina", "Luvas"],
        "procedimento": [
            "1. Limpe plataforma e FEP",
            "2. Coloque tanque de resina vazio",
            "3. Pingue 2-3 gotas de resina no centro do FEP",
            "4. Vá em Menu > Nivelar",
            "5. Abaixe plataforma lentamente até tocar na resina",
            "6. Resina deve se espalhar uniformemente",
            "7. Levante plataforma 0.1mm",
            "8. Aperte parafuso de trava",
            "9. Limpe resina do FEP e plataforma",
            "10. Defina Z=0"
        ],
        "vantagem": "Mais preciso que papel, leva em conta tensão superficial da resina"
    },
    "metodo_raft": {
        "nome": "Método do Raft de Teste",
        "quando_usar": "Para validar nivelamento após ajustar",
        "procedimento": [
            "1. Fatiar um quadrado de 50x50mm com 0.2mm de altura",
            "2. Imprimir apenas a primeira camada",
            "3. Cancelar impressão após 1ª camada",
            "4. Remover e analisar",
            "5. Camada deve ser uniforme em toda área",
            "6. Se um lado mais fino: plataforma desnivelada",
            "7. Ajustar e repetir"
        ]
    },
    "ajuste_fino": {
        "problema_comum": "Um lado da plataforma mais alto que outro",
        "solucao_elegoo_mars": [
            "1. Solte completamente parafuso de trava",
            "2. Coloque papel em 4 cantos da plataforma",
            "3. Abaixe plataforma até Z=0",
            "4. Teste resistência em cada canto",
            "5. Se desigual: bata LEVEMENTE no lado mais alto",
            "6. Repita até todos cantos iguais",
            "7. Aperte parafuso de trava"
        ],
        "solucao_anycubic_photon": [
            "1. Algumas impressoras têm parafusos de ajuste nos cantos",
            "2. Aperte parafuso do lado mais baixo",
            "3. Ou solte parafuso do lado mais alto",
            "4. Ajuste 1/4 de volta por vez",
            "5. Teste com papel novamente"
        ]
    },
    "problemas_comuns": {
        "plataforma_muito_alta": {
            "sintoma": "Papel passa solto, sem resistência",
            "solucao": "Abaixe plataforma 0.05mm por vez até resistência ideal"
        },
        "plataforma_muito_baixa": {
            "sintoma": "Papel não sai, muito apertado ou rasga",
            "solucao": "Levante plataforma 0.05mm por vez"
        },
        "desnivelamento_lateral": {
            "sintoma": "Um lado gruda, outro não",
            "solucao": "Ajuste parafusos de nivelamento ou bata levemente no lado alto"
        },
        "plataforma_solta": {
            "sintoma": "Plataforma se move durante impressão",
            "solucao": "Aperte parafuso de trava com mais força (cuidado para não mover)"
        }
    }
}

# ============================================================================
# MÓDULO 8: COMO COLOCAR PARA IMPRIMIR
# ============================================================================

PROCESSO_IMPRESSAO = {
    "preparacao_pre_impressao": {
        "limpeza": [
            "1. Limpe plataforma com acetona (remove óleos e resina antiga)",
            "2. Limpe FEP com IPA 99% (remove resina curada)",
            "3. Seque completamente com papel toalha",
            "4. Verifique se FEP está sem rasgos ou opacidade"
        ],
        "nivelamento": [
            "1. Nivele plataforma (método do papel ou Flint Read)",
            "2. Valide em todos os cantos",
            "3. Defina Z=0"
        ],
        "resina": [
            "1. Agite frasco de resina por 2 minutos (pigmentos se depositam)",
            "2. Verifique temperatura (ideal 25-30°C)",
            "3. Se fria, aqueça em banho-maria morno (NÃO micro-ondas!)",
            "4. Despeje resina no tanque (não encha mais que 2/3)",
            "5. Filtre resina se tiver partículas (use filtro de café ou malha fina)"
        ]
    },
    "fatiamento": {
        "configuracoes_basicas": [
            "1. Importe modelo no fatiador",
            "2. Oriente peça (15-30° ideal)",
            "3. Adicione suportes (automático + manual se necessário)",
            "4. Oca se necessário (peças grandes)",
            "5. Configure parâmetros de impressão"
        ],
        "parametros_criticos": {
            "altura_camada": "0.05mm (padrão) | 0.025mm (alta qualidade) | 0.1mm (rascunho)",
            "tempo_exposicao": "Use valor do teste XP2 ou planilha Quanton3D",
            "tempo_exposicao_base": "10-15x o tempo normal (ex: se normal é 2.5s, base é 30-35s)",
            "camadas_base": "5-8 camadas (mais = melhor adesão, mas mais difícil remover)",
            "lift_distance": "6-8mm (padrão) | 10mm (peças grandes)",
            "lift_speed": "60-80mm/min (padrão) | 40mm/min (resinas flexíveis)",
            "retract_speed": "120-150mm/min",
            "light_off_delay": "0-1s (LCD) | 2-3s (DLP)"
        },
        "exportacao": [
            "1. Fatiar (slice)",
            "2. Verificar tempo estimado e volume de resina",
            "3. Exportar para pendrive (.ctb, .cbddlp, .photon, etc.)",
            "4. Ejetar pendrive com segurança"
        ]
    },
    "iniciando_impressao": {
        "procedimento": [
            "1. Insira pendrive na impressora",
            "2. Selecione arquivo no menu",
            "3. Verifique informações (tempo, camadas, altura)",
            "4. Confirme início",
            "5. Impressora fará home (plataforma sobe)",
            "6. Plataforma desce até tanque",
            "7. Primeiras camadas (base) são expostas",
            "8. Impressão continua automaticamente"
        ],
        "acompanhamento": [
            "1. Assista primeiras 10-15 camadas",
            "2. Verifique se peça está grudando na plataforma",
            "3. Se não grudar até camada 10: CANCELE e nivele novamente",
            "4. Se grudar: pode deixar imprimir sozinha",
            "5. Monitore a cada 30-60min (opcional)"
        ]
    },
    "durante_impressao": {
        "o_que_observar": [
            "Som de 'pop' ao levantar plataforma (normal - sucção do FEP)",
            "Resina deve fluir de volta ao tanque entre camadas",
            "Plataforma sobe e desce suavemente",
            "LCD acende e apaga a cada camada"
        ],
        "sinais_problema": [
            "Som muito alto de 'pop' (sucção excessiva - reduza área de contato)",
            "Plataforma trava ou faz barulho estranho (problema mecânico)",
            "Peça se solta da plataforma (nivelamento ruim ou exposição baixa)",
            "Resina não flui de volta (muito viscosa - aqueça ambiente)"
        ]
    },
    "finalizacao": {
        "remocao_peca": [
            "1. ESPERE impressora finalizar e plataforma subir",
            "2. Remova tanque de resina",
            "3. Coloque bandeja embaixo da plataforma",
            "4. Use espátula de metal para soltar peça",
            "5. Insira espátula entre peça e plataforma",
            "6. Faça movimento de alavanca (cuidado para não dobrar plataforma)",
            "7. Peça deve soltar de uma vez",
            "8. Se muito difícil: deixe plataforma de molho em IPA por 5min"
        ],
        "limpeza_pos_impressao": [
            "1. Filtre resina do tanque de volta ao frasco",
            "2. Limpe tanque com papel toalha",
            "3. Limpe FEP com IPA",
            "4. Limpe plataforma com IPA",
            "5. Seque tudo",
            "6. Guarde resina em local escuro"
        ]
    }
}

# ============================================================================
# MÓDULO 9: LAVAGEM E CURA
# ============================================================================

LAVAGEM_CURA = {
    "lavagem": {
        "por_que_lavar": "Remover resina não curada da superfície da peça",
        "liquidos": {
            "ipa_99": {
                "nome": "Álcool Isopropílico 99%",
                "vantagens": ["Mais eficiente", "Evapora rápido", "Não deixa resíduos"],
                "desvantagens": ["Mais caro", "Inflamável"],
                "onde_comprar": "Farmácias de manipulação, lojas de química"
            },
            "ipa_70": {
                "nome": "Álcool Isopropílico 70%",
                "vantagens": ["Mais barato", "Fácil encontrar"],
                "desvantagens": ["Menos eficiente", "Demora mais para secar"],
                "onde_comprar": "Farmácias comuns"
            },
            "alcool_etilico": {
                "nome": "Álcool Etílico 92-96%",
                "vantagens": ["Alternativa ao IPA", "Mais barato"],
                "desvantagens": ["Menos eficiente que IPA 99%"],
                "onde_comprar": "Supermercados, farmácias"
            },
            "mean_green": {
                "nome": "Mean Green (ou similar)",
                "vantagens": ["Não inflamável", "Reutilizável por muito tempo"],
                "desvantagens": ["Mais caro inicialmente", "Precisa água depois"],
                "onde_comprar": "Importação ou lojas especializadas"
            }
        },
        "metodos": {
            "lavagem_manual": {
                "procedimento": [
                    "1. Use 2 recipientes com IPA (sujo e limpo)",
                    "2. Mergulhe peça no IPA sujo por 2-3 minutos",
                    "3. Agite suavemente ou use escova macia",
                    "4. Transfira para IPA limpo",
                    "5. Agite por mais 2-3 minutos",
                    "6. Remova e deixe secar ao ar por 10-15 minutos"
                ],
                "dica": "Use escova de dentes macia para detalhes difíceis"
            },
            "lavadora_ultrassonica": {
                "procedimento": [
                    "1. Coloque peça em cesto",
                    "2. Encha com IPA até cobrir peça",
                    "3. Ligue por 3-5 minutos",
                    "4. Remova e seque"
                ],
                "vantagens": ["Limpa detalhes minúsculos", "Mais eficiente"],
                "desvantagens": ["Equipamento caro"],
                "recomendacao": "Ultrasonic Cleaner 3L (R$ 200-400)"
            },
            "lavadora_automatica": {
                "modelos": ["Anycubic Wash & Cure", "Elegoo Mercury Plus", "Creality UW-02"],
                "procedimento": [
                    "1. Coloque peça na cesta",
                    "2. Selecione tempo (3-5 min)",
                    "3. Máquina agita automaticamente",
                    "4. Remova e seque"
                ],
                "vantagens": ["Automático", "Consistente", "Menos bagunça"],
                "desvantagens": ["Equipamento caro (R$ 400-800)"]
            }
        },
        "tempo_lavagem": {
            "minimo": "3 minutos (peças pequenas)",
            "ideal": "5-7 minutos (peças médias)",
            "maximo": "10 minutos (peças grandes ou muito detalhadas)"
        },
        "troca_ipa": {
            "frequencia": "Quando IPA ficar muito turvo (cor de leite)",
            "reutilizacao": [
                "1. Deixe IPA sujo em recipiente fechado por 1 semana",
                "2. Resina se deposita no fundo",
                "3. Despeje IPA limpo em outro recipiente",
                "4. Resina depositada pode ser curada e descartada"
            ]
        }
    },
    "secagem": {
        "importancia": "IPA residual interfere na cura e pode deixar peça pegajosa",
        "metodos": {
            "ar_natural": {
                "tempo": "10-15 minutos",
                "procedimento": "Deixe peça em local ventilado"
            },
            "ar_comprimido": {
                "tempo": "2-3 minutos",
                "procedimento": "Sopre ar comprimido em toda superfície",
                "cuidado": "Não use pressão muito alta (pode quebrar detalhes)"
            },
            "secador_cabelo": {
                "tempo": "3-5 minutos",
                "procedimento": "Use ar frio ou morno (NÃO quente)",
                "cuidado": "Ar quente pode deformar peça"
            }
        }
    },
    "cura": {
        "por_que_curar": "Finalizar polimerização da resina, aumentando resistência mecânica",
        "metodos": {
            "sol": {
                "tempo": "15-30 minutos (depende da intensidade)",
                "procedimento": [
                    "1. Coloque peça em recipiente com água",
                    "2. Exponha ao sol direto",
                    "3. Vire peça a cada 5 minutos para cura uniforme"
                ],
                "vantagens": ["Grátis", "Simples"],
                "desvantagens": ["Depende do clima", "Pode amarelar peça", "Não uniforme"],
                "dica": "Água evita superaquecimento e amarelamento"
            },
            "caixa_uv_caseira": {
                "materiais": [
                    "Caixa de papelão ou madeira",
                    "Papel alumínio (forrar interior)",
                    "Fita LED UV 405nm (5-10 metros)",
                    "Prato giratório (opcional)"
                ],
                "procedimento": [
                    "1. Forre interior da caixa com alumínio",
                    "2. Cole fitas LED nas laterais e topo",
                    "3. Coloque peça no centro (use prato giratório)",
                    "4. Ligue por 5-10 minutos",
                    "5. Vire peça e repita"
                ],
                "custo": "R$ 50-150",
                "vantagens": ["Barato", "Eficiente", "Controlável"]
            },
            "caixa_uv_comercial": {
                "modelos": ["Anycubic Wash & Cure", "Elegoo Mercury Plus", "Creality UW-02"],
                "procedimento": [
                    "1. Coloque peça na plataforma giratória",
                    "2. Selecione tempo (3-10 min dependendo da resina)",
                    "3. Máquina cura uniformemente",
                    "4. Remova peça"
                ],
                "custo": "R$ 400-800",
                "vantagens": ["Automático", "Uniforme", "Consistente", "Integrado com lavadora"]
            },
            "lampada_uv_unha": {
                "tipo": "Lâmpada UV para unhas (36-48W)",
                "procedimento": [
                    "1. Coloque peça dentro da lâmpada",
                    "2. Ligue por 5-10 minutos",
                    "3. Vire peça e repita"
                ],
                "custo": "R$ 50-150",
                "vantagens": ["Barato", "Fácil encontrar"],
                "desvantagens": ["Espaço limitado", "Cura não uniforme"]
            }
        },
        "tempo_cura": {
            "resina_padrao": "5-10 minutos",
            "resina_abs_like": "10-15 minutos",
            "resina_flexivel": "5-8 minutos (cuidado para não endurecer demais)",
            "resina_transparente": "3-5 minutos em água (evita amarelamento)",
            "resina_dental": "Seguir especificações do fabricante (geralmente 10-20 min)"
        },
        "sinais_cura_correta": [
            "Superfície não pegajosa ao toque",
            "Peça firme e resistente",
            "Sem cheiro forte de resina",
            "Cor uniforme"
        ],
        "sinais_subcura": [
            "Superfície pegajosa",
            "Peça flexível demais",
            "Cheiro forte de resina",
            "Quebra facilmente"
        ],
        "sinais_supercura": [
            "Peça amarelada (especialmente transparentes)",
            "Superfície áspera ou rachada",
            "Peça muito quebradiça",
            "Deformação (empenamento)"
        ]
    },
    "pos_cura": {
        "remocao_suportes": [
            "1. Remova suportes ANTES de curar (mais fácil)",
            "2. Use alicate de corte fino",
            "3. Corte rente à peça",
            "4. Lixe marcas com lixa 400-600",
            "5. Cure novamente por 2-3 minutos"
        ],
        "polimento": [
            "1. Lixe com lixas progressivas: 400 > 600 > 800 > 1200",
            "2. Use água durante lixamento (wet sanding)",
            "3. Seque e cure por 2-3 minutos",
            "4. Para acabamento espelho: 2000 > 3000 > pasta de polir"
        ]
    }
}

# ============================================================================
# MÓDULO 10: CUIDADOS PÓS-IMPRESSÃO
# ============================================================================

CUIDADOS_POS_IMPRESSAO = {
    "armazenamento_pecas": {
        "local": "Local seco, fresco e escuro",
        "temperatura": "15-25°C (evite calor excessivo)",
        "luz": "Proteja de luz solar direta (pode amarelar e enfraquecer)",
        "umidade": "Baixa umidade (resina absorve umidade e pode enfraquecer)",
        "dica": "Guarde em caixas opacas ou armários fechados"
    },
    "pintura": {
        "preparacao": [
            "1. Lave e cure completamente",
            "2. Lixe levemente com lixa 400 (cria textura para tinta aderir)",
            "3. Limpe pó com pano úmido",
            "4. Aplique primer (opcional mas recomendado)"
        ],
        "tintas_recomendadas": {
            "acrilica": "Tinta acrílica para modelismo (Vallejo, Citadel, Tamiya)",
            "spray": "Tinta spray para plástico",
            "esmalte": "Tinta esmalte sintético (mais resistente)"
        },
        "tecnica": [
            "1. Aplique camadas finas (melhor 3 camadas finas que 1 grossa)",
            "2. Deixe secar entre camadas (30-60 min)",
            "3. Finalize com verniz (fosco, semi-brilho ou brilhante)"
        ]
    },
    "colagem": {
        "colas_recomendadas": {
            "cianoacrilato": "Super Bonder (uso geral, cura rápida)",
            "epoxi_5min": "Epóxi de 5 minutos (mais resistente)",
            "epoxi_24h": "Epóxi de 24 horas (máxima resistência)",
            "uv": "Cola UV (cura com luz UV, ideal para transparentes)"
        },
        "tecnica": [
            "1. Lixe superfícies a serem coladas (lixa 400)",
            "2. Limpe com IPA",
            "3. Aplique cola em ambas superfícies",
            "4. Pressione firmemente por 30-60 segundos",
            "5. Deixe curar completamente antes de manusear"
        ]
    },
    "reparo": {
        "preenchimento_falhas": {
            "materiais": ["Massa epóxi", "Resina líquida + UV", "Putty (massa de modelismo)"],
            "procedimento": [
                "1. Limpe área com IPA",
                "2. Aplique material de preenchimento",
                "3. Modele com espátula ou dedo molhado",
                "4. Deixe curar",
                "5. Lixe até ficar liso",
                "6. Pinte se necessário"
            ]
        },
        "colagem_quebras": {
            "procedimento": [
                "1. Limpe superfícies quebradas",
                "2. Teste encaixe antes de colar",
                "3. Aplique cola cianoacrilato ou epóxi",
                "4. Pressione firmemente",
                "5. Limpe excesso de cola",
                "6. Deixe curar 24h antes de manusear"
            ]
        }
    },
    "manutencao_impressora": {
        "diaria": [
            "Limpar plataforma com IPA",
            "Limpar FEP com IPA",
            "Verificar nível de resina no tanque"
        ],
        "semanal": [
            "Verificar tensão do FEP (deve soar como tambor)",
            "Limpar tela LCD com pano de microfibra",
            "Verificar aperto de parafusos"
        ],
        "mensal": [
            "Lubrificar fuso do eixo Z com graxa PTFE",
            "Verificar folgas nas guias lineares",
            "Limpar filtro de ar (se houver)",
            "Verificar integridade do FEP (trocar se opaco ou rasgado)"
        ],
        "anual": [
            "Substituir FEP preventivamente",
            "Verificar potência da fonte UV (pode precisar trocar LCD)",
            "Limpeza geral da impressora",
            "Atualizar firmware se houver atualizações"
        ]
    },
    "descarte": {
        "resina_liquida": {
            "procedimento": [
                "1. NÃO jogue no ralo ou lixo comum",
                "2. Cure resina completamente ao sol ou UV",
                "3. Resina curada é plástico inerte",
                "4. Descarte como plástico comum"
            ]
        },
        "ipa_contaminado": {
            "procedimento": [
                "1. Deixe IPA em recipiente fechado por 1 semana",
                "2. Resina se deposita no fundo",
                "3. Despeje IPA limpo para reutilizar",
                "4. Cure resina depositada ao sol",
                "5. Descarte resina curada como plástico",
                "6. IPA pode ser despejado no ralo (diluído em água)"
            ]
        },
        "luvas_papel": {
            "procedimento": [
                "1. Cure resina residual nas luvas ao sol",
                "2. Descarte como lixo comum"
            ]
        },
        "pecas_falhadas": {
            "procedimento": [
                "1. Lave com IPA para remover resina não curada",
                "2. Cure completamente",
                "3. Descarte como plástico comum ou recicle"
            ]
        }
    }
}

# ============================================================================
# MÓDULO 11: POLIMENTO E REMOÇÃO DE SUPORTES
# ============================================================================

POLIMENTO_REMOCAO = {
    "remocao_suportes": {
        "quando_remover": {
            "antes_cura": {
                "vantagens": ["Mais fácil cortar", "Menos força necessária"],
                "desvantagens": ["Peça mais frágil", "Pode quebrar"],
                "recomendado_para": "Peças robustas, suportes leves"
            },
            "depois_cura": {
                "vantagens": ["Peça mais resistente", "Menos risco de quebrar"],
                "desvantagens": ["Mais difícil cortar", "Pode deixar marcas maiores"],
                "recomendado_para": "Peças delicadas, suportes pesados"
            }
        },
        "ferramentas": {
            "alicate_corte": "Alicate de corte fino (modelo para eletrônica)",
            "estilete": "Estilete afiado ou X-Acto knife",
            "lixa": "Lixas 400, 600, 800, 1200",
            "lima": "Lima de joalheiro (para detalhes)",
            "dremel": "Micro retífica com broca de corte (opcional)"
        },
        "tecnica": [
            "1. Identifique todos os pontos de suporte",
            "2. Corte suportes maiores com alicate rente à peça",
            "3. Remova tocos restantes com estilete",
            "4. Lixe marcas com lixa 400 (movimentos circulares)",
            "5. Progrida para lixas mais finas: 600 > 800 > 1200",
            "6. Use água durante lixamento (wet sanding)",
            "7. Seque e cure novamente por 2-3 minutos"
        ],
        "dicas_pro": [
            "Use lupa ou óculos de aumento para detalhes minúsculos",
            "Aqueça suportes com secador de cabelo (ficam mais maleáveis)",
            "Corte em ângulo de 45° para facilitar lixamento",
            "Não force - se muito difícil, cure mais e tente novamente"
        ]
    },
    "polimento": {
        "niveis": {
            "basico": {
                "objetivo": "Remover layer lines e marcas visíveis",
                "lixas": "400 > 600 > 800",
                "tempo": "10-20 minutos",
                "resultado": "Superfície lisa ao toque"
            },
            "intermediario": {
                "objetivo": "Acabamento semi-brilhante",
                "lixas": "400 > 600 > 800 > 1200 > 2000",
                "tempo": "30-60 minutos",
                "resultado": "Superfície brilhante, layer lines quase invisíveis"
            },
            "avancado": {
                "objetivo": "Acabamento espelho",
                "lixas": "400 > 600 > 800 > 1200 > 2000 > 3000 > pasta de polir",
                "tempo": "1-3 horas",
                "resultado": "Superfície reflexiva como espelho"
            }
        },
        "tecnica_wet_sanding": {
            "procedimento": [
                "1. Molhe lixa e peça em água",
                "2. Lixe com movimentos circulares suaves",
                "3. Enxágue frequentemente para ver progresso",
                "4. Não pressione muito (deixe lixa fazer o trabalho)",
                "5. Progrida para lixa mais fina quando superfície estiver uniforme",
                "6. Seque completamente antes de próxima etapa"
            ],
            "vantagens": [
                "Menos pó (mais saudável)",
                "Lixa dura mais",
                "Acabamento mais uniforme",
                "Menos calor (não derrete resina)"
            ]
        },
        "polimento_quimico": {
            "metodo_vapor_ipa": {
                "procedimento": [
                    "1. Aqueça IPA 99% em banho-maria (NÃO chama direta!)",
                    "2. Suspenda peça sobre vapor por 10-30 segundos",
                    "3. Vapor derrete camada superficial",
                    "4. Deixe secar ao ar",
                    "5. Cure por 2-3 minutos"
                ],
                "resultado": "Superfície brilhante, layer lines suavizadas",
                "cuidados": [
                    "IPA é INFLAMÁVEL - use banho-maria",
                    "Faça em ambiente ventilado",
                    "Use luvas e óculos",
                    "Não deixe muito tempo (pode derreter detalhes)"
                ]
            },
            "metodo_resina_liquida": {
                "procedimento": [
                    "1. Pincele camada fina de resina na peça",
                    "2. Cure por 1-2 minutos",
                    "3. Repita se necessário"
                ],
                "resultado": "Preenche layer lines, acabamento brilhante",
                "cuidados": "Pode perder detalhes finos"
            }
        },
        "polimento_mecanico": {
            "pasta_polir": {
                "tipos": ["Pasta de polir para plástico", "Pasta de polir para joias", "Compound automotivo"],
                "procedimento": [
                    "1. Aplique pasta em pano macio",
                    "2. Esfregue em movimentos circulares",
                    "3. Limpe resíduo com pano limpo",
                    "4. Repita até brilho desejado"
                ]
            },
            "politriz": {
                "ferramenta": "Politriz rotativa ou Dremel com disco de feltro",
                "procedimento": [
                    "1. Aplique pasta de polir no disco",
                    "2. Ligue em velocidade baixa-média",
                    "3. Passe levemente sobre superfície",
                    "4. Não pressione muito (pode derreter resina)",
                    "5. Limpe resíduo"
                ],
                "cuidado": "Pode gerar calor e deformar peça - use baixa velocidade"
            }
        }
    },
    "acabamentos_especiais": {
        "texturizacao": {
            "lixa_grossa": "Use lixa 200-400 para criar textura áspera",
            "jateamento": "Jateamento com areia cria textura uniforme fosca",
            "estampagem": "Pressione objeto texturizado em resina mole (antes de curar)"
        },
        "pintura_primer": {
            "procedimento": [
                "1. Lixe com 400-600",
                "2. Limpe com IPA",
                "3. Aplique primer spray (2-3 camadas finas)",
                "4. Lixe levemente com 800-1000",
                "5. Aplique tinta final"
            ],
            "vantagem": "Esconde layer lines e imperfeições"
        },
        "revestimento_epoxi": {
            "procedimento": [
                "1. Prepare resina epóxi (proporção correta)",
                "2. Pincele ou despeje sobre peça",
                "3. Use soprador térmico para remover bolhas",
                "4. Deixe curar 24h"
            ],
            "resultado": "Acabamento brilhante tipo vidro, esconde layer lines"
        }
    }
}

# ============================================================================
# MÓDULO 13: SUGESTÕES DE INVESTIMENTOS
# ============================================================================

INVESTIMENTOS = {
    "nivel_iniciante": {
        "impressora": {
            "opcoes": [
                {"modelo": "Elegoo Mars 3", "preco": "R$ 1.200-1.500", "resolucao": "4K"},
                {"modelo": "Anycubic Photon Mono 4K", "preco": "R$ 1.300-1.600", "resolucao": "4K"},
                {"modelo": "Creality Halot One", "preco": "R$ 1.100-1.400", "resolucao": "2K"}
            ],
            "recomendacao": "Elegoo Mars 3 (melhor custo-benefício)"
        },
        "acessorios_essenciais": [
            {"item": "Resina 1kg (Quanton3D PYROBLAST)", "preco": "R$ 150-200"},
            {"item": "Álcool Isopropílico 99% (5L)", "preco": "R$ 100-150"},
            {"item": "Luvas nitrilo (caixa 100un)", "preco": "R$ 30-50"},
            {"item": "Espátulas metal", "preco": "R$ 20-40"},
            {"item": "Recipientes para lavagem (2un)", "preco": "R$ 30-60"},
            {"item": "Papel toalha", "preco": "R$ 10-20"},
            {"item": "Filtros para resina (100un)", "preco": "R$ 20-40"}
        ],
        "total_estimado": "R$ 1.600-2.200"
    },
    "nivel_intermediario": {
        "upgrades": [
            {"item": "Lavadora e Curadora UV (Elegoo Mercury Plus)", "preco": "R$ 600-900", "beneficio": "Automação de lavagem e cura"},
            {"item": "Resinas especiais (ABS-Like, Flexível)", "preco": "R$ 200-300/kg", "beneficio": "Mais opções de aplicação"},
            {"item": "FEP extra (5 folhas)", "preco": "R$ 100-150", "beneficio": "Reposição preventiva"},
            {"item": "Lavadora ultrassônica 3L", "preco": "R$ 200-400", "beneficio": "Limpeza profunda"},
            {"item": "Lixas sortidas (pack)", "preco": "R$ 50-100", "beneficio": "Polimento profissional"}
        ],
        "total_adicional": "R$ 1.150-1.850"
    },
    "nivel_avancado": {
        "upgrades": [
            {"item": "Impressora maior (Elegoo Saturn 2)", "preco": "R$ 2.500-3.500", "beneficio": "Peças maiores (8.9 polegadas)"},
            {"item": "Resinas profissionais (Dental, Castável)", "preco": "R$ 400-800/kg", "beneficio": "Aplicações profissionais"},
            {"item": "Sistema de ventilação/exaustor", "preco": "R$ 300-600", "beneficio": "Ambiente mais seguro"},
            {"item": "Estação de trabalho completa", "preco": "R$ 500-1.000", "beneficio": "Organização e produtividade"},
            {"item": "Politriz/Dremel profissional", "preco": "R$ 300-800", "beneficio": "Acabamento profissional"}
        ],
        "total_adicional": "R$ 4.000-6.700"
    },
    "consumiveis_mensais": {
        "uso_hobby": [
            {"item": "Resina (1-2kg/mês)", "preco": "R$ 150-400"},
            {"item": "IPA (2-3L/mês)", "preco": "R$ 40-90"},
            {"item": "Luvas (50un/mês)", "preco": "R$ 15-25"},
            {"item": "FEP (1 troca a cada 2-3 meses)", "preco": "R$ 20-30"}
        ],
        "total_mensal": "R$ 225-545"
    },
    "dicas_economia": [
        "Compre resina em quantidade (5kg+) para desconto",
        "Reutilize IPA deixando resina decantar",
        "Oque peças grandes para economizar resina",
        "Compre FEP em rolo (mais barato que folhas)",
        "Faça sua própria caixa de cura UV (R$ 50 vs R$ 600)",
        "Compre luvas em atacado (caixas de 500un)",
        "Use álcool etílico 96% como alternativa ao IPA"
    ]
}

# ============================================================================
# MÓDULO 14: MARCAS CONFIÁVEIS
# ============================================================================

MARCAS_CONFIAVEIS = {
    "impressoras": {
        "elegoo": {
            "pais": "China",
            "reputacao": "Excelente",
            "modelos_destaque": [
                "Mars 3 (4K, R$ 1.200-1.500)",
                "Mars 3 Pro (4K, R$ 1.500-1.800)",
                "Saturn 2 (8K, R$ 2.500-3.500)"
            ],
            "vantagens": ["Melhor custo-benefício", "Suporte ativo", "Comunidade grande"],
            "desvantagens": ["Importação (pode ter taxas)"],
            "onde_comprar": ["Amazon", "AliExpress", "Mercado Livre"]
        },
        "anycubic": {
            "pais": "China",
            "reputacao": "Excelente",
            "modelos_destaque": [
                "Photon Mono 4K (R$ 1.300-1.600)",
                "Photon Mono X (R$ 2.000-2.500)",
                "Photon M3 Plus (R$ 2.800-3.500)"
            ],
            "vantagens": ["Qualidade construção", "Firmware estável", "Boa resolução"],
            "desvantagens": ["Preço um pouco mais alto"],
            "onde_comprar": ["Amazon", "Site oficial", "Mercado Livre"]
        },
        "creality": {
            "pais": "China",
            "reputacao": "Boa",
            "modelos_destaque": [
                "Halot One (2K, R$ 1.100-1.400)",
                "Halot Mage (8K, R$ 2.200-2.800)"
            ],
            "vantagens": ["Marca conhecida", "Preço acessível"],
            "desvantagens": ["Suporte menos ativo que Elegoo/Anycubic"],
            "onde_comprar": ["Amazon", "AliExpress", "Mercado Livre"]
        },
        "phrozen": {
            "pais": "Taiwan",
            "reputacao": "Premium",
            "modelos_destaque": [
                "Sonic Mini 8K (R$ 2.500-3.200)",
                "Sonic Mega 8K (R$ 4.500-5.500)"
            ],
            "vantagens": ["Altíssima qualidade", "Resolução excepcional", "Suporte premium"],
            "desvantagens": ["Preço alto"],
            "onde_comprar": ["Site oficial", "Amazon"]
        }
    },
    "resinas_brasil": {
        "quanton3d": {
            "pais": "Brasil",
            "reputacao": "Excelente (Nacional)",
            "modelos_destaque": [
                "PYROBLAST (Padrão, R$ 150-200/kg)",
                "IRON 7030 (ABS-Like, R$ 180-230/kg)",
                "FLEXFORM (Flexível, R$ 200-280/kg)",
                "POSEIDON (Transparente, R$ 180-230/kg)"
            ],
            "vantagens": [
                "Produção nacional (sem taxas)",
                "Suporte em português",
                "Entrega rápida",
                "Qualidade comprovada",
                "Preço competitivo"
            ],
            "onde_comprar": ["Site oficial Quanton3D", "Revendedores autorizados"],
            "nota": "MARCA RECOMENDADA PARA BRASIL - Melhor custo-benefício nacional"
        }
    },
    "resinas_importadas": {
        "siraya_tech": {
            "pais": "EUA",
            "reputacao": "Premium",
            "modelos_destaque": [
                "Fast (Padrão rápida, $30-40/kg)",
                "Blu (ABS-Like, $35-45/kg)",
                "Tenacious (Flexível, $40-50/kg)",
                "Sculpt (Transparente, $35-45/kg)"
            ],
            "vantagens": ["Qualidade excepcional", "Comunidade grande"],
            "desvantagens": ["Importação cara", "Taxas alfandegárias"],
            "onde_comprar": ["Amazon US", "Site oficial"]
        },
        "elegoo": {
            "pais": "China",
            "reputacao": "Boa",
            "modelos_destaque": [
                "Standard (R$ 120-180/kg)",
                "ABS-Like (R$ 150-220/kg)",
                "Water Washable (R$ 140-200/kg)"
            ],
            "vantagens": ["Preço acessível", "Fácil encontrar"],
            "desvantagens": ["Qualidade média"],
            "onde_comprar": ["Amazon", "AliExpress", "Mercado Livre"]
        },
        "anycubic": {
            "pais": "China",
            "reputacao": "Boa",
            "modelos_destaque": [
                "Basic (R$ 130-190/kg)",
                "Tough (R$ 160-230/kg)",
                "Plant-Based (R$ 140-200/kg)"
            ],
            "vantagens": ["Compatibilidade garantida com impressoras Anycubic"],
            "desvantagens": ["Preço um pouco alto"],
            "onde_comprar": ["Amazon", "Site oficial", "Mercado Livre"]
        }
    },
    "acessorios": {
        "fep": {
            "marcas": ["Elegoo", "Anycubic", "EPAX", "Genérico"],
            "preco": "R$ 20-40/folha | R$ 100-200/rolo",
            "dica": "Compre rolo (mais econômico) ou específico da sua impressora"
        },
        "ipa": {
            "marcas": ["Farmax", "Rioquímica", "Synth"],
            "preco": "R$ 20-30/L (99%) | R$ 80-120/5L",
            "dica": "Compre em farmácias de manipulação (mais barato em quantidade)"
        },
        "luvas": {
            "marcas": ["Descarpack", "Supermax", "Genérico"],
            "preco": "R$ 30-50/100un | R$ 120-200/500un",
            "dica": "Compre em atacado (caixas de 500un) para economizar"
        }
    },
    "onde_comprar_brasil": {
        "lojas_online": [
            {"nome": "Quanton3D", "tipo": "Resinas nacionais", "site": "quanton3d.com.br"},
            {"nome": "3D Lab", "tipo": "Impressoras e resinas", "site": "3dlab.com.br"},
            {"nome": "GTMax3D", "tipo": "Impressoras e acessórios", "site": "gtmax3d.com.br"},
            {"nome": "Mercado Livre", "tipo": "Geral", "site": "mercadolivre.com.br"},
            {"nome": "Amazon Brasil", "tipo": "Geral", "site": "amazon.com.br"}
        ],
        "grupos_comunidade": [
            "Impressão 3D Brasil (Facebook)",
            "Impressão 3D Resina Brasil (Facebook)",
            "r/impressao3d (Reddit)",
            "Grupos de WhatsApp regionais"
        ]
    }
}

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def buscar_informacao_guia(modulo, topico=None):
    """
    Busca informação específica no guia completo
    
    Args:
        modulo: Nome do módulo (ex: "partes_impressora", "seguranca", etc.)
        topico: Tópico específico dentro do módulo (opcional)
    
    Returns:
        Informação solicitada ou mensagem de erro
    """
    modulos_disponiveis = {
        "partes_impressora": PARTES_IMPRESSORA,
        "seguranca": EQUIPAMENTOS_SEGURANCA,
        "fatiadores": FATIADORES,
        "tipos_resina": TIPOS_RESINA,
        "calibracao": CALIBRACAO_RESINA,
        "suportes": SUPORTES,
        "separacao": SEPARACAO_MODELOS,
        "nivelamento": NIVELAMENTO,
        "impressao": PROCESSO_IMPRESSAO,
        "lavagem_cura": LAVAGEM_CURA,
        "pos_impressao": CUIDADOS_POS_IMPRESSAO,
        "polimento": POLIMENTO_REMOCAO,
        "investimentos": INVESTIMENTOS,
        "marcas": MARCAS_CONFIAVEIS
    }
    
    if modulo not in modulos_disponiveis:
        return f"Módulo '{modulo}' não encontrado. Módulos disponíveis: {', '.join(modulos_disponiveis.keys())}"
    
    dados = modulos_disponiveis[modulo]
    
    if topico:
        if topico in dados:
            return dados[topico]
        else:
            return f"Tópico '{topico}' não encontrado no módulo '{modulo}'"
    
    return dados

def listar_modulos_disponiveis():
    """Retorna lista de todos os módulos disponíveis no guia"""
    return [
        "1. partes_impressora - Componentes da impressora 3D de resina",
        "2. seguranca - Equipamentos de proteção e segurança",
        "3. fatiadores - Software de fatiamento (Chitubox, Lychee, etc.)",
        "4. tipos_resina - Tipos de resina e aplicações",
        "5. calibracao - Como calibrar resina (testes XP2, Ameralabs)",
        "6. suportes - Como fazer suportes eficientes",
        "7. separacao - Como ocar modelos (hollow)",
        "8. nivelamento - Como nivelar impressora",
        "9. impressao - Processo completo de impressão",
        "10. lavagem_cura - Lavagem e cura de peças",
        "11. pos_impressao - Cuidados após impressão",
        "12. polimento - Polimento e remoção de suportes",
        "13. investimentos - Sugestões de compras por nível",
        "14. marcas - Marcas confiáveis (impressoras, resinas, acessórios)"
    ]

# ============================================================================
# METADATA
# ============================================================================

METADATA_GUIA = {
    "versao": "2.0",
    "data_criacao": "2024",
    "autor": "Elio",
    "destinatario": "Ronei (Quanton3D)",
    "total_modulos": 14,
    "total_paginas_pdf": 98,
    "status_integracao": "COMPLETO - 100%",
    "linhas_codigo": 996,
    "ultima_atualizacao": "2025-01-10"
}

# Exportar tudo
__all__ = [
    'PARTES_IMPRESSORA',
    'EQUIPAMENTOS_SEGURANCA',
    'FATIADORES',
    'TIPOS_RESINA',
    'CALIBRACAO_RESINA',
    'SUPORTES',
    'SEPARACAO_MODELOS',
    'NIVELAMENTO',
    'PROCESSO_IMPRESSAO',
    'LAVAGEM_CURA',
    'CUIDADOS_POS_IMPRESSAO',
    'POLIMENTO_REMOCAO',
    'INVESTIMENTOS',
    'MARCAS_CONFIAVEIS',
    'buscar_informacao_guia',
    'listar_modulos_disponiveis',
    'METADATA_GUIA'
]

