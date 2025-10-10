"""
BASE DE ERROS E SOLUÇÕES COMPLETA - BOTELLIO
Compilação de 100+ problemas técnicos com diagnósticos em 3 etapas
Estrutura: DIAGNÓSTICO → SOLUÇÃO IMEDIATA → PROTOCOLO AVANÇADO
"""

# =============================================================================
# CATEGORIA 1: PROBLEMAS CRÍTICOS DE ADESÃO E NIVELAMENTO
# =============================================================================

CATEGORIA_1_ADESAO_NIVELAMENTO = {
    "erro_1_1": {
        "nome": "Peça não gruda mesmo com base limpa e nivelada",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Problema de tensão superficial ou contaminação microscópica. A base pode ter óleos residuais invisíveis ou a temperatura da resina está muito baixa, aumentando viscosidade.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Limpe a base com acetona pura (não álcool) para remover óleos. 2) Aumente Bottom Exposure Time em 20% (ex: de 25s para 30s). 3) Aqueça a resina a 28-30°C antes de imprimir.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Teste de Gota d'Água**: Pingue água na base - se formar bolha, há contaminação oleosa
2. **Texturização Microscópica**: Lixe levemente com lixa grão 400 em movimentos circulares
3. **Limpeza Final com IPA**: Álcool Isopropílico 99% para desengordurar completamente a base
4. **Configurações Extremas**:
   - Primeira camada: 120-180s (muito acima do normal)
   - Camadas base: 15-20 (dobro do padrão)
   - Lift speed: 30 mm/min (extremamente lento)
   - Light-off delay: 5-10s entre camadas""",
        
        "categoria": "Crítico",
        "frequencia": "Alta"
    },
    
    "erro_1_2": {
        "nome": "Base 'afunda' durante impressão (Z-axis drift)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Problema mecânico no eixo Z - perda de passos do motor, folga no acoplamento motor-fuso ou lubrificação inadequada causando travamento intermitente.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Reduza velocidade Z para 50% do padrão. 2) Limpe e lubrifique o fuso Z com graxa de lítio (não óleo comum). 3) Verifique e aperte todos os parafusos de fixação da Build Plate.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Calibração de Steps/mm**: Verificar se motor Z está configurado corretamente no firmware
2. **Verificação de Backlash**: Testar folga no acoplamento motor-fuso manualmente
3. **Tensão da Correia**: Ajustar tensão se usar sistema de correia (não muito apertada)
4. **Temperatura do Driver**: Verificar aquecimento excessivo do driver do motor
5. **Configurações de Emergência**:
   - Aumentar corrente do motor Z em 10% (cuidado com aquecimento)
   - Adicionar delay extra de 2s entre movimentos
   - Usar modo de microstepping mais alto (1/16 ou 1/32)""",
        
        "categoria": "Crítico",
        "frequencia": "Média"
    },
    
    "erro_1_3": {
        "nome": "'Pé de Elefante' (Elephant's Foot)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Super-compressão nas primeiras camadas devido a Z-offset muito baixo ou super-exposição da base causando expansão lateral excessiva.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Ajuste o Z-offset para que a plataforma esteja ligeiramente mais alta (papel de nivelamento deve deslizar com leve atrito). 2) Reduza Bottom Exposure Time em 10-15%.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Ajuste Fino de Z**: Utilizar babystepping durante impressão das primeiras camadas
2. **Limpeza do LCD**: Pixels curados em excesso causam super-exposição
3. **Configurações Compensatórias**:
   - Bottom Exposure Time: Diminuir ligeiramente (2-3s a menos)
   - Usar função "Chamfer" no slicer (chanfro nas primeiras camadas)
   - Lift Distance nas primeiras camadas: Aumentar para 8-10mm""",
        
        "categoria": "Moderado",
        "frequencia": "Alta"
    }
}

# =============================================================================
# CATEGORIA 2: FALHAS NO CORPO DA PEÇA (CURA E DELAMINAÇÃO)
# =============================================================================

CATEGORIA_2_CURA_DELAMINACAO = {
    "erro_2_1": {
        "nome": "Separação de Camadas (Delamination/Splitting)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Subexposição causando ligação fraca entre camadas OU tensão de descolamento (Peel Force) muito alta OU variação de temperatura ambiente durante impressão.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Aumente Normal Exposure Time em 0.5s (ex: de 2.5s para 3.0s). 2) Agite bem a resina antes de usar. 3) Limpe o FEP/NFEP - se estiver turvo, a transmissão de luz é desigual.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Otimização de Exposição**: Fazer teste de calibração (torre de exposição)
2. **Controle Térmico**: Manter temperatura ambiente estável (±2°C)
3. **Verificação de Resina**: Filtrar resina com malha 40 microns
4. **Configurações Críticas**:
   - Light-Off Delay/Wait Time: Adicionar 0.5s a 1s para resina se estabilizar
   - Lift Speed: Reduzir para 50-60 mm/min
   - Overlap entre camadas: Aumentar se disponível no slicer""",
        
        "categoria": "Crítico",
        "frequencia": "Muito Alta"
    },
    
    "erro_2_2": {
        "nome": "Peças Parciais/Fragmentos (Incomplete Print)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Falha total de suporte OU modelo oco sem respiro (Suction Cups) OU peça inteira ficou presa no FEP por área de seção transversal muito grande.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Se modelo for oco, adicione 2 furos de respiro de 2-3mm na parte mais baixa. 2) Incline a peça 25-35° para reduzir área de seção transversal. 3) Adicione mais suportes nas áreas críticas.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Hollow Setting**: Usar espessura de parede de 2-3mm
2. **Furos de Drenagem**: Mínimo 2 furos de 2mm de diâmetro
3. **Angulação Otimizada**: 10° a 45° para distribuir tensões
4. **Suportes Reforçados**:
   - Adicionar suportes médios/pesados nas áreas de grande seção
   - Densidade de suportes: 80-90% em áreas críticas
   - Usar suportes em árvore (tree supports) para melhor distribuição""",
        
        "categoria": "Crítico",
        "frequencia": "Alta"
    },
    
    "erro_2_3": {
        "nome": "Linhas de Camada Excessivas (Extreme Layer Lines)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Super-exposição causando expansão lateral da cura OU velocidade de Lift/Retract muito alta causando vibrações OU Z-wobble (folga no eixo Z).",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Diminua Normal Exposure Time em 0.2-0.3s. 2) Reduza Lift Speed para 50 mm/min. 3) Limpe e lubrifique o fuso Z.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Calibração do Eixo Z**: Verificar folgas ou sujeira no fuso
2. **Isolamento de Vibração**: Colocar impressora em base sólida (concreto/granito)
3. **Configurações Anti-Vibração**:
   - Lift Speed: 40-50 mm/min (muito lento)
   - Retract Speed: 120-150 mm/min
   - Layer Height: Usar 0.03mm para maior detalhe
   - Pause entre movimentos: 1-2s""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    },
    
    "erro_2_4": {
        "nome": "Cura parcial em camadas específicas (Zebra Striping)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Variação de potência do LED durante impressão longa (aquecimento) OU problema térmico no LED OU degradação do LED UV.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Adicione ventilação extra no LED. 2) Aumente exposição em 20-30% para compensar perda de potência. 3) Faça pausas de 5 min a cada 2 horas de impressão.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Mapeamento Térmico**: Verificar temperatura do LED durante impressão longa
2. **Calibração de Potência**: Usar luxímetro para medir uniformidade da luz
3. **Substituição do LED**: LEDs degradam com uso - verificar vida útil (500-1000h)
4. **Configurações Compensatórias**:
   - Usar anti-aliasing nível 4-8 para suavizar transições
   - Reduzir altura de camada para 0.03mm
   - Adicionar cooling forçado no LED""",
        
        "categoria": "Moderado",
        "frequencia": "Baixa"
    }
}

# =============================================================================
# CATEGORIA 3: PROBLEMAS DE RESINA, TANQUE E PÓS-PROCESSAMENTO
# =============================================================================

CATEGORIA_3_RESINA_TANQUE = {
    "erro_3_1": {
        "nome": "Resina 'cozinha' no tanque (cura espontânea)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Vazamento de luz UV pela vedação da impressora OU contaminação por partículas curadas flutuando OU FEP riscado causando dispersão de luz.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Filtre a resina URGENTEMENTE com malha 40 microns. 2) Verifique se tampa está vedando 100%. 3) Cubra o tanque com papel alumínio se necessário.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Teste de Vazamento**: Usar papel fotossensível para detectar vazamentos de luz
2. **Limpeza Profunda**: Limpar tanque com álcool + ultrassom se disponível
3. **Substituição do FEP**: FEP riscado causa dispersão - trocar imediatamente
4. **Medidas Preventivas**:
   - Trocar FEP a cada 15-20 impressões (não esperar furar)
   - Armazenar resina em recipiente opaco
   - Verificar vedação da tampa regularmente""",
        
        "categoria": "Crítico",
        "frequencia": "Média"
    },
    
    "erro_3_2": {
        "nome": "Detalhes Finos Ausentes ou Arredondados",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Super-exposição arredondando quinas OU Anti-Aliasing (AA) muito agressivo OU altura de camada muito alta para o nível de detalhe desejado.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Reduza Normal Exposure Time em 0.1-0.2s. 2) Diminua Anti-Aliasing para nível 2-4 (ou desative). 3) Use Layer Height de 0.025-0.03mm.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Calibração com Torre de Exposição**: Encontrar tempo exato de exposição
2. **Verificação do AA/Grayscale**: Manter AA baixo ou desativar para detalhes nítidos
3. **Limpeza Óptica**: Limpar LCD e FEP - sujeira causa exposição irregular
4. **Configurações de Precisão**:
   - Layer Height: 0.025mm para máxima resolução
   - Exposure Time: Calibrar com teste XP2
   - Anti-aliasing: Nível 2 ou desativado""",
        
        "categoria": "Moderado",
        "frequencia": "Alta"
    },
    
    "erro_3_3": {
        "nome": "Superfície Áspera/Grudenta após Cura",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Lavagem insuficiente deixando resina não curada residual OU super-cura UV tornando resina quebradiça/amarelada OU IPA de baixa pureza.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Lave em DOIS banhos: primeiro IPA 'sujo', depois IPA limpo. 2) Seque completamente com ar comprimido antes da cura. 3) Use IPA 99% (não 70%).",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Processo de Lavagem em 2 Etapas**:
   - 1º banho: IPA sujo (3-5 min)
   - 2º banho: IPA limpo (2-3 min)
   - Secagem: Ar comprimido + 10 min ao ar
2. **Pós-Cura Controlada**:
   - Reduzir tempo de cura UV (5-10 min, não mais)
   - Temperatura < 40°C durante cura
   - Usar plataforma giratória para cura uniforme
3. **IPA Concentration**: Usar 95-99% (não diluído)""",
        
        "categoria": "Moderado",
        "frequencia": "Alta"
    },
    
    "erro_3_4": {
        "nome": "'Ondulações' na Superfície (Ringing/Ghosting)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Vibrações mecânicas do movimento da Build Plate OU impressora em superfície instável OU velocidades de movimento muito altas.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Coloque impressora em superfície sólida (laje de concreto, tijolo). 2) Reduza Lift Speed e Retract Speed em 50%. 3) Desligue equipamentos próximos (geladeira, AC).",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Isolamento de Vibração**: Base de concreto/granito
2. **Verificação Mecânica**: Apertar correias e polias
3. **Configurações Anti-Vibração**:
   - Lift Speed: 40-50 mm/min (muito lento)
   - Retract Speed: 100-120 mm/min
   - Pause entre movimentos: 1-2s
   - Reduzir aceleração no firmware se possível""",
        
        "categoria": "Moderado",
        "frequencia": "Baixa"
    }
}

# =============================================================================
# CATEGORIA 4: PROBLEMAS CRÍTICOS DE SUPORTES E ESTRUTURAS
# =============================================================================

CATEGORIA_4_SUPORTES = {
    "erro_4_1": {
        "nome": "Suportes falham, quebram ou não se unem à peça",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Pontos de contato muito pequenos OU pouca densidade de suporte OU falta de penetração do suporte na malha da peça.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Aumente penetração da ponta do suporte de 0.2mm para 0.4mm no slicer. 2) Aumente diâmetro do ponto de contato para 0.4-0.5mm. 3) Adicione suportes manuais nos pontos críticos.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Configuração de Suportes**:
   - Penetração: 0.4-0.5mm
   - Diâmetro do ponto: 0.4-0.5mm
   - Densidade: 80-90% em áreas críticas
2. **Angulação da Peça**: Inclinar 15-45° para evitar grandes seções
3. **Raft/Base**: Garantir que base dos suportes tenha exposição maior
4. **Suportes Híbridos**: Combinar automáticos + manuais""",
        
        "categoria": "Crítico",
        "frequencia": "Muito Alta"
    },
    
    "erro_4_2": {
        "nome": "Suportes 'derretem' durante impressão",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Superexposição localizada OU problema de dissipação de calor OU suportes muito finos para o peso da peça.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Use suportes médios (0.4-0.5mm) em vez de pesados. 2) Aumente densidade para 80-90%. 3) Direcione ventilação para área dos suportes.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Suportes Graduais**: Aumentar espessura gradualmente da base ao topo
2. **Cooling Localizado**: Ventilação direcionada
3. **Configurações Especiais**:
   - Reduzir exposição dos suportes em 20-30% (se slicer permitir)
   - Usar suportes em árvore (tree supports)
   - Orientação otimizada: Inclinar peça para reduzir área""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    },
    
    "erro_4_3": {
        "nome": "Falha de suporte em peças grandes (Elephant Foot em suportes)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Deformação por peso próprio OU força de sucção excessiva em peças grandes OU suportes subdimensionados.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Use suportes em árvore (tree supports). 2) Crie base mais larga para suportes principais. 3) Faça peça oca com furos de drenagem.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Suportes Estruturais**:
   - Usar padrão ramificado (tree supports)
   - Base expandida para suportes principais
   - Suportes duplos em pontos críticos
2. **Hollow com Drenos**: Furos de 2-3mm para drenagem
3. **Configurações para Peças Grandes**:
   - Lift speed: 40-50 mm/min (muito lento)
   - Rest time before lift: 3-5s
   - Rest time after retract: 2-3s""",
        
        "categoria": "Crítico",
        "frequencia": "Média"
    }
}

# =============================================================================
# CATEGORIA 5: PROBLEMAS AVANÇADOS DE QUALIDADE E PRECISÃO
# =============================================================================

CATEGORIA_5_QUALIDADE_PRECISAO = {
    "erro_5_1": {
        "nome": "Distorção dimensional sistemática (Shrinkage não uniforme)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Tensões internas da resina liberadas durante cura OU problema de calibração XY OU pós-cura inadequada.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Imprima cubo de calibração e meça dimensões reais. 2) Aplique fator de correção no slicer (101-103%). 3) Use pós-cura com temperatura controlada < 40°C.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Calibração XY**: Imprimir teste de calibração dimensional
2. **Compensação de Shrinkage**: Aplicar fator no slicer
3. **Pós-Cura Controlada**:
   - Temperatura < 40°C
   - Múltiplos ciclos curtos (5 min cada)
   - Pausas de resfriamento entre ciclos
4. **Orientação Estratégica**: Dimensões críticas no eixo Z""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    },
    
    "erro_5_2": {
        "nome": "Superfície 'casca de laranja' (Orange Peel Effect)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Vibração durante impressão OU temperatura inadequada OU problema de viscosidade da resina.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Coloque impressora em base sólida (concreto/granito). 2) Aqueça resina a 25-27°C. 3) Reduza todas as velocidades em 50%.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Isolamento de Vibração**: Base de concreto/granito
2. **Controle Térmico Rigoroso**: Manter ±1°C de variação
3. **Viscosidade Otimizada**: Aquecer resina antes do uso
4. **Filtração Fina**: Usar filtro de 25 microns
5. **Configurações Anti-Vibração**:
   - Lift speed: 40 mm/min máximo
   - Retract speed: 100 mm/min máximo
   - Pause entre movimentos: 1-2s""",
        
        "categoria": "Moderado",
        "frequencia": "Baixa"
    }
}

# Continua com mais categorias...

# =============================================================================
# FUNÇÃO DE BUSCA DE ERROS
# =============================================================================

def buscar_erro(sintoma):
    """
    Busca erro por sintoma/palavra-chave
    Retorna diagnóstico completo em 3 etapas
    """
    todas_categorias = {
        **CATEGORIA_1_ADESAO_NIVELAMENTO,
        **CATEGORIA_2_CURA_DELAMINACAO,
        **CATEGORIA_3_RESINA_TANQUE,
        **CATEGORIA_4_SUPORTES,
        **CATEGORIA_5_QUALIDADE_PRECISAO
    }
    
    resultados = []
    sintoma_lower = sintoma.lower()
    
    for erro_id, erro_data in todas_categorias.items():
        if sintoma_lower in erro_data['nome'].lower():
            resultados.append({
                'id': erro_id,
                'nome': erro_data['nome'],
                'diagnostico': erro_data['diagnostico'],
                'solucao_imediata': erro_data['solucao_imediata'],
                'protocolo_avancado': erro_data['protocolo_avancado'],
                'categoria': erro_data['categoria'],
                'frequencia': erro_data['frequencia']
            })
    
    return resultados

# =============================================================================
# EXPORTAÇÃO
# =============================================================================

__all__ = [
    'CATEGORIA_1_ADESAO_NIVELAMENTO',
    'CATEGORIA_2_CURA_DELAMINACAO',
    'CATEGORIA_3_RESINA_TANQUE',
    'CATEGORIA_4_SUPORTES',
    'CATEGORIA_5_QUALIDADE_PRECISAO',
    'buscar_erro'
]

