"""
Configurações gerais do sistema Botellio
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configurações base"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    PORT = int(os.getenv('PORT', 8000))
    
    # Grok (xAI)
    GROK_API_KEY = os.getenv('GROK_API_KEY')
    GROK_MODEL = os.getenv('GROK_MODEL', 'grok-beta')
    
    # OpenAI (mantido como fallback)
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')
    
    # WhatsApp
    WHATSAPP_API_TOKEN = os.getenv('WHATSAPP_API_TOKEN')
    WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
    WHATSAPP_BUSINESS_ACCOUNT_ID = os.getenv('WHATSAPP_BUSINESS_ACCOUNT_ID')
    VERIFY_TOKEN = os.getenv('VERIFY_TOKEN', 'botellio-verify-token')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL')
    REDIS_URL = os.getenv('REDIS_URL')
    
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # AWS S3
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
    
    # Google Calendar
    GOOGLE_CALENDAR_API_KEY = os.getenv('GOOGLE_CALENDAR_API_KEY')
    GOOGLE_CALENDAR_ID = os.getenv('GOOGLE_CALENDAR_ID')
    
    # Sistema
    MAX_HISTORY_MESSAGES = 50  # Número máximo de mensagens no histórico
    RESPONSE_TIMEOUT = 30  # Timeout para respostas em segundos
    
    # Clientes prioritários
    PRIORITY_CLIENTS = ['quanton3d']  # Lista de identificadores de clientes prioritários


class DevelopmentConfig(Config):
    """Configurações de desenvolvimento"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configurações de produção"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Configurações de teste"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Seleciona a configuração baseada no ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Retorna a configuração apropriada baseada no ambiente"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])
