"""
Base de Conhecimento Expandida Completa - Integração do CONHECIMENTO(1).txt
Desenvolvido por Elio para Ronei e Quanton3D
Data: 10/10/2025
"""

# ============================================================================
# CATEGORIA 3: PROBLEMAS DE DETALHE, RUPTURA E GEOMETRIA
# ============================================================================

CATEGORIA_3_DETALHE_RUPTURA_GEOMETRIA = {
    "layer_splitting": {
        "nome": "Ruptura ou 'quebra' da peça (Layer Splitting)",
        "sintomas": [
            "Peça se parte ao longo de uma camada específica",
            "Delaminação entre camadas",
            "Fraturas horizontais visíveis",
            "Peça se separa em duas partes"
        ],
        "diagnostico": """🔍 DIAGNÓSTICO PRIMÁRIO:
Layer Splitting (ruptura entre camadas) ocorre quando a adesão intercamadas falha. As causas principais são:

1. **Subexposição Crítica** (70% dos casos)
   - Tempo de exposição insuficiente para cura completa
   - Camadas não se fundem adequadamente
   - Ligações químicas fracas entre camadas

2. **Contaminação da Resina** (20% dos casos)
   - Resina contaminada com IPA residual
   - Mistura de resinas incompatíveis
   - Resina vencida ou degradada

3. **Problemas Mecânicos** (10% dos casos)
   - Vibração excessiva durante impressão
   - Desalinhamento do eixo Z
   - Força de separação muito alta

**Diagnóstico Específico:**
- Se a ruptura ocorre sempre na mesma altura → Problema mecânico (eixo Z)
- Se ocorre em alturas variáveis → Subexposição ou contaminação
- Se ocorre em peças finas → Força de separação muito alta""",
        "solucao_imediata": """🛠 SOLUÇÃO IMEDIATA:

1. **Aumentar Tempo de Exposição** (Ação Prioritária)
   - Aumente 20-30% o tempo de exposição normal
   - Exemplo: Se usa 2.5s, teste com 3.0-3.3s
   - Faça teste de calibração XP2 Validation Matrix

2. **Verificar Qualidade da Resina**
   - Agite vigorosamente por 2-3 minutos
   - Verifique data de validade
   - Filtre a resina para remover partículas

3. **Reduzir Velocidade de Elevação**
   - Diminua Lift Speed em 30-40%
   - Exemplo: De 80mm/min para 50mm/min
   - Isso reduz stress mecânico entre camadas""",
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:

**1. TESTE DE CALIBRAÇÃO COMPLETO**

A) Matriz de Exposição (XP2 Validation Matrix):
   - Baixe o arquivo STL do teste XP2
   - Fatie com tempos variados: 2.0s, 2.5s, 3.0s, 3.5s, 4.0s
   - Imprima e analise qual tempo dá melhor resultado
   - Use o tempo ideal + 10% de margem de segurança

B) Teste de Tração Intercamadas:
   - Imprima cilindro vertical (20mm diâmetro, 50mm altura)
   - Tente quebrar manualmente
   - Se quebrar facilmente → Subexposição confirmada

**2. CONFIGURAÇÕES OTIMIZADAS ANTI-SPLITTING**

Para Resinas Quanton3D:

| Resina | Tempo Normal | Tempo Anti-Splitting | Lift Speed |
|--------|--------------|---------------------|------------|
| PYROBLAST | 2.0s | 2.6s (+30%) | 50 mm/min |
| IRON 7030 | 2.5s | 3.3s (+32%) | 45 mm/min |
| FLEXFORM | 2.1s | 2.8s (+33%) | 40 mm/min |
| POSEIDON | 1.8s | 2.4s (+33%) | 55 mm/min |

**3. ANÁLISE DE CONTAMINAÇÃO**

Teste de Pureza da Resina:
```
1. Pegue 10ml de resina em copo transparente
2. Deixe em repouso por 30 minutos
3. Observe se há:
   - Sedimentação no fundo → Resina contaminada
   - Separação de fases → Resina degradada
   - Partículas flutuantes → Filtrar urgentemente
```

**4. VERIFICAÇÃO MECÂNICA DO EIXO Z**

A) Teste de Linearidade:
   - Imprima torre de calibração (100mm altura)
   - Meça espessura a cada 10mm
   - Variação > 0.05mm → Desalinhamento do eixo Z

B) Teste de Vibração:
   - Durante impressão, toque levemente na impressora
   - Se vibrar visivelmente → Problema de estabilidade
   - Solução: Colocar em superfície mais rígida

**5. OTIMIZAÇÃO DE FORÇA DE SEPARAÇÃO**

Cálculo da Força de Separação:
```
Força = Área da Camada (cm²) × Fator de Adesão (N/cm²)

Fator de Adesão típico: 15-25 N/cm²

Exemplo: Peça 5cm × 5cm = 25cm²
Força = 25 × 20 = 500N (50kg de força!)
```

Redução de Força:
- Adicione furos de ventilação (5mm diâmetro)
- Incline peça 15-30° para reduzir área de sucção
- Use suportes mais densos para distribuir força

**6. PROTOCOLO DE RECUPERAÇÃO DE RESINA CONTAMINADA**

Se suspeitar de contaminação:
```
1. Filtrar resina com filtro 100 microns
2. Deixar em recipiente aberto por 24h (evaporar IPA)
3. Agitar vigorosamente por 5 minutos
4. Fazer teste de impressão pequeno
5. Se falhar → Descartar resina
```

**7. CONFIGURAÇÕES AVANÇADAS ANTI-SPLITTING**

Para impressoras LCD/DLP:

```python
# Configuração Conservadora (Máxima Adesão)
LAYER_HEIGHT = 0.05mm
EXPOSURE_TIME = TEMPO_NORMAL × 1.3
LIFT_DISTANCE = 8mm
LIFT_SPEED = 40 mm/min
RETRACT_SPEED = 120 mm/min
LIGHT_OFF_DELAY = 1.5s
```

**8. DICA DE OURO: CAMADAS DE TRANSIÇÃO**

Para peças críticas:
- Aumente exposição das primeiras 50 camadas em 15%
- Exemplo: Camadas 1-10: +30%, 11-30: +20%, 31-50: +10%
- Isso cria "zona de segurança" na base da peça

**9. ANÁLISE POST-MORTEM**

Se a peça já quebrou:
```
1. Examine a superfície de fratura:
   - Lisa e brilhante → Subexposição
   - Rugosa e opaca → Contaminação
   - Com linhas paralelas → Vibração mecânica

2. Teste de dureza:
   - Pressione unha na superfície
   - Se marcar facilmente → Subcurada
```

**10. PREVENÇÃO DEFINITIVA**

Checklist Anti-Splitting:
- ✅ Calibração de exposição mensal
- ✅ Filtrar resina a cada 5 impressões
- ✅ Limpar tanque semanalmente
- ✅ Verificar alinhamento eixo Z mensalmente
- ✅ Manter temperatura 22-28°C
- ✅ Agitar resina antes de cada impressão"""
    },
    
    "loss_of_fine_detail": {
        "nome": "Detalhes finos não aparecem (Loss of Fine Detail)",
        "sintomas": [
            "Texturas não aparecem",
            "Detalhes pequenos desaparecem",
            "Superfície lisa onde deveria ter relevo",
            "Letras pequenas ilegíveis"
        ],
        "diagnostico": """🔍 DIAGNÓSTICO PRIMÁRIO:
Perda de detalhes finos ocorre quando a resolução efetiva da impressão é insuficiente. Causas principais:

1. **Altura de Camada Muito Alta** (50% dos casos)
   - Camadas grossas não capturam detalhes pequenos
   - Efeito "escada" muito pronunciado
   - Detalhes < 2× altura de camada desaparecem

2. **Subexposição Localizada** (30% dos casos)
   - Detalhes finos não curam completamente
   - Resina líquida "lava" detalhes durante lavagem
   - Exposição insuficiente para geometrias pequenas

3. **Problemas de Fatiamento** (15% dos casos)
   - Slicer não detecta detalhes muito pequenos
   - Anti-aliasing mal configurado
   - Resolução do modelo 3D insuficiente

4. **LCD/Projetor com Baixa Resolução** (5% dos casos)
   - Pixels muito grandes para detalhes finos
   - Impressora não consegue reproduzir geometria

**Diagnóstico Específico:**
- Se TODOS os detalhes finos somem → Altura de camada ou resolução
- Se ALGUNS detalhes somem → Subexposição ou fatiamento
- Se detalhes aparecem mas deformados → Overexposure ou bleeding""",
        "solucao_imediata": """🛠 SOLUÇÃO IMEDIATA:

1. **Reduzir Altura de Camada** (Ação Prioritária)
   - Use 0.025mm ou 0.03mm para detalhes finos
   - Regra: Altura ≤ Menor detalhe ÷ 3
   - Exemplo: Detalhe 0.3mm → Use camada 0.1mm ou menos

2. **Aumentar Exposição em 10-15%**
   - Detalhes finos precisam de mais luz
   - Teste: +0.3s se usa 2.5s
   - Não exagere ou terá bleeding

3. **Orientar Peça Corretamente**
   - Detalhes finos perpendiculares às camadas
   - Evite detalhes paralelos às camadas
   - Incline 15-30° se necessário""",
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:

**1. CÁLCULO DE RESOLUÇÃO MÍNIMA NECESSÁRIA**

Fórmula da Resolução Efetiva:
```
Resolução XY = Tamanho do Pixel do LCD
Resolução Z = Altura de Camada

Detalhe Mínimo Reproduzível:
- XY: 3 × Pixel Size
- Z: 2 × Layer Height

Exemplo (Elegoo Mars 3 Pro):
- Pixel: 35 microns (0.035mm)
- Detalhe mínimo XY: 0.105mm
- Com camada 0.05mm: Detalhe mínimo Z: 0.1mm
```

**2. MATRIZ DE CONFIGURAÇÃO POR TAMANHO DE DETALHE**

| Tamanho do Detalhe | Altura Camada | Exposição | Anti-Aliasing |
|--------------------|---------------|-----------|---------------|
| > 1.0mm | 0.05mm | Normal | Nível 4 |
| 0.5-1.0mm | 0.03mm | +10% | Nível 6 |
| 0.3-0.5mm | 0.025mm | +15% | Nível 8 |
| < 0.3mm | 0.02mm | +20% | Nível 8 |

**3. CONFIGURAÇÃO AVANÇADA DE ANTI-ALIASING**

No Chitubox/Lychee:
```
Anti-Aliasing Nível 8:
- Suaviza bordas
- Melhora detalhes diagonais
- Aumenta tempo de fatiamento
- ESSENCIAL para detalhes finos!

Configuração:
1. Abra slicer
2. Vá em Settings → Anti-Aliasing
3. Selecione nível 8 (máximo)
4. Ative "Gray Scale"
```

**4. TESTE DE RESOLUÇÃO (AMERALABS TOWN)**

Baixe e imprima o modelo "Ameralabs Town":
```
1. Baixe STL gratuito
2. Fatie com suas configurações
3. Imprima
4. Analise com lupa:
   - Letras pequenas legíveis? → Resolução OK
   - Texturas visíveis? → Exposição OK
   - Bordas suaves? → Anti-aliasing OK
```

**5. OTIMIZAÇÃO DE MODELO 3D**

Antes de fatiar:
```
1. Verifique resolução do modelo:
   - Abra no Meshmixer ou Blender
   - Conte número de polígonos
   - Detalhes finos precisam de alta densidade

2. Remesh se necessário:
   - Use "Remesh" com densidade alta
   - Alvo: 500k-1M polígonos para peças detalhadas

3. Verifique espessura mínima:
   - Detalhes < 0.3mm podem não imprimir
   - Use ferramenta "Thickness Analysis"
```

**6. CONFIGURAÇÕES ESPECÍFICAS POR TIPO DE DETALHE**

A) Texturas Superficiais:
```
- Altura camada: 0.025mm
- Exposição: +15%
- Anti-aliasing: Nível 8
- Orientação: Textura perpendicular às camadas
```

B) Letras Pequenas:
```
- Altura camada: 0.03mm
- Exposição: +10%
- Anti-aliasing: Nível 6
- Profundidade mínima: 0.5mm
- Largura mínima: 0.3mm
```

C) Detalhes Mecânicos (engrenagens, roscas):
```
- Altura camada: 0.025mm
- Exposição: Normal (não aumentar!)
- Anti-aliasing: Nível 4
- Tolerância: +0.1mm em furos
```

**7. TÉCNICA DE EXPOSIÇÃO DUPLA**

Para detalhes MUITO finos:
```
1. Fatie com exposição normal
2. Edite arquivo .ctb/.pwma:
   - Camadas com detalhes: +20% exposição
   - Camadas sem detalhes: Exposição normal
3. Isso preserva detalhes sem overexposure geral
```

**8. ANÁLISE DE BLEEDING (SANGRAMENTO DE LUZ)**

Bleeding destrói detalhes finos:
```
Teste de Bleeding:
1. Imprima quadrado vazado 10×10mm, parede 0.5mm
2. Meça espessura da parede
3. Se > 0.6mm → Bleeding presente

Solução:
- Reduzir exposição em 10%
- Limpar LCD (manchas causam bleeding)
- Verificar FEP (arranhões espalham luz)
```

**9. CONFIGURAÇÃO DE SUPORTES PARA DETALHES FINOS**

Suportes podem destruir detalhes:
```
Configuração Ideal:
- Tip Diameter: 0.2mm (mínimo)
- Contact Depth: 0.3mm (raso)
- Densidade: Baixa em áreas detalhadas
- Alternativa: Imprimir sem suportes se possível
```

**10. DICA DE OURO: PÓS-PROCESSAMENTO**

Se detalhes ainda não aparecem:
```
1. Após lavagem, cure parcialmente (50%)
2. Use pincel fino com resina líquida
3. "Pinte" detalhes que faltam
4. Cure novamente com UV
5. Resultado: Detalhes restaurados manualmente
```

**11. CHECKLIST DE DETALHES FINOS**

Antes de imprimir peça detalhada:
- ✅ Altura camada ≤ 0.03mm?
- ✅ Anti-aliasing nível 6+?
- ✅ Modelo 3D com alta resolução?
- ✅ Detalhes perpendiculares às camadas?
- ✅ Exposição +10-15%?
- ✅ LCD limpo e sem manchas?
- ✅ FEP sem arranhões?
- ✅ Teste de bleeding realizado?

**12. TABELA DE REFERÊNCIA RÁPIDA**

| Problema | Solução |
|----------|---------|
| Detalhes somem completamente | Reduzir altura camada |
| Detalhes borrados | Reduzir exposição (bleeding) |
| Detalhes deformados | Aumentar anti-aliasing |
| Detalhes frágeis | Aumentar exposição +10% |
| Detalhes em diagonal ruins | Anti-aliasing nível 8 |"""
    }
}

# ============================================================================
# CATEGORIA 4: PROBLEMAS DE SUPORTES E PÓS-PROCESSAMENTO
# ============================================================================

CATEGORIA_4_SUPORTES_POS_PROCESSAMENTO = {
    "support_failure": {
        "nome": "Suportes falham ou quebram (Support Failure)",
        "sintomas": [
            "Suportes se soltam durante impressão",
            "Peça cai no tanque",
            "Suportes quebram ao remover",
            "Marcas profundas onde suportes tocam"
        ],
        "diagnostico": """🔍 DIAGNÓSTICO PRIMÁRIO:
Falha de suportes é um dos problemas mais comuns e frustrantes. Causas principais:

1. **Suportes Subdimensionados** (60% dos casos)
   - Diâmetro muito fino para peso da peça
   - Densidade insuficiente
   - Pontos de contato muito pequenos

2. **Orientação Inadequada da Peça** (25% dos casos)
   - Ângulos muito agressivos (> 45°)
   - Áreas grandes sem suporte
   - Forças de sucção muito altas

3. **Configuração de Impressão Errada** (10% dos casos)
   - Lift speed muito rápido
   - Subexposição (suportes frágeis)
   - Força de separação excessiva

4. **Problemas de Geração Automática** (5% dos casos)
   - Algoritmo não detecta áreas críticas
   - Suportes em locais errados

**Diagnóstico Específico:**
- Se suportes quebram DURANTE impressão → Subdimensionados ou lift speed alto
- Se quebram ao REMOVER → Overexposure ou contato muito profundo
- Se peça cai mas suportes ficam → Contato insuficiente""",
        "solucao_imediata": """🛠 SOLUÇÃO IMEDIATA:

1. **Aumentar Diâmetro dos Suportes** (Ação Prioritária)
   - Tip: 0.4mm → 0.5mm
   - Middle: 1.5mm → 2.0mm
   - Base: 3.0mm → 4.0mm
   - Suportes mais grossos = mais resistentes

2. **Aumentar Densidade de Suportes**
   - Adicione 50-100% mais suportes
   - Foque em áreas grandes e overhangs
   - Regra: 1 suporte a cada 5-8mm

3. **Reduzir Lift Speed**
   - De 80mm/min para 50mm/min
   - Isso reduz stress nos suportes
   - Especialmente importante para peças pesadas""",
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:

**1. CÁLCULO DE DIMENSIONAMENTO DE SUPORTES**

Fórmula de Carga por Suporte:
```
Carga = (Peso da Peça × Fator de Segurança) ÷ Número de Suportes

Fator de Segurança: 3-5× (recomendado: 4×)

Exemplo:
- Peça: 50g
- Fator: 4×
- Carga total: 200g
- 20 suportes → 10g por suporte

Diâmetro necessário:
- < 5g: 0.3mm
- 5-10g: 0.4mm
- 10-20g: 0.5mm
- > 20g: 0.6mm ou mais
```

**2. MATRIZ DE CONFIGURAÇÃO DE SUPORTES**

| Peso da Peça | Tip Ø | Middle Ø | Base Ø | Densidade |
|--------------|-------|----------|--------|-----------|
| < 20g | 0.3mm | 1.2mm | 2.5mm | 1/10mm |
| 20-50g | 0.4mm | 1.5mm | 3.0mm | 1/8mm |
| 50-100g | 0.5mm | 2.0mm | 4.0mm | 1/6mm |
| > 100g | 0.6mm | 2.5mm | 5.0mm | 1/5mm |

**3. TÉCNICA DE SUPORTES EM CAMADAS**

Para peças grandes:
```
Camada 1 (Base): Suportes grossos (0.6mm)
- Suportam peso principal
- Espaçamento: 5-8mm

Camada 2 (Meio): Suportes médios (0.4mm)
- Estabilizam geometria
- Espaçamento: 8-10mm

Camada 3 (Topo): Suportes finos (0.3mm)
- Detalhes e overhangs
- Espaçamento: 10-12mm
```

**4. ANÁLISE DE ILHAS E OVERHANGS**

No slicer:
```
1. Ative "Show Islands" (Chitubox)
2. Identifique áreas vermelhas (sem suporte)
3. Adicione suportes manualmente:
   - Ilhas grandes: 3-5 suportes
   - Ilhas pequenas: 1-2 suportes
   - Overhangs > 45°: Suporte a cada 5mm
```

**5. CONFIGURAÇÃO DE CONTATO**

Parâmetros críticos:
```
Contact Depth: 0.4-0.6mm
- Muito raso (< 0.3mm): Suporte solta
- Muito profundo (> 0.8mm): Marca na peça

Contact Diameter: 0.3-0.5mm
- Muito fino: Quebra fácil
- Muito grosso: Marca grande

Recomendação Quanton3D:
- PYROBLAST: 0.5mm depth, 0.4mm diameter
- FLEXFORM: 0.4mm depth, 0.3mm diameter
- IRON 7030: 0.6mm depth, 0.5mm diameter
```

**6. TÉCNICA DE ORIENTAÇÃO OTIMIZADA**

Regras de ouro:
```
1. Incline peça 15-30° para reduzir sucção
2. Coloque face maior para cima
3. Evite overhangs > 45° sem suporte
4. Distribua peso uniformemente
5. Minimize área de contato por camada
```

Ferramenta de análise:
```
Use "Overhang Analysis" no slicer:
- Verde: OK sem suporte
- Amarelo: Suporte recomendado
- Vermelho: Suporte obrigatório
```

**7. SUPORTES PARA GEOMETRIAS ESPECÍFICAS**

A) Cilindros Horizontais:
```
- Suportes ao longo de toda extensão
- Espaçamento: 5mm
- Diâmetro: 0.5mm
- Adicione suporte extra no meio
```

B) Esferas:
```
- Suportes radiais (como raios de roda)
- Mínimo 8 suportes
- Evite suportes no "equador"
```

C) Paredes Finas:
```
- Suportes alternados (zigue-zague)
- Evite suportes alinhados
- Diâmetro fino: 0.3mm
```

**8. CONFIGURAÇÃO AVANÇADA DE LIFT**

Para evitar quebra de suportes:
```
Lift Distance: 6-8mm
- Muito baixo: Sucção excessiva
- Muito alto: Tempo desperdiçado

Lift Speed: 40-60 mm/min
- Fase 1 (0-2mm): 30 mm/min (lento)
- Fase 2 (2-6mm): 60 mm/min (rápido)
- Fase 3 (6-8mm): 40 mm/min (desacelera)

Retract Speed: 120-150 mm/min
- Pode ser mais rápido que lift
```

**9. TESTE DE RESISTÊNCIA DE SUPORTES**

Antes de imprimir peça grande:
```
1. Imprima apenas os suportes (sem peça)
2. Deixe curar completamente
3. Teste resistência manualmente
4. Se quebrar fácil → Aumentar diâmetro
```

**10. REMOÇÃO SEGURA DE SUPORTES**

Técnica profissional:
```
1. Deixe peça curar 100% antes de remover
2. Use alicate de corte diagonal
3. Corte suporte próximo à base (não na peça)
4. Torça levemente antes de puxar
5. Lixe marcas com lixa 400-600

Ferramentas recomendadas:
- Alicate de corte flush (Xuron 410)
- Alicate de ponta fina
- Lixa d'água 400, 600, 800
- Dremel com broca esférica (opcional)
```

**11. SUPORTES SOLÚVEIS (TÉCNICA AVANÇADA)**

Para peças muito detalhadas:
```
1. Use resina solúvel em água para suportes
2. Imprima peça com resina normal
3. Imprima suportes com resina solúvel
4. Após cura, dissolva suportes em água
5. Resultado: Zero marcas!

Resinas solúveis compatíveis:
- Aqua Wash (Elegoo)
- Water Washable (Anycubic)
```

**12. DICA DE OURO: SUPORTES CUSTOMIZADOS**

Para áreas críticas:
```
1. Gere suportes automáticos
2. Delete suportes em área crítica
3. Adicione suportes manuais:
   - Tipo: "Tree" ou "Cone"
   - Posição: Estratégica
   - Diâmetro: Customizado
4. Resultado: Suporte perfeito onde precisa
```

**13. CHECKLIST PRÉ-IMPRESSÃO**

Antes de iniciar:
- ✅ Peça orientada 15-30°?
- ✅ Overhangs > 45° suportados?
- ✅ Ilhas identificadas e suportadas?
- ✅ Densidade de suportes adequada?
- ✅ Diâmetro de suportes calculado?
- ✅ Lift speed ≤ 60 mm/min?
- ✅ Contact depth 0.4-0.6mm?
- ✅ Teste de resistência feito?

**14. TROUBLESHOOTING RÁPIDO**

| Sintoma | Causa Provável | Solução |
|---------|----------------|---------|
| Suporte quebra durante impressão | Subdimensionado | +0.1mm diâmetro |
| Peça cai mas suporte fica | Contato insuficiente | +0.2mm depth |
| Suporte deixa marca grande | Contato muito profundo | -0.2mm depth |
| Suporte quebra ao remover | Overcure | Reduzir exposição 10% |
| Múltiplos suportes quebram | Lift speed alto | Reduzir para 40mm/min |"""
    },
    
    "post_cure_brittleness": {
        "nome": "Peça fica quebradiça após cura UV (Post-Cure Issues)",
        "sintomas": [
            "Peça quebra facilmente após cura",
            "Superfície amarelada ou esbranquiçada",
            "Peça perde flexibilidade",
            "Rachaduras aparecem após cura"
        ],
        "diagnostico": """🔍 DIAGNÓSTICO PRIMÁRIO:
Peças quebradiças após cura UV indicam overcure (cura excessiva) ou degradação. Causas principais:

1. **Overcure (Cura Excessiva)** (70% dos casos)
   - Tempo de cura UV muito longo
   - Potência UV muito alta
   - Distância muito próxima da fonte UV
   - Resultado: Resina "queima" e fica frágil

2. **Exposição ao Calor** (20% dos casos)
   - Cura UV gera calor excessivo
   - Temperatura > 60°C degrada resina
   - Especialmente em câmaras UV fechadas

3. **Resina Inadequada** (5% dos casos)
   - Resina não projetada para alta cura
   - Resina vencida ou degradada
   - Mistura de resinas incompatíveis

4. **Lavagem Inadequada** (5% dos casos)
   - IPA residual na peça
   - IPA reage com UV causando degradação

**Diagnóstico Específico:**
- Se peça amarela/branca → Overcure ou calor excessivo
- Se quebra imediatamente → Overcure severo
- Se rachaduras aparecem depois → Stress interno por overcure""",
        "solucao_imediata": """🛠 SOLUÇÃO IMEDIATA:

1. **Reduzir Tempo de Cura** (Ação Prioritária)
   - Use 50-70% do tempo atual
   - Exemplo: Se cura 10min, teste 5-7min
   - Regra: Menos é mais!

2. **Curar em Água**
   - Coloque peça em recipiente com água
   - Água absorve calor e distribui UV
   - Previne superaquecimento
   - Tempo: 60-80% do tempo normal

3. **Verificar Lavagem**
   - Lave novamente com IPA limpo
   - Seque completamente antes de curar
   - IPA residual + UV = Degradação""",
        "protocolo_avancado": """⚙ PROTOCOLO AVANÇADO:

**1. TABELA DE TEMPOS DE CURA OTIMIZADOS**

Para Câmara UV 405nm (36W):

| Resina Quanton3D | Tempo Mínimo | Tempo Ideal | Tempo Máximo |
|------------------|--------------|-------------|--------------|
| PYROBLAST | 3min | 5min | 8min |
| IRON 7030 | 4min | 6min | 10min |
| IRON | 4min | 6min | 10min |
| FLEXFORM | 2min | 3min | 5min |
| POSEIDON | 3min | 5min | 8min |
| SPARK | 3min | 4min | 6min |
| ALCHEMIST | 4min | 6min | 10min |

**IMPORTANTE:** Estes tempos são para cura TOTAL. Nunca exceda o tempo máximo!

**2. TÉCNICA DE CURA EM ÁGUA**

Protocolo profissional:
```
1. Prepare recipiente transparente com água
2. Adicione 2-3 gotas de detergente neutro
3. Coloque peça totalmente submersa
4. Posicione sob luz UV
5. Cure por 60-80% do tempo normal
6. Seque peça com ar comprimido

Vantagens:
- Temperatura controlada (< 30°C)
- Cura mais uniforme
- Zero risco de overcure
- Superfície mais lisa
```

**3. TESTE DE CURA PROGRESSIVA**

Para encontrar tempo ideal:
```
1. Imprima 5 peças idênticas pequenas
2. Cure cada uma por tempo diferente:
   - Peça A: 2min
   - Peça B: 4min
   - Peça C: 6min
   - Peça D: 8min
   - Peça E: 10min

3. Teste resistência:
   - Tente quebrar manualmente
   - Observe cor (amarelamento)
   - Verifique flexibilidade

4. Escolha tempo que dá:
   - Boa resistência
   - Sem amarelamento
   - Flexibilidade adequada
```

**4. ANÁLISE DE TEMPERATURA DURANTE CURA**

Use termômetro infravermelho:
```
Temperaturas seguras:
- < 40°C: Ideal
- 40-50°C: Aceitável
- 50-60°C: Limite
- > 60°C: PERIGO! Reduzir tempo

Solução se muito quente:
- Adicione ventilador
- Cure em intervalos (2min ON, 1min OFF)
- Use cura em água
```

**5. PROTOCOLO DE CURA EM ETAPAS**

Para peças grandes ou críticas:
```
Etapa 1 - Pré-Cura (30%):
- Tempo: 2-3 minutos
- Objetivo: Solidificar superfície
- Peça ainda flexível

Etapa 2 - Espera (Resfriamento):
- Tempo: 5-10 minutos
- Deixe peça esfriar naturalmente
- Não toque!

Etapa 3 - Cura Final (70%):
- Tempo: 3-5 minutos
- Objetivo: Cura completa
- Peça atinge propriedades finais

Total: 10-18 minutos (com intervalos)
Resultado: Cura perfeita sem overcure
```

**6. CONFIGURAÇÃO DE CÂMARA UV**

Parâmetros ideais:
```
Potência: 36-40W (405nm)
Distância: 10-15cm da peça
Reflexão: Espelhos ou papel alumínio
Ventilação: Obrigatória!
Rotação: Gire peça a cada 2min

DIY: Câmara UV Caseira
- Caixa de papelão forrada com alumínio
- Fita LED UV 405nm (5m, 36W)
- Ventilador de computador
- Custo: ~R$ 100
```

**7. TESTE DE OVERCURE**

Sinais de overcure:
```
Visual:
- Amarelamento (leve a severo)
- Esbranquiçamento
- Perda de translucidez
- Superfície opaca

Mecânico:
- Quebra com pouca força
- Som "seco" ao quebrar
- Fratura lisa e brilhante
- Perda total de flexibilidade

Químico:
- Cheiro forte de "queimado"
- Superfície pegajosa (degradação)
```

**8. RECUPERAÇÃO DE PEÇAS OVERCURED**

Se já curou demais:
```
Opção 1 - Recozimento:
1. Aqueça peça a 60°C por 30min
2. Deixe esfriar lentamente
3. Isso redistribui stress interno
4. Melhora resistência em 20-30%

Opção 2 - Revestimento:
1. Aplique camada fina de resina líquida
2. Cure levemente (1-2min)
3. Isso "sela" superfície degradada
4. Melhora aparência

Opção 3 - Aceitação:
- Se peça é decorativa: OK
- Se peça é funcional: Reimprimir
```

**9. CURA PARA RESINAS ESPECIAIS**

A) Resinas Flexíveis (FLEXFORM):
```
- Tempo: 50% do normal
- Método: SEMPRE em água
- Temperatura: < 35°C
- Teste: Deve manter flexibilidade
```

B) Resinas Duras (IRON 7030):
```
- Tempo: 100% do recomendado
- Método: Ar ou água
- Pós-cura: Forno 60°C por 1h (opcional)
- Resultado: Dureza máxima
```

C) Resinas Transparentes (POSEIDON):
```
- Tempo: 70% do normal
- Método: Água (obrigatório)
- Evitar: Overcure causa opacidade
- Polimento: Após cura
```

**10. DICA DE OURO: CURA SOLAR**

Método natural e eficaz:
```
1. Coloque peça em recipiente com água
2. Deixe ao sol por 15-30 minutos
3. Vire peça a cada 5 minutos
4. Resultado: Cura perfeita e gratuita!

Vantagens:
- Espectro UV completo
- Temperatura controlada (água)
- Custo zero
- Cura mais uniforme

Desvantagens:
- Depende do clima
- Tempo variável
```

**11. CHECKLIST DE CURA UV**

Antes de curar:
- ✅ Peça lavada e seca?
- ✅ IPA completamente evaporado?
- ✅ Tempo de cura calculado?
- ✅ Temperatura monitorada?
- ✅ Ventilação adequada?
- ✅ Recipiente com água preparado?
- ✅ Timer configurado?

**12. TROUBLESHOOTING RÁPIDO**

| Sintoma | Causa | Solução |
|---------|-------|---------|
| Amarelamento | Overcure | Reduzir tempo 30% |
| Quebra fácil | Overcure severo | Reduzir tempo 50% |
| Pegajosa após cura | Undercure ou IPA | Lavar novamente + curar mais |
| Rachaduras | Stress térmico | Curar em água |
| Perda de flexibilidade | Overcure | Reduzir tempo + água |
| Opacidade | Overcure | Curar em água + menos tempo |"""
    }
}

# ============================================================================
# FUNÇÃO DE BUSCA INTEGRADA
# ============================================================================

def buscar_erro_expandido(descricao_problema: str) -> dict:
    """
    Busca erro na base expandida do CONHECIMENTO(1).txt
    
    Args:
        descricao_problema: Descrição do problema relatado pelo usuário
    
    Returns:
        dict: Informações completas do erro com diagnóstico em 3 etapas
    """
    descricao_lower = descricao_problema.lower()
    
    # Busca em Categoria 3
    for erro_key, erro_data in CATEGORIA_3_DETALHE_RUPTURA_GEOMETRIA.items():
        if any(sintoma.lower() in descricao_lower for sintoma in erro_data["sintomas"]):
            return erro_data
    
    # Busca em Categoria 4
    for erro_key, erro_data in CATEGORIA_4_SUPORTES_POS_PROCESSAMENTO.items():
        if any(sintoma.lower() in descricao_lower for sintoma in erro_data["sintomas"]):
            return erro_data
    
    return None

# ============================================================================
# EXPORTAÇÃO
# ============================================================================

__all__ = [
    'CATEGORIA_3_DETALHE_RUPTURA_GEOMETRIA',
    'CATEGORIA_4_SUPORTES_POS_PROCESSAMENTO',
    'buscar_erro_expandido'
]

