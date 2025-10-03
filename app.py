"""
Aplicação principal do Botellio - Sistema de Suporte Técnico Automatizado
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from config import get_config
from database import init_db
from routes.webhook import webhook_bp
from routes.admin import admin_bp

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Criar aplicação Flask
app = Flask(__name__)

# Carregar configurações
config_class = get_config()
app.config.from_object(config_class)

# Habilitar CORS
CORS(app)

# Inicializar banco de dados
init_db(app)

# Registrar blueprints (rotas)
app.register_blueprint(webhook_bp, url_prefix='/webhook')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def index():
    """Rota principal - informações sobre o sistema"""
    return jsonify({
        'nome': 'Botellio',
        'versao': '1.1',
        'descricao': 'Sistema de Suporte Técnico Automatizado para Impressoras 3D SLA',
        'status': 'online'
    })

@app.route('/health')
def health():
    """Endpoint de health check"""
    return jsonify({
        'status': 'healthy',
        'service': 'botellio'
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handler para erro 404"""
    return jsonify({'erro': 'Endpoint não encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler para erro 500"""
    logger.error(f"Erro interno: {error}")
    return jsonify({'erro': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    port = app.config.get('PORT', 8000)
    debug = app.config.get('FLASK_ENV') == 'development'
    
    logger.info(f"Iniciando Botellio na porta {port}...")
    app.run(host='0.0.0.0', port=port, debug=debug)
