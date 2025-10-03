"""
Pacote de rotas do Botellio
"""
from .webhook import webhook_bp
from .admin import admin_bp

__all__ = ['webhook_bp', 'admin_bp']
