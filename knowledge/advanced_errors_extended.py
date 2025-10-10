"""
BASE DE ERROS AVANÇADOS ESTENDIDA - BOTELLIO
Categorias 6-10: Problemas de Hardware, Software, Ambientais e Pós-Processamento
"""

# =============================================================================
# CATEGORIA 6: PROBLEMAS ELETRÔNICOS E DE HARDWARE
# =============================================================================

CATEGORIA_6_HARDWARE_ELETRONICO = {
    "erro_6_1": {
        "nome": "Pixels 'fantasma' no LCD (stuck pixels)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Degradação do LCD por uso prolongado OU problema no driver de vídeo OU dano por resina infiltrada.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Execute ciclo de refresh completo do LCD (função no menu). 2) Verifique conexão do cabo flat do LCD. 3) Aumente exposição em 10-15% para compensar.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Pixel Refresh**: Rodar padrão de teste por 30 minutos
2. **Teste de Stress**: Verificar padrão de pixels mortos
3. **Verificação de Cabo**: Reconectar cabo flat do LCD
4. **Atualização de Firmware**: Atualizar para versão mais recente
5. **Substituição Preventiva**: LCD tem vida útil de 500-1000h
6. **Configurações Compensatórias**:
   - Mapear pixels mortos e evitar usar essas áreas
   - Usar anti-aliasing para suavizar bordas
   - Aumentar exposição em 10-15%""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    },
    
    "erro_6_2": {
        "nome": "Aquecimento excessivo da eletrônica",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Problema de dissipação térmica OU sobrecarga elétrica nos drivers OU ventilação inadequada.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Adicione ventiladores extras na eletrônica. 2) Reduza corrente dos motores para 80% do máximo. 3) Faça pausa de 5 min a cada 2h de impressão.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Ventilação Forçada**: Adicionar ventiladores 12V extras
2. **Dissipadores Extras**: Instalar em drivers de motor
3. **Relocação**: Mover eletrônica para fora da câmara aquecida
4. **Verificação Elétrica**: Medir corrente dos motores
5. **Pasta Térmica**: Reaplicar em componentes críticos
6. **Configurações de Proteção**:
   - Adicionar pausa térmica automática
   - Monitorar temperatura com sensor externo
   - Reduzir velocidades para diminuir carga""",
        
        "categoria": "Moderado",
        "frequencia": "Baixa"
    },
    
    "erro_6_3": {
        "nome": "Desgaste prematuro do FEP (menos de 10 impressões)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Tensão inadequada do FEP OU química incompatível resina-FEP OU abrasão excessiva por limpeza incorreta.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Verifique tensão do FEP (deve soar como tambor ao bater). 2) Use apenas espátula de plástico macio. 3) Aplique PTFE spray (muito pouco) no FEP.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Tensão Otimizada**: Usar medidor de tensão ou app de frequência sonora
2. **Química Compatível**: Verificar compatibilidade resina-FEP
3. **Limpeza Suave**: Apenas espátula plástica macia
4. **Substituição por nFEP**: Mais durável que FEP comum
5. **Configurações para Preservar FEP**:
   - Lift speed máximo: 80 mm/min
   - Usar tilt se disponível
   - Evitar impressões com base > 50% da área do tanque""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    }
}

# =============================================================================
# CATEGORIA 7: PROBLEMAS AMBIENTAIS EXTREMOS
# =============================================================================

CATEGORIA_7_PROBLEMAS_AMBIENTAIS = {
    "erro_7_1": {
        "nome": "Falha em ambiente com alta umidade (>70%)",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Absorção de umidade pela resina OU condensação no LCD OU alteração das propriedades de cura.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Use desumidificador no ambiente (manter < 50%). 2) Aqueça impressora 30min antes do uso. 3) Aumente exposição em 15-20%.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Desumidificação**: Manter ambiente < 50% umidade relativa
2. **Aquecimento Preventivo**: 30 min antes do uso
3. **Vedação**: Vedar completamente câmara da impressora
4. **Sílica Gel**: Colocar sachês próximo à resina
5. **Pré-aquecimento da Resina**: 30°C antes do uso
6. **Configurações para Umidade**:
   - Aumentar exposição em 15-20%
   - Reduzir velocidades
   - Fazer teste de calibração diário""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    },
    
    "erro_7_2": {
        "nome": "Impressão falha com variação de temperatura ambiente",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Expansão térmica diferencial OU mudança de viscosidade da resina OU variação nas propriedades de cura.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Isole impressora com caixa térmica. 2) Use aquecedor com termostato. 3) Ajuste exposição: -10% para cada 5°C acima de 25°C.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Isolamento Térmico**: Espuma ou caixa térmica
2. **Aquecimento Ativo**: Aquecedor + termostato
3. **Compensação Automática**: Sensor de temperatura + ajuste automático
4. **Massa Térmica**: Adicionar recipiente com água para estabilizar
5. **Programação Horária**: Imprimir em horários de temperatura estável
6. **Configurações Térmicas**:
   - Criar perfis: frio/normal/quente
   - Monitorar temperatura da resina
   - Ajustar exposição dinamicamente""",
        
        "categoria": "Moderado",
        "frequencia": "Alta"
    },
    
    "erro_7_3": {
        "nome": "Contaminação por poeira e partículas",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Ambiente não controlado OU falta de filtração OU manipulação inadequada.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Filtre SEMPRE a resina antes de usar (malha 40 microns). 2) Cubra impressora quando não estiver em uso. 3) Limpe área de trabalho antes de imprimir.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Ambiente Limpo**: Área dedicada, circulação controlada
2. **Filtro HEPA**: Sistema de filtragem de ar
3. **Procedimentos de Sala Limpa**: Conforme NBR ISO 14644-5
4. **Troca Regular de IPA**: Não reutilizar banhos sujos
5. **Equipamentos de Proteção**: Toucas, propés, luvas
6. **Inspeção Óptica**: Luz polarizada para detectar contaminação""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    }
}

# =============================================================================
# CATEGORIA 8: PROBLEMAS DE SOFTWARE E ARQUIVO
# =============================================================================

CATEGORIA_8_SOFTWARE_ARQUIVO = {
    "erro_8_1": {
        "nome": "Corrupção de arquivo durante impressão longa",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Problema no cartão SD OU USB OU memória da impressora OU arquivo corrompido.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Use cartão SD industrial classe 10 ou superior. 2) Formate cartão antes de usar. 3) Verifique integridade do arquivo (checksum MD5).",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Verificação de Integridade**: Usar checksum MD5
2. **Cartão SD Industrial**: SLC (Single-Level Cell) para durabilidade
3. **Backup Redundante**: Salvar em múltiplas localizações
4. **Desfragmentação**: Desfragmentar cartão regularmente
5. **Teste de Stress**: Software específico para testar cartão
6. **Configurações de Segurança**:
   - Formatar a cada 10 impressões
   - Manter backup dos arquivos críticos
   - Usar conexão USB se disponível""",
        
        "categoria": "Moderado",
        "frequencia": "Baixa"
    },
    
    "erro_8_2": {
        "nome": "Layers 'perdidas' em arquivo complexo",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Problema de processamento do slicer OU limitação de memória OU STL corrompido.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Simplifique mesh (reduza polígonos). 2) Repare STL com Netfabb ou 3D Builder. 3) Teste com slicer alternativo (ChiTuBox, Lychee).",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Simplificação de Mesh**: Reduzir polígonos do STL
2. **Divisão de Arquivo**: Dividir modelo em partes menores
3. **Slicer Alternativo**: Testar diferentes slicers
4. **Aumento de RAM**: Computador com mais memória
5. **Verificação de STL**: Reparar topologia
6. **Configurações de Otimização**:
   - Reduzir anti-aliasing
   - Usar altura de camada maior
   - Simplicar geometria desnecessária""",
        
        "categoria": "Moderado",
        "frequencia": "Baixa"
    },
    
    "erro_8_3": {
        "nome": "Peça impressa 'no ar' ou apenas suportes aparecem",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Modelo mal posicionado no slicer (base abaixo de Z=0) OU arquivo STL corrompido OU configuração incorreta.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Use função 'Drop to bed' no slicer. 2) Verifique preview camada por camada. 3) Certifique-se que nenhuma parte está abaixo do plano zero.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Reposicionamento**: Função 'Drop to bed' + verificação visual
2. **Reparo de STL**: Netfabb, Meshmixer, PrusaSlicer
3. **Verificação de Preview**: Inspecionar todas as camadas
4. **Configuração de Parâmetros**: Revisar altura de camada, exposição
5. **Teste de Validação**: Imprimir cubo de teste antes de peça complexa""",
        
        "categoria": "Crítico",
        "frequencia": "Média"
    }
}

# =============================================================================
# CATEGORIA 9: PROBLEMAS ESPECÍFICOS POR TIPO DE RESINA
# =============================================================================

CATEGORIA_9_RESINAS_ESPECIAIS = {
    "erro_9_1": {
        "nome": "Resina flexível não cura adequadamente",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Inibição por oxigênio OU configuração inadequada para elastômeros OU temperatura muito baixa.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Aumente exposição em 50-100% (ex: de 2.5s para 5-8s). 2) Aqueça resina a 30-32°C. 3) Use suportes mais densos e finos.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Atmosfera Controlada**: Câmara com nitrogênio para cura final (avançado)
2. **Exposição Prolongada**: 2-3x tempo de resina rígida
3. **Pós-Cura Específica**: 405nm, 15-25 minutos
4. **Temperatura Controlada**: 28-32°C (aquecimento essencial)
5. **Configurações para Flexíveis**:
   - Lift speed: 30-50 mm/min (muito lento)
   - Bottom layers: 10-15
   - Suportes mais densos
6. **Pós-Cura em Água**: Submerso em água morna (50°C)""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    },
    
    "erro_9_2": {
        "nome": "Resina cerâmica com partículas sedimentadas",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Separação de fases OU agitação inadequada OU tempo de repouso muito longo.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Misture por 10-15 minutos antes do uso. 2) Aqueça a 30-35°C para reduzir viscosidade. 3) Agite a cada 30 min durante impressão.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Agitação Contínua**: Agitador magnético durante impressão
2. **Homogeneização**: 10-15 min antes do uso
3. **Viscosidade Ajustada**: 30-35°C
4. **Filtração Cuidadosa**: 100 microns (não muito fino)
5. **Armazenamento Vertical**: Em pé para evitar sedimentação
6. **Configurações para Cerâmicas**:
   - Exposição aumentada em 30-50%
   - Velocidades reduzidas
   - Agitação periódica""",
        
        "categoria": "Avançado",
        "frequencia": "Baixa"
    },
    
    "erro_9_3": {
        "nome": "Resina transparente fica turva ou amarelada",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Lavagem incompleta OU super-cura UV (amarelamento) OU água/IPA residual na superfície.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Use IPA 99% (não 70%). 2) Reduza tempo de pós-cura UV para 5-8 minutos. 3) Seque completamente antes da cura.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Lavagem Premium**: IPA 99.9%, trocar frequentemente
2. **Cura Controlada**: Máximo 5-8 minutos, temperatura < 35°C
3. **Clareamento**: Aplicar verniz transparente UV após cura
4. **Lixamento e Polimento**:
   - Lixar: grão 400 → 800 → 1500 → 3000
   - Polir: composto acrílico
   - Resultado: transparência restaurada
5. **Prevenção**: Não super-curar, secar bem antes da cura""",
        
        "categoria": "Moderado",
        "frequencia": "Alta"
    }
}

# =============================================================================
# CATEGORIA 10: PÓS-PROCESSAMENTO AVANÇADO
# =============================================================================

CATEGORIA_10_POS_PROCESSAMENTO = {
    "erro_10_1": {
        "nome": "Deformação durante pós-cura UV",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Tensões internas liberadas pelo calor OU cura não uniforme OU temperatura excessiva.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Mantenha peça suportada durante cura. 2) Use múltiplos ciclos curtos (2min → 4min → 6min). 3) Mantenha temperatura < 40°C.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Cura Gradual**: Aumentar tempo gradualmente
2. **Suporte Durante Cura**: Manter peça apoiada
3. **Temperatura Controlada**: < 40°C sempre
4. **Rotação Contínua**: Plataforma giratória para uniformidade
5. **Pré-aquecimento**: Aquecer peça gradualmente
6. **Configurações de Pós-Cura**:
   - Múltiplos ciclos curtos
   - Pausas de 5 min entre ciclos
   - Monitorar temperatura com IR""",
        
        "categoria": "Moderado",
        "frequencia": "Média"
    },
    
    "erro_10_2": {
        "nome": "Dificuldade extrema para remover suportes",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Suportes muito grossos OU penetração excessiva OU super-cura antes da remoção.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) SEMPRE remova suportes ANTES da pós-cura UV. 2) Use alicate de corte fino. 3) Congele peça por 30 min (facilita remoção).",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Remoção Antes da Cura**: CRÍTICO - sempre antes da pós-cura
2. **Técnica de Congelamento**: 30 min no freezer
3. **Ferramentas Adequadas**: Alicate de corte fino, estilete
4. **Suportes Otimizados**:
   - Usar suportes leves/médios
   - Penetração: 0.2-0.3mm (não mais)
   - Tree supports para facilitar remoção
5. **Acabamento**: Lixar pontos de contato após remoção""",
        
        "categoria": "Moderado",
        "frequencia": "Alta"
    },
    
    "erro_10_3": {
        "nome": "Opacidade após lavagem com álcool",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Resíduo de álcool OU reação química com resina OU IPA de baixa pureza (70%).",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Use IPA 99.9% (não 70%). 2) Lave em 2 etapas: IPA sujo → IPA limpo. 3) Seque com ar comprimido.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Álcool de Alta Pureza**: IPA 99.9%
2. **Lavagem em Etapas**:
   - 1ª lavagem: IPA sujo (3-5 min)
   - 2ª lavagem: IPA limpo (2-3 min)
3. **Secagem Forçada**: Ar comprimido + 10 min ao ar
4. **Alternativa ao Álcool**: Mean Green ou Simple Green
5. **Banho Ultrassônico**: 3-5 min em IPA
6. **Processo Otimizado**:
   - Tempo máximo: 5 min por banho
   - Temperatura: ambiente
   - Secagem: 10 min antes da cura""",
        
        "categoria": "Moderado",
        "frequencia": "Alta"
    }
}

# =============================================================================
# PROBLEMAS MECÂNICOS AVANÇADOS
# =============================================================================

CATEGORIA_11_MECANICA_AVANCADA = {
    "erro_11_1": {
        "nome": "Desalinhamento de eixos e Z-wobble",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Desalinhamento do acoplador motor-fuso OU parafusos-guia desgastados OU rolamentos sujos.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) Limpe fuso com IPA e aplique graxa de lítio. 2) Verifique se acoplador está firme e centralizado. 3) Reduza velocidades em 50%.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Desmontagem e Limpeza**: Limpar fuso completamente
2. **Lubrificação Adequada**: Graxa de lítio branca (não óleo)
3. **Aperto de Componentes**: Verificar todos os parafusos
4. **Alinhamento**: Usar relógio comparador
5. **Calibração de Firmware**: Steps/mm do motor Z
6. **Prevenção**: Manutenção a cada 100 horas de uso""",
        
        "categoria": "Crítico",
        "frequencia": "Média"
    },
    
    "erro_11_2": {
        "nome": "Vazamento de resina na câmara mecânica/eletrônica",
        "diagnostico": "🔍 DIAGNÓSTICO PRIMÁRIO: Má vedação do tanque OU trincas no tanque OU derramamento durante manipulação.",
        
        "solucao_imediata": "🛠 SOLUÇÃO IMEDIATA: 1) PARE imediatamente. 2) Limpe com pano macio + IPA. 3) Desmonte componentes afetados para limpeza criteriosa.",
        
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:
1. **Ação Emergencial**: Parar operação imediatamente
2. **Limpeza Profunda**: IPA 99% + panos sem fiapos
3. **Inspeção de Danos**: Verificar LCD, motores, placas
4. **Vedação**: Aplicar silicone industrial nos pontos críticos
5. **Proteção Física**: Barreiras anti-respingos
6. **Prevenção**:
   - Verificar vedação do tanque regularmente
   - Trocar tanque ao primeiro sinal de trinca
   - Manipular resina com cuidado""",
        
        "categoria": "Crítico",
        "frequencia": "Baixa"
    }
}

# =============================================================================
# FUNÇÃO DE BUSCA EXPANDIDA
# =============================================================================

def buscar_erro_avancado(sintoma, categoria=None):
    """
    Busca avançada de erros com filtro por categoria
    """
    todas_categorias = {
        **CATEGORIA_6_HARDWARE_ELETRONICO,
        **CATEGORIA_7_PROBLEMAS_AMBIENTAIS,
        **CATEGORIA_8_SOFTWARE_ARQUIVO,
        **CATEGORIA_9_RESINAS_ESPECIAIS,
        **CATEGORIA_10_POS_PROCESSAMENTO,
        **CATEGORIA_11_MECANICA_AVANCADA
    }
    
    resultados = []
    sintoma_lower = sintoma.lower()
    
    for erro_id, erro_data in todas_categorias.items():
        if categoria and not erro_id.startswith(f"erro_{categoria}_"):
            continue
            
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
    'CATEGORIA_6_HARDWARE_ELETRONICO',
    'CATEGORIA_7_PROBLEMAS_AMBIENTAIS',
    'CATEGORIA_8_SOFTWARE_ARQUIVO',
    'CATEGORIA_9_RESINAS_ESPECIAIS',
    'CATEGORIA_10_POS_PROCESSAMENTO',
    'CATEGORIA_11_MECANICA_AVANCADA',
    'buscar_erro_avancado'
]

