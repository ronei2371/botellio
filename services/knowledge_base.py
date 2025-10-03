"""
Base de conhecimento técnico para impressão 3D SLA
"""

KNOWLEDGE_BASE = {
    "nivelamento_plataforma": {
        "titulo": "Nivelamento de Plataforma",
        "descricao": "Procedimento para nivelar corretamente a plataforma de impressão",
        "passos": [
            "1. Limpe completamente a plataforma e o tanque de resina",
            "2. Solte os parafusos de nivelamento da plataforma",
            "3. Posicione uma folha de papel A4 sobre a tela LCD",
            "4. Use o menu da impressora para mover a plataforma até a posição inicial (Z=0)",
            "5. Aperte os parafusos de nivelamento com a plataforma pressionando o papel",
            "6. Verifique se há resistência ao puxar o papel - deve estar firme mas não impossível de mover",
            "7. Teste com uma impressão de calibração"
        ],
        "dicas": [
            "Faça o nivelamento com a impressora em temperatura ambiente estável",
            "Repita o processo se a primeira camada não aderir corretamente",
            "Alguns modelos possuem nivelamento automático - consulte o manual"
        ]
    },
    "calibracao_resina": {
        "titulo": "Calibração de Resina",
        "descricao": "Como calibrar o tempo de exposição para diferentes resinas",
        "passos": [
            "1. Imprima um modelo de teste de calibração (Cones de Exposição)",
            "2. Use o tempo de exposição recomendado pelo fabricante como ponto de partida",
            "3. Observe os resultados: se subcurado, aumente o tempo; se supercurado, diminua",
            "4. Ajuste em incrementos de 0.5 a 1 segundo",
            "5. Repita até obter detalhes nítidos e boa adesão entre camadas"
        ],
        "parametros_iniciais": {
            "camada_base": "25-40 segundos",
            "camadas_normais": "6-12 segundos (varia por resina)",
            "altura_camada": "0.05mm (padrão para alta qualidade)"
        }
    },
    "problemas_adesao": {
        "titulo": "Problemas de Adesão",
        "descricao": "Soluções para peças que não aderem à plataforma",
        "causas_comuns": [
            "Plataforma mal nivelada",
            "Tempo de exposição das camadas base insuficiente",
            "Plataforma ou filme FEP sujos",
            "Temperatura ambiente muito baixa",
            "Resina vencida ou mal agitada"
        ],
        "solucoes": [
            "Refaça o nivelamento da plataforma",
            "Aumente o tempo de exposição das camadas base (30-50s)",
            "Limpe a plataforma com álcool isopropílico",
            "Aumente a temperatura ambiente para 20-25°C",
            "Agite bem a resina antes de usar",
            "Adicione mais suportes ou uma base (raft) ao modelo"
        ]
    },
    "camadas_descolando": {
        "titulo": "Camadas Descolando",
        "descricao": "Solução para delaminação entre camadas",
        "causas": [
            "Tempo de exposição muito curto",
            "Resina contaminada ou vencida",
            "Temperatura muito baixa durante impressão",
            "Agitação insuficiente da resina"
        ],
        "solucoes": [
            "Aumente o tempo de exposição em 1-2 segundos",
            "Use resina fresca e bem agitada",
            "Mantenha temperatura ambiente entre 20-25°C",
            "Filtre a resina para remover partículas curadas"
        ]
    },
    "limpeza_manutencao": {
        "titulo": "Limpeza e Manutenção Preventiva",
        "descricao": "Rotina de manutenção para impressoras SLA",
        "rotina_diaria": [
            "Limpe respingos de resina da impressora",
            "Verifique o nível de resina no tanque",
            "Inspecione visualmente o filme FEP"
        ],
        "rotina_semanal": [
            "Limpe completamente o tanque de resina",
            "Verifique o aperto dos parafusos da plataforma",
            "Limpe a tela LCD com pano de microfibra"
        ],
        "rotina_mensal": [
            "Lubrifique o eixo Z conforme manual",
            "Verifique e limpe o filtro de ar (se houver)",
            "Inspecione o filme FEP em busca de arranhões ou opacidade",
            "Faça um teste de calibração completo"
        ]
    },
    "chitubox_basico": {
        "titulo": "Configurações Básicas do Chitubox",
        "descricao": "Guia rápido para fatiamento no Chitubox",
        "configuracoes_recomendadas": {
            "altura_camada": "0.05mm (qualidade) ou 0.1mm (velocidade)",
            "camadas_base": "5-8 camadas",
            "tempo_exposicao_base": "30-40s",
            "tempo_exposicao_normal": "8-12s (depende da resina)",
            "velocidade_elevacao": "60-80 mm/min",
            "distancia_elevacao": "5-8mm"
        },
        "dicas_suporte": [
            "Use suporte automático como ponto de partida",
            "Adicione suportes manualmente em áreas críticas",
            "Evite suportes em superfícies visíveis",
            "Teste com densidade média (50-70%)"
        ]
    }
}


class KnowledgeBaseService:
    """Serviço para acessar a base de conhecimento"""
    
    def __init__(self):
        self.knowledge = KNOWLEDGE_BASE
    
    def get_solution(self, problem_key):
        """
        Retorna a solução para um problema específico
        
        Args:
            problem_key (str): Chave do problema na base de conhecimento
            
        Returns:
            dict: Informações sobre o problema e solução
        """
        return self.knowledge.get(problem_key)
    
    def search_knowledge(self, query):
        """
        Busca na base de conhecimento por palavras-chave
        
        Args:
            query (str): Termo de busca
            
        Returns:
            list: Lista de resultados relevantes
        """
        query_lower = query.lower()
        results = []
        
        for key, content in self.knowledge.items():
            # Busca no título e descrição
            if query_lower in content.get('titulo', '').lower() or \
               query_lower in content.get('descricao', '').lower():
                results.append({
                    'key': key,
                    'titulo': content.get('titulo'),
                    'descricao': content.get('descricao')
                })
        
        return results
    
    def get_all_topics(self):
        """Retorna todos os tópicos disponíveis na base de conhecimento"""
        return [
            {
                'key': key,
                'titulo': content.get('titulo'),
                'descricao': content.get('descricao')
            }
            for key, content in self.knowledge.items()
        ]
    
    def format_solution(self, problem_key):
        """
        Formata uma solução de forma legível para envio via WhatsApp
        
        Args:
            problem_key (str): Chave do problema
            
        Returns:
            str: Solução formatada
        """
        solution = self.get_solution(problem_key)
        
        if not solution:
            return "Desculpe, não encontrei informações sobre esse problema."
        
        formatted = f"*{solution['titulo']}*\n\n"
        formatted += f"{solution['descricao']}\n\n"
        
        if 'passos' in solution:
            formatted += "*Passos:*\n"
            for passo in solution['passos']:
                formatted += f"{passo}\n"
            formatted += "\n"
        
        if 'causas_comuns' in solution:
            formatted += "*Causas Comuns:*\n"
            for causa in solution['causas_comuns']:
                formatted += f"• {causa}\n"
            formatted += "\n"
        
        if 'solucoes' in solution:
            formatted += "*Soluções:*\n"
            for solucao in solution['solucoes']:
                formatted += f"• {solucao}\n"
            formatted += "\n"
        
        if 'dicas' in solution:
            formatted += "*Dicas:*\n"
            for dica in solution['dicas']:
                formatted += f"💡 {dica}\n"
        
        return formatted
