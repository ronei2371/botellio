"""
Módulo de banco de dados
"""
import logging

logger = logging.getLogger(__name__)

# Mock do SQLAlchemy para quando não há banco de dados configurado
class MockDB:
    """Mock do SQLAlchemy para quando não há banco de dados"""
    Model = object
    Column = lambda *args, **kwargs: None
    Integer = None
    String = lambda *args: None
    Boolean = None
    DateTime = None
    Text = None
    ForeignKey = lambda *args: None
    relationship = lambda *args, **kwargs: None
    session = None
    
    class Query:
        def filter_by(self, **kwargs):
            return self
        def first(self):
            return None
        def all(self):
            return []
        def order_by(self, *args):
            return self
        def limit(self, n):
            return self
    
    query = Query()
    
    def __getattr__(self, name):
        return lambda *args, **kwargs: None

# Inicializar db com MockDB por padrão
db = MockDB()
migrate = None

# Importar função de inicialização
from .connection import init_db

__all__ = ['db', 'init_db']

