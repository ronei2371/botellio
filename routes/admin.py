"""
Rotas administrativas para gerenciamento do sistema
"""
from flask import Blueprint, render_template, jsonify, request
import logging
from models import User, Conversation, Appointment
from database import db

logger = logging.getLogger(__name__)

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
def dashboard():
    """Dashboard administrativo"""
    try:
        # Estatísticas básicas
        total_users = User.query.count()
        total_conversations = Conversation.query.count()
        total_appointments = Appointment.query.count()
        priority_users = User.query.filter_by(is_priority=True).count()
        
        stats = {
            'total_usuarios': total_users,
            'total_conversas': total_conversations,
            'total_agendamentos': total_appointments,
            'clientes_prioritarios': priority_users
        }
        
        return jsonify(stats), 200
    
    except Exception as e:
        logger.error(f"Erro ao carregar dashboard: {e}")
        return jsonify({'erro': str(e)}), 500


@admin_bp.route('/users')
def list_users():
    """Lista todos os usuários"""
    try:
        users = User.query.all()
        users_data = [user.to_dict() for user in users]
        return jsonify(users_data), 200
    
    except Exception as e:
        logger.error(f"Erro ao listar usuários: {e}")
        return jsonify({'erro': str(e)}), 500


@admin_bp.route('/users/<int:user_id>')
def get_user(user_id):
    """Obtém detalhes de um usuário específico"""
    try:
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict()), 200
    
    except Exception as e:
        logger.error(f"Erro ao obter usuário: {e}")
        return jsonify({'erro': str(e)}), 500


@admin_bp.route('/users/<int:user_id>/history')
def get_user_history(user_id):
    """Obtém o histórico de conversas de um usuário"""
    try:
        limit = request.args.get('limit', 50, type=int)
        conversations = Conversation.query.filter_by(user_id=user_id)\
            .order_by(Conversation.created_at.desc())\
            .limit(limit)\
            .all()
        
        history = [conv.to_dict() for conv in conversations]
        return jsonify(history), 200
    
    except Exception as e:
        logger.error(f"Erro ao obter histórico: {e}")
        return jsonify({'erro': str(e)}), 500


@admin_bp.route('/users/<int:user_id>/priority', methods=['POST'])
def set_user_priority(user_id):
    """Define um usuário como prioritário"""
    try:
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        is_priority = data.get('is_priority', True)
        client_type = data.get('client_type', 'quanton3d')
        
        user.set_priority(is_priority, client_type)
        
        return jsonify({
            'mensagem': 'Prioridade atualizada com sucesso',
            'usuario': user.to_dict()
        }), 200
    
    except Exception as e:
        logger.error(f"Erro ao definir prioridade: {e}")
        return jsonify({'erro': str(e)}), 500


@admin_bp.route('/conversations')
def list_conversations():
    """Lista todas as conversas recentes"""
    try:
        limit = request.args.get('limit', 100, type=int)
        conversations = Conversation.query\
            .order_by(Conversation.created_at.desc())\
            .limit(limit)\
            .all()
        
        conversations_data = [conv.to_dict() for conv in conversations]
        return jsonify(conversations_data), 200
    
    except Exception as e:
        logger.error(f"Erro ao listar conversas: {e}")
        return jsonify({'erro': str(e)}), 500


@admin_bp.route('/appointments')
def list_appointments():
    """Lista todos os agendamentos"""
    try:
        appointments = Appointment.query\
            .order_by(Appointment.scheduled_date.desc())\
            .all()
        
        appointments_data = [appt.to_dict() for appt in appointments]
        return jsonify(appointments_data), 200
    
    except Exception as e:
        logger.error(f"Erro ao listar agendamentos: {e}")
        return jsonify({'erro': str(e)}), 500


@admin_bp.route('/stats')
def get_statistics():
    """Retorna estatísticas detalhadas do sistema"""
    try:
        # Conversas por tipo de problema
        basic_problems = Conversation.query.filter_by(problem_type='basic').count()
        intermediate_problems = Conversation.query.filter_by(problem_type='intermediate').count()
        complex_problems = Conversation.query.filter_by(problem_type='complex').count()
        
        # Conversas por status de resolução
        resolved = Conversation.query.filter_by(resolution_status='resolved').count()
        escalated = Conversation.query.filter_by(resolution_status='escalated').count()
        pending = Conversation.query.filter_by(resolution_status='pending').count()
        
        stats = {
            'problemas_por_tipo': {
                'basico': basic_problems,
                'intermediario': intermediate_problems,
                'complexo': complex_problems
            },
            'status_resolucao': {
                'resolvido': resolved,
                'escalado': escalated,
                'pendente': pending
            },
            'taxa_resolucao_automatica': round(
                (resolved / (resolved + escalated + pending) * 100) if (resolved + escalated + pending) > 0 else 0,
                2
            )
        }
        
        return jsonify(stats), 200
    
    except Exception as e:
        logger.error(f"Erro ao obter estatísticas: {e}")
        return jsonify({'erro': str(e)}), 500
