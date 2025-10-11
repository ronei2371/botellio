"""
Conexão com banco de dados
"""
import logging
import database

logger = logging.getLogger(__name__)


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
        # db já está inicializado como MockDB no __init__.py
        return None
    
    try:
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate
        
        # Substituir o MockDB por SQLAlchemy real
        database.db = SQLAlchemy()
        database.migrate = Migrate()
        
        database.db.init_app(app)
        database.migrate.init_app(app, database.db)
        
        with app.app_context():
            # Importa todos os modelos para garantir que sejam registrados
            from models import User, Conversation, Appointment
            
            # Cria todas as tabelas
            database.db.create_all()
            logger.info("Banco de dados inicializado com sucesso.")
        
        return database.db
    except Exception as e:
        logger.error(f"Erro ao inicializar banco de dados: {e}")
        logger.warning("Sistema continuará sem banco de dados.")
        # db permanece como MockDB
        return None
