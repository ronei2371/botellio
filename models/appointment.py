"""
Modelo de Agendamento
"""
from datetime import datetime
from database import db


class Appointment(db.Model):
    """Modelo de agendamento de suporte"""
    
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    scheduled_date = db.Column(db.DateTime, nullable=False, index=True)
    duration_minutes = db.Column(db.Integer, default=30)
    problem_description = db.Column(db.Text)
    status = db.Column(db.String(20), default='scheduled')  # 'scheduled', 'confirmed', 'completed', 'cancelled'
    meeting_url = db.Column(db.String(500))  # URL da chamada de vídeo
    google_calendar_event_id = db.Column(db.String(200))  # ID do evento no Google Calendar
    reminder_sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamento
    user = db.relationship('User', back_populates='appointments')
    
    def __repr__(self):
        return f'<Appointment {self.id} - User {self.user_id} at {self.scheduled_date}>'
    
    def to_dict(self):
        """Converte o agendamento para dicionário"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'scheduled_date': self.scheduled_date.isoformat() if self.scheduled_date else None,
            'duration_minutes': self.duration_minutes,
            'problem_description': self.problem_description,
            'status': self.status,
            'meeting_url': self.meeting_url,
            'google_calendar_event_id': self.google_calendar_event_id,
            'reminder_sent': self.reminder_sent,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def create_appointment(cls, user_id, scheduled_date, problem_description=None, 
                          duration_minutes=30, meeting_url=None):
        """Cria um novo agendamento"""
        appointment = cls(
            user_id=user_id,
            scheduled_date=scheduled_date,
            problem_description=problem_description,
            duration_minutes=duration_minutes,
            meeting_url=meeting_url
        )
        db.session.add(appointment)
        db.session.commit()
        return appointment
    
    @classmethod
    def get_user_appointments(cls, user_id, include_past=False):
        """Retorna os agendamentos de um usuário"""
        query = cls.query.filter_by(user_id=user_id)
        
        if not include_past:
            query = query.filter(cls.scheduled_date >= datetime.utcnow())
        
        return query.order_by(cls.scheduled_date.asc()).all()
    
    @classmethod
    def get_pending_reminders(cls):
        """Retorna agendamentos que precisam de lembrete"""
        # Agendamentos nas próximas 24 horas que ainda não tiveram lembrete
        from datetime import timedelta
        tomorrow = datetime.utcnow() + timedelta(days=1)
        
        return cls.query.filter(
            cls.scheduled_date <= tomorrow,
            cls.scheduled_date >= datetime.utcnow(),
            cls.reminder_sent == False,
            cls.status == 'scheduled'
        ).all()
    
    def confirm(self):
        """Confirma o agendamento"""
        self.status = 'confirmed'
        db.session.commit()
    
    def cancel(self):
        """Cancela o agendamento"""
        self.status = 'cancelled'
        db.session.commit()
    
    def complete(self):
        """Marca o agendamento como completo"""
        self.status = 'completed'
        db.session.commit()
    
    def mark_reminder_sent(self):
        """Marca que o lembrete foi enviado"""
        self.reminder_sent = True
        db.session.commit()
    
    def update_google_event_id(self, event_id):
        """Atualiza o ID do evento do Google Calendar"""
        self.google_calendar_event_id = event_id
        db.session.commit()
