"""
Pacote de modelos do Botellio
"""
# Importação condicional - só importa se o banco estiver configurado
try:
    from .user import User
    from .conversation import Conversation
    from .appointment import Appointment
    __all__ = ['User', 'Conversation', 'Appointment']
except Exception:
    # Se não houver banco configurado, define classes vazias
    User = None
    Conversation = None
    Appointment = None
    __all__ = []
