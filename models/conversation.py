"""
Modelo de Conversa
"""
from datetime import datetime
from database.connection import db


class Conversation(db.Model):
    """Modelo de conversa/mensagem"""
    
    __tablename__ = 'conversations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    message_type = db.Column(db.String(20))  # 'user', 'bot', 'system'
    message_content = db.Column(db.Text, nullable=False)
    problem_type = db.Column(db.String(50))  # 'basic', 'intermediate', 'complex'
    problem_category = db.Column(db.String(100))  # categoria do problema
    resolution_status = db.Column(db.String(20))  # 'resolved', 'escalated', 'pending'
    media_url = db.Column(db.String(500))  # URL de mídia anexada
    media_type = db.Column(db.String(20))  # 'image', 'video', 'document'
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # Relacionamento
    user = db.relationship('User', back_populates='conversations')
    
    def __repr__(self):
        return f'<Conversation {self.id} - User {self.user_id}>'
    
    def to_dict(self):
        """Converte a conversa para dicionário"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message_type': self.message_type,
            'message_content': self.message_content,
            'problem_type': self.problem_type,
            'problem_category': self.problem_category,
            'resolution_status': self.resolution_status,
            'media_url': self.media_url,
            'media_type': self.media_type,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    @classmethod
    def create_message(cls, user_id, message_content, message_type='user', 
                      problem_type=None, problem_category=None, 
                      resolution_status=None, media_url=None, media_type=None):
        """Cria uma nova mensagem na conversa"""
        conversation = cls(
            user_id=user_id,
            message_content=message_content,
            message_type=message_type,
            problem_type=problem_type,
            problem_category=problem_category,
            resolution_status=resolution_status,
            media_url=media_url,
            media_type=media_type
        )
        db.session.add(conversation)
        db.session.commit()
        return conversation
    
    @classmethod
    def get_user_history(cls, user_id, limit=50):
        """Retorna o histórico de conversas de um usuário"""
        return cls.query.filter_by(user_id=user_id).order_by(
            cls.created_at.desc()
        ).limit(limit).all()
    
    @classmethod
    def get_context_for_ai(cls, user_id, limit=10):
        """Retorna o contexto das últimas mensagens para a IA"""
        messages = cls.query.filter_by(user_id=user_id).order_by(
            cls.created_at.desc()
        ).limit(limit).all()
        
        # Inverte para ordem cronológica
        messages.reverse()
        
        context = []
        for msg in messages:
            role = 'user' if msg.message_type == 'user' else 'assistant'
            context.append({
                'role': role,
                'content': msg.message_content
            })
        
        return context
    
    def update_resolution_status(self, status):
        """Atualiza o status de resolução"""
        self.resolution_status = status
        db.session.commit()
