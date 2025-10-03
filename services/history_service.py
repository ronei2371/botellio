"""
Serviço para gerenciamento de histórico de conversas
"""
import logging
from database import db

logger = logging.getLogger(__name__)

class HistoryService:
    """Serviço para gerenciar o histórico de conversas dos usuários"""
    
    def __init__(self):
        """Inicializa o serviço de histórico"""
        self.memory_storage = {}  # Armazenamento em memória quando não há banco
        self.has_database = db is not None
        
        if not self.has_database:
            logger.warning("Banco de dados não configurado. Usando armazenamento em memória.")

    def get_user_by_phone(self, phone_number):
        """Busca um usuário pelo número de telefone."""
        if not self.has_database:
            return self.memory_storage.get(phone_number)
        
        from models import User
        return User.query.filter_by(phone_number=phone_number).first()

    def get_or_create_user(self, phone_number, name=None):
        """Obtém ou cria um novo usuário."""
        if not self.has_database:
            if phone_number not in self.memory_storage:
                self.memory_storage[phone_number] = {
                    'phone_number': phone_number,
                    'name': name,
                    'history': [],
                    'is_priority': False
                }
                logger.info(f"Novo usuário criado em memória: {phone_number}")
            elif name and not self.memory_storage[phone_number].get('name'):
                self.memory_storage[phone_number]['name'] = name
                logger.info(f"Nome do usuário {phone_number} atualizado para {name}")
            return self.memory_storage[phone_number]
        
        from models import User
        user = self.get_user_by_phone(phone_number)
        if not user:
            user = User(phone_number=phone_number, name=name)
            db.session.add(user)
            db.session.commit()
            logger.info(f"Novo usuário criado: {phone_number}")
        elif name and not user.name:
            user.name = name
            db.session.commit()
            logger.info(f"Nome do usuário {phone_number} atualizado para {name}")
        return user

    def add_message_to_history(self, user_id, message_content, message_type='user', **kwargs):
        """
        Adiciona uma nova mensagem ao histórico de um usuário.

        Args:
            user_id: ID ou número de telefone do usuário.
            message_content (str): Conteúdo da mensagem.
            message_type (str): Tipo da mensagem ('user', 'bot', 'system').
            **kwargs: Outros campos do modelo Conversation.
        """
        if not self.has_database:
            if user_id in self.memory_storage:
                self.memory_storage[user_id]['history'].append({
                    'content': message_content,
                    'type': message_type
                })
                logger.info(f"Mensagem de '{message_type}' adicionada ao histórico em memória")
            return None
        
        try:
            from models import Conversation
            message = Conversation(
                user_id=user_id,
                message_content=message_content,
                message_type=message_type,
                **kwargs
            )
            db.session.add(message)
            db.session.commit()
            logger.info(f"Mensagem de '{message_type}' adicionada ao histórico do usuário {user_id}")
            return message
        except Exception as e:
            db.session.rollback()
            logger.error(f"Erro ao adicionar mensagem ao histórico: {e}")
            raise

    def get_conversation_history(self, user_id, limit=20):
        """
        Retorna o histórico de conversas de um usuário.

        Args:
            user_id: ID ou número de telefone do usuário.
            limit (int): Número de mensagens a serem retornadas.

        Returns:
            list: Lista de mensagens.
        """
        if not self.has_database:
            if user_id in self.memory_storage:
                return self.memory_storage[user_id]['history'][-limit:]
            return []
        
        from models import Conversation
        history = Conversation.query.filter_by(user_id=user_id)\
            .order_by(Conversation.created_at.desc())\
            .limit(limit)\
            .all()
        
        # Inverte a lista para ter a ordem cronológica correta (mais antiga primeiro)
        return history[::-1]

    def get_context_for_ai(self, user_id, limit=10):
        """
        Prepara o histórico de conversas como contexto para a IA.

        Args:
            user_id: ID ou número de telefone do usuário.
            limit (int): Número de mensagens a serem usadas como contexto.

        Returns:
            list: Lista de dicionários no formato {"role": ..., "content": ...}.
        """
        history = self.get_conversation_history(user_id, limit)
        context = []
        
        if not self.has_database:
            for message in history:
                role = 'user' if message['type'] == 'user' else 'assistant'
                context.append({"role": role, "content": message['content']})
        else:
            for message in history:
                role = 'user' if message.message_type == 'user' else 'assistant'
                context.append({"role": role, "content": message.message_content})
        
        return context

    def update_user_priority(self, user_id, is_priority, client_type='quanton3d'):
        """
        Atualiza o status de prioridade de um usuário.
        """
        if not self.has_database:
            if user_id in self.memory_storage:
                self.memory_storage[user_id]['is_priority'] = is_priority
                self.memory_storage[user_id]['client_type'] = client_type
                logger.info(f"Prioridade do usuário {user_id} atualizada para {is_priority}")
            return None
        
        from models import User
        user = User.query.get(user_id)
        if user:
            user.is_priority = is_priority
            user.client_type = client_type
            db.session.commit()
            logger.info(f"Prioridade do usuário {user_id} atualizada para {is_priority}")
        return user

