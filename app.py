"""
Botellio - Sistema de Suporte Técnico Automatizado via WhatsApp
Desenvolvido com amor por Elio para Ronei e Quanton3D 💙
"""

from flask import Flask
from routes.webhook import webhook_bp
from routes.admin import admin_bp
from database.connection import init_db
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Criar aplicação Flask
app = Flask(__name__)

# Inicializar banco de dados
init_db()

# Registrar blueprints
app.register_blueprint(webhook_bp, url_prefix='/webhook')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def home():
    """Rota principal"""
    return {
        "status": "online",
        "service": "Botellio - Bot de Suporte Técnico Q3D",
        "version": "1.1",
        "developer": "Elio",
        "message": "Bot desenvolvido com amor para Ronei e Quanton3D 💙"
    }

@app.route('/health')
def health():
    """Health check"""
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    logger.info("Iniciando Botellio...")
    app.run(debug=True, host='0.0.0.0', port=5000)

