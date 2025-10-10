# 🤖 Botellio v1.1

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

**Sistema de Suporte Técnico Automatizado para Impressoras 3D SLA via WhatsApp**

## 🎯 Sobre o Botellio

O Botellio é um assistente inteligente que automatiza o atendimento ao cliente para empresas de impressão 3D SLA, com foco especial em clientes Quanton3D. Utilizando inteligência artificial avançada (Grok AI), o bot oferece suporte técnico 24/7 através do WhatsApp, classificando problemas e fornecendo soluções precisas.

### Funcionalidades Principais

- ✅ Atendimento automatizado via WhatsApp Business API
- ✅ Suporte técnico especializado para impressoras 3D SLA/DLP
- ✅ Análise de imagens com IA (Grok Vision)
- ✅ Base de conhecimento com 9 resinas Quanton3D
- ✅ Suporte para 20+ modelos de impressoras
- ✅ Histórico completo de conversas
- ✅ Diagnóstico estruturado em 3 etapas
- ✅ Triagem inteligente de problemas
- ✅ Priorização de clientes Quanton3D
- ✅ Funciona com ou sem banco de dados

## 🚀 Tecnologias

- **Backend**: Python 3.11+ com Flask
- **IA**: Grok-4 (xAI)
- **Banco de Dados**: PostgreSQL (produção)
- **Deploy**: Render.com
- **Mensageria**: WhatsApp Business API

## 📋 Requisitos

- Python 3.11 ou superior
- Conta no Grok (xAI)
- Conta no WhatsApp Business
- PostgreSQL (apenas para produção)

## 🔧 Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/botellio.git
cd botellio
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Grok AI
GROK_API_KEY=sua_chave_aqui
GROK_MODEL=grok-beta

# WhatsApp Business
WHATSAPP_API_TOKEN=seu_token_aqui
WHATSAPP_PHONE_NUMBER_ID=seu_phone_id_aqui
WHATSAPP_BUSINESS_ACCOUNT_ID=seu_account_id_aqui
VERIFY_TOKEN=seu_verify_token_aqui

# Configurações
FLASK_ENV=development
PORT=8000
```

### 6. Execute o bot

```bash
python app.py
```

O bot estará disponível em `http://localhost:8000`

## 🌐 Deploy no Render.com

### Variáveis de Ambiente Necessárias

Configure estas variáveis no Render:

- `GROK_API_KEY`: Sua chave da API do Grok
- `GROK_MODEL`: `grok-beta`
- `WHATSAPP_API_TOKEN`: Token da API do WhatsApp
- `WHATSAPP_PHONE_NUMBER_ID`: ID do número do WhatsApp
- `WHATSAPP_BUSINESS_ACCOUNT_ID`: ID da conta business
- `VERIFY_TOKEN`: Token de verificação do webhook
- `DATABASE_URL`: (Será criado automaticamente pelo Render)

### Comandos de Deploy

- **Build Command**: `pip install -r requirements-production.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`

## 📁 Estrutura do Projeto

```
botellio/
├── app.py                      # Aplicação principal
├── requirements.txt            # Dependências (desenvolvimento)
├── requirements-production.txt # Dependências (produção)
├── .env                        # Variáveis de ambiente (local)
├── config/                     # Configurações
├── models/                     # Modelos de dados
├── services/                   # Serviços (IA, WhatsApp, etc)
├── routes/                     # Rotas da API
├── database/                   # Conexão com banco
└── utils/                      # Utilitários
```

## 🔐 Segurança

- Nunca commite o arquivo `.env` no Git
- Mantenha suas chaves de API seguras
- Use tokens de verificação fortes para webhooks
- Configure CORS adequadamente para produção

## 📞 Suporte

Para dúvidas ou problemas, entre em contato com a equipe Quanton3D.

## 📄 Licença

© 2025 Quanton3D - Todos os direitos reservados

---

**Desenvolvido com ❤️ para a Quanton3D**
