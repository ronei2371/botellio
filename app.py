"""
Botellio - Sistema de Suporte Técnico Automatizado via WhatsApp
Desenvolvido com amor por Elio para Ronei e Quanton3D 💙
"""

from flask import Flask, request, jsonify
import logging
import os

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Criar aplicação Flask
app = Flask(__name__)

# Carregar configurações
from config.settings import get_config
config_class = get_config()
app.config.from_object(config_class)

# Inicializar banco de dados (após configurar o app)
try:
    from database.connection import init_db
    init_db(app)
    logger.info("Banco de dados inicializado com sucesso")
except Exception as e:
    logger.warning(f"Banco de dados não inicializado: {e}")
    logger.info("Sistema continuará sem persistência de dados")

# Registrar blueprints
try:
    from routes.webhook import webhook_bp
    from routes.admin import admin_bp
    app.register_blueprint(webhook_bp, url_prefix='/webhook')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    logger.info("Blueprints registrados com sucesso")
except Exception as e:
    logger.error(f"Erro ao registrar blueprints: {e}")


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


@app.route('/webhook', methods=['GET', 'POST'])
def webhook_root():
    """
    Rota de webhook na raiz (sem /webhook prefix) para compatibilidade
    """
    if request.method == 'GET':
        # Verificação do webhook pelo WhatsApp
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        verify_token = app.config.get('VERIFY_TOKEN', os.getenv('VERIFY_TOKEN', 'botellio_quanton3d_2025'))
        
        logger.info(f"Verificação webhook recebida - Mode: {mode}, Token válido: {token == verify_token}")
        
        if mode == 'subscribe' and token == verify_token:
            logger.info("✅ Webhook verificado com sucesso!")
            return challenge, 200
        else:
            logger.warning("❌ Falha na verificação do webhook")
            return 'Forbidden', 403
    
    elif request.method == 'POST':
        # Receber mensagens do WhatsApp
        try:
            data = request.get_json()
            logger.info(f"📨 Webhook POST recebido: {data}")
            
            # Importar e processar mensagem
            from routes.webhook import receive_message
            return receive_message()
            
        except Exception as e:
            logger.error(f"❌ Erro ao processar webhook POST: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    logger.info("🚀 Iniciando Botellio...")
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

