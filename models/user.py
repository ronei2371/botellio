"""
Modelo de Usuário
"""
from datetime import datetime
from database.connection import db


class User(db.Model):
    """Modelo de usuário do sistema"""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    name = db.Column(db.String(100))
    is_priority = db.Column(db.Boolean, default=False)  # Cliente Quanton3D
    client_type = db.Column(db.String(50))  # 'quanton3d', 'regular', etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_interaction = db.Column(db.DateTime)
    
    # Relacionamentos
    conversations = db.relationship('Conversation', back_populates='user', lazy='dynamic')
    appointments = db.relationship('Appointment', back_populates='user', lazy='dynamic')
    
    def __repr__(self):
        return f'<User {self.name} ({self.phone_number})>'
    
    def to_dict(self):
        """Converte o usuário para dicionário"""
        return {
            'id': self.id,
            'phone_number': self.phone_number,
            'name': self.name,
            'is_priority': self.is_priority,
            'client_type': self.client_type,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'last_interaction': self.last_interaction.isoformat() if self.last_interaction else None
        }
    
    @classmethod
    def get_or_create(cls, phone_number, name=None):
        """Obtém ou cria um usuário"""
        user = cls.query.filter_by(phone_number=phone_number).first()
        
        if not user:
            user = cls(phone_number=phone_number, name=name)
            db.session.add(user)
            db.session.commit()
        elif name and not user.name:
            user.name = name
            db.session.commit()
        
        return user
    
    def update_last_interaction(self):
        """Atualiza o timestamp da última interação"""
        self.last_interaction = datetime.utcnow()
        db.session.commit()
    
    def set_priority(self, is_priority=True, client_type='quanton3d'):
        """Define o usuário como prioritário"""
        self.is_priority = is_priority
        self.client_type = client_type
        db.session.commit()
    
    def get_conversation_history(self, limit=50):
        """Retorna o histórico de conversas do usuário"""
        return self.conversations.order_by(
            Conversation.created_at.desc()
        ).limit(limit).all()
