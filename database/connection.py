"""
Conexão com banco de dados
"""
import logging

logger = logging.getLogger(__name__)

# Variável para armazenar a instância do banco (None se não configurado)
db = None
migrate = None


def init_db(app):
    """
    Inicializa o banco de dados com a aplicação Flask
    
    Nota: Em desenvolvimento, o banco de dados é opcional.
    Se DATABASE_URL não estiver configurado, o sistema funcionará
    sem persistência de dados (apenas em memória).
    """
    database_url = app.config.get('DATABASE_URL')
    
    if not database_url:
        logger.warning("DATABASE_URL não configurado. Sistema rodando sem banco de dados.")
        logger.warning("Os dados não serão persistidos entre reinicializações.")
        return None
    
    try:
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate
        
        global db, migrate
        db = SQLAlchemy()
        migrate = Migrate()
        
        db.init_app(app)
        migrate.init_app(app, db)
        
        with app.app_context():
            # Importa todos os modelos para garantir que sejam registrados
            from models import User, Conversation, Appointment
            
            # Cria todas as tabelas
            db.create_all()
            logger.info("Banco de dados inicializado com sucesso.")
        
        return db
    except Exception as e:
        logger.error(f"Erro ao inicializar banco de dados: {e}")
        logger.warning("Sistema continuará sem banco de dados.")
        return None
