# 🚀 Guia de Início Rápido - Botellio v1.1

## O que você tem?

Você tem em mãos o **Botellio v1.1**, um sistema completo de suporte técnico automatizado via WhatsApp para impressoras 3D SLA, agora usando o **Grok** (xAI) como motor de inteligência artificial!

## Primeiros Passos

### 1️⃣ Verificar o Python

Certifique-se de ter o **Python 3.11 ou superior** instalado no seu computador.

**Para verificar:**
```bash
python --version
```

Se não tiver, baixe em: https://www.python.org/downloads/

### 2️⃣ Abrir o Terminal na Pasta do Projeto

**Windows:**
- Abra a pasta `botellio` no Explorador de Arquivos
- Clique na barra de endereço e digite `cmd`
- Pressione Enter

**macOS/Linux:**
- Abra o Terminal
- Navegue até a pasta: `cd /caminho/para/botellio`

### 3️⃣ Criar Ambiente Virtual

Execute os seguintes comandos:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate
```

Você verá `(venv)` no início da linha do terminal quando estiver ativado.

### 4️⃣ Instalar as Dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

Isso vai instalar todas as bibliotecas necessárias. Pode demorar alguns minutos.

### 5️⃣ Configurar as Variáveis de Ambiente

1. Copie o arquivo `.env.example` e renomeie para `.env`
2. Abra o arquivo `.env` em um editor de texto
3. Preencha com suas chaves de API:

```env
# Grok (xAI) - Obtenha em: https://console.x.ai
GROK_API_KEY=xai-sua-chave-aqui
GROK_MODEL=grok-beta

# WhatsApp (obtenha no Meta for Developers)
WHATSAPP_API_TOKEN=seu-token-aqui
WHATSAPP_PHONE_NUMBER_ID=seu-id-aqui
WHATSAPP_BUSINESS_ACCOUNT_ID=seu-id-aqui
VERIFY_TOKEN=escolha-uma-senha-secreta

# Banco de Dados (deixe assim para desenvolvimento)
DATABASE_URL=sqlite:///botellio.db
REDIS_URL=redis://localhost:6379/0

# Configurações
FLASK_ENV=development
PORT=8000
SECRET_KEY=minha-chave-secreta-123
```

### 6️⃣ Executar o Botellio

Com tudo configurado, inicie o servidor:

```bash
python app.py
```

Você verá uma mensagem como:
```
INFO - Iniciando Botellio na porta 8000...
 * Running on http://127.0.0.1:8000
```

🎉 **Parabéns! O Botellio está rodando!**

## Próximos Passos

### Testar o Bot

1. Abra seu navegador (Chrome, Firefox, etc.)
2. Digite na barra de endereço: `http://127.0.0.1:8000`
3. Pressione Enter

Você deve ver uma mensagem JSON assim:
```json
{
  "nome": "Botellio",
  "versao": "1.1",
  "status": "online"
}
```

✅ Se viu isso, está tudo funcionando!

### Configurar o Webhook do WhatsApp

Para conectar com o WhatsApp:

1. **Instalar o ngrok** (para expor seu servidor local)
   - Baixe em: https://ngrok.com/download
   - Descompacte e execute: `ngrok http 8000`
   - Copie a URL HTTPS que aparecer

2. **Configurar no Meta for Developers:**
   - Vá em: https://developers.facebook.com
   - Configure o webhook com a URL do ngrok
   - Exemplo: `https://abc123.ngrok.io/webhook`

3. **Testar enviando uma mensagem** para o número do WhatsApp Business

## Comandos Úteis

```bash
# Ativar ambiente virtual
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Desativar ambiente virtual
deactivate

# Executar o servidor
python app.py

# Ver logs em tempo real
# Os logs aparecerão no terminal onde você executou o app.py
```

## ❓ Problemas Comuns

### "python não é reconhecido como comando"
**Solução:** Você precisa instalar o Python. Baixe em: https://www.python.org/downloads/

### "can't open file 'app.py'"
**Solução:** Você não está na pasta correta. Use `cd` para navegar até a pasta `botellio` onde estão os arquivos.

### "ModuleNotFoundError"
**Solução:** Certifique-se de que o ambiente virtual está ativado (deve ter `(venv)` no terminal) e execute:
```bash
pip install -r requirements.txt
```

### O terminal fechou sozinho
**Solução:** Abra novamente e repita os passos a partir do Passo 3 (ativar o ambiente virtual).

## 📋 O que você precisa ter:

✅ **Python 3.11+** instalado (se não tiver, baixe em python.org)
✅ **Chave do Grok** (crie conta em https://x.ai)
✅ **Conta no Meta for Developers** (para o WhatsApp Business API)

## 💡 Dica Importante

**Se você ver o erro "can't open file 'app.py'"**, significa que os arquivos não estão na pasta onde você está. Certifique-se de:

1. Ter descompactado o arquivo `botellio_v1.1.zip`
2. Estar dentro da pasta `botellio` (onde estão os arquivos `app.py`, `requirements.txt`, etc.)
3. Usar o comando `cd` para navegar até a pasta correta

---

**Desenvolvido com ❤️ para Quanton3D**  
**Versão:** 1.1 (com Grok)  
**Data:** 03 de Outubro de 2025
