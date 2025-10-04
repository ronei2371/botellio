#!/usr/bin/env python3
"""
Script de teste para validar o funcionamento do Botellio
"""
import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Testa se todos os módulos podem ser importados"""
    print("🔍 Testando importações...")
    
    try:
        from flask import Flask
        print("  ✅ Flask")
    except ImportError as e:
        print(f"  ❌ Flask: {e}")
        return False
    
    try:
        from config import get_config
        print("  ✅ Config")
    except ImportError as e:
        print(f"  ❌ Config: {e}")
        return False
    
    try:
        from database import init_db
        print("  ✅ Database")
    except ImportError as e:
        print(f"  ❌ Database: {e}")
        return False
    
    try:
        from services.ai_service import AIService
        print("  ✅ AI Service")
    except ImportError as e:
        print(f"  ❌ AI Service: {e}")
        return False
    
    try:
        from services.whatsapp_service import WhatsAppService
        print("  ✅ WhatsApp Service")
    except ImportError as e:
        print(f"  ❌ WhatsApp Service: {e}")
        return False
    
    try:
        from services.knowledge_base import KnowledgeBaseService
        print("  ✅ Knowledge Base")
    except ImportError as e:
        print(f"  ❌ Knowledge Base: {e}")
        return False
    
    return True

def test_config():
    """Testa se as configurações estão corretas"""
    print("\n⚙️  Testando configurações...")
    
    from config import get_config
    config = get_config()
    
    # Testa variáveis obrigatórias
    if not config.GROK_API_KEY or config.GROK_API_KEY == 'sua-chave-grok-aqui':
        print("  ⚠️  GROK_API_KEY não configurada")
    else:
        print("  ✅ GROK_API_KEY configurada")
    
    if not config.WHATSAPP_API_TOKEN or config.WHATSAPP_API_TOKEN == 'seu-token-whatsapp-aqui':
        print("  ⚠️  WHATSAPP_API_TOKEN não configurada")
    else:
        print("  ✅ WHATSAPP_API_TOKEN configurada")
    
    if not config.DATABASE_URL:
        print("  ⚠️  DATABASE_URL não configurada (OK para desenvolvimento)")
    else:
        print("  ✅ DATABASE_URL configurada")
    
    return True

def test_app_creation():
    """Testa se a aplicação pode ser criada"""
    print("\n🚀 Testando criação da aplicação...")
    
    try:
        from app import app
        print("  ✅ Aplicação criada com sucesso")
        
        # Testa rotas principais
        with app.test_client() as client:
            response = client.get('/')
            if response.status_code == 200:
                print("  ✅ Rota '/' funcionando")
            else:
                print(f"  ❌ Rota '/' retornou status {response.status_code}")
            
            response = client.get('/health')
            if response.status_code == 200:
                print("  ✅ Rota '/health' funcionando")
            else:
                print(f"  ❌ Rota '/health' retornou status {response.status_code}")
        
        return True
    except Exception as e:
        print(f"  ❌ Erro ao criar aplicação: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🤖 BOTELLIO - TESTES DE VALIDAÇÃO")
    print("=" * 60)
    
    success = True
    
    # Executa testes
    success = test_imports() and success
    success = test_config() and success
    success = test_app_creation() and success
    
    print("\n" + "=" * 60)
    if success:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("\nO Botellio está pronto para uso!")
        print("\nPara iniciar o servidor:")
        print("  python app.py")
    else:
        print("❌ ALGUNS TESTES FALHARAM")
        print("\nVerifique os erros acima e corrija antes de continuar.")
    print("=" * 60)
    
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())
