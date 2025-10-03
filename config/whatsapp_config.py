"""
Configurações específicas do WhatsApp Business API
"""

# URLs da API do WhatsApp
WHATSAPP_API_BASE_URL = "https://graph.facebook.com/v18.0"

# Tipos de mensagens suportados
MESSAGE_TYPES = {
    'TEXT': 'text',
    'IMAGE': 'image',
    'VIDEO': 'video',
    'DOCUMENT': 'document',
    'AUDIO': 'audio',
    'INTERACTIVE': 'interactive',
    'TEMPLATE': 'template'
}

# Templates de mensagens interativas
INTERACTIVE_BUTTONS = {
    'HISTORICO': {
        'type': 'button',
        'body': {
            'text': 'Como posso ajudá-lo hoje?'
        },
        'action': {
            'buttons': [
                {
                    'type': 'reply',
                    'reply': {
                        'id': 'historico',
                        'title': '📋 Histórico'
                    }
                },
                {
                    'type': 'reply',
                    'reply': {
                        'id': 'novo_problema',
                        'title': '🆕 Novo Problema'
                    }
                },
                {
                    'type': 'reply',
                    'reply': {
                        'id': 'agendar',
                        'title': '📅 Agendar Suporte'
                    }
                }
            ]
        }
    }
}

# Mensagens padrão do sistema
SYSTEM_MESSAGES = {
    'WELCOME': """Olá {name}! 👋

Sou o Botellio, seu assistente técnico especializado em impressoras 3D SLA da Quanton3D.

Estou aqui para ajudá-lo com:
• Problemas de impressão
• Calibração e configuração
• Manutenção preventiva
• Dúvidas técnicas

Como posso ajudá-lo hoje?""",
    
    'WELCOME_NEW': """Olá! 👋

Bem-vindo ao suporte técnico Quanton3D!

Sou o Botellio, seu assistente especializado em impressoras 3D SLA.

Para começar, por favor me diga seu nome.""",
    
    'ERROR': """Desculpe, ocorreu um erro ao processar sua mensagem. 😔

Por favor, tente novamente ou digite "ajuda" para ver as opções disponíveis.""",
    
    'PROCESSING': """Estou analisando sua solicitação... ⏳

Um momento, por favor.""",
    
    'ESCALATION': """Entendo que este problema requer atenção especializada. 🔧

Vou conectá-lo com nossa equipe de suporte técnico.

Gostaria de agendar uma chamada de vídeo?""",
    
    'FEEDBACK_REQUEST': """Consegui ajudá-lo com seu problema? 

Por favor, avalie o atendimento:
⭐ Excelente
⭐⭐ Bom
⭐⭐⭐ Regular
⭐⭐⭐⭐ Ruim"""
}

# Configurações de timeout
TIMEOUTS = {
    'MESSAGE_SEND': 10,  # segundos
    'MEDIA_UPLOAD': 30,  # segundos
    'API_REQUEST': 15  # segundos
}
