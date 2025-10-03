"""
Serviço de integração com WhatsApp Business API
"""
import requests
import logging
from config.settings import Config
from config.whatsapp_config import (
    WHATSAPP_API_BASE_URL,
    MESSAGE_TYPES,
    TIMEOUTS
)

logger = logging.getLogger(__name__)


class WhatsAppService:
    """Serviço para gerenciar comunicação com WhatsApp Business API"""
    
    def __init__(self):
        self.api_token = Config.WHATSAPP_API_TOKEN
        self.phone_number_id = Config.WHATSAPP_PHONE_NUMBER_ID
        self.base_url = f"{WHATSAPP_API_BASE_URL}/{self.phone_number_id}"
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
    
    def send_text_message(self, to_phone, message):
        """
        Envia uma mensagem de texto
        
        Args:
            to_phone (str): Número de telefone do destinatário
            message (str): Conteúdo da mensagem
            
        Returns:
            dict: Resposta da API
        """
        url = f"{self.base_url}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to_phone,
            "type": MESSAGE_TYPES['TEXT'],
            "text": {
                "preview_url": False,
                "body": message
            }
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=TIMEOUTS['MESSAGE_SEND']
            )
            response.raise_for_status()
            logger.info(f"Mensagem enviada para {to_phone}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar mensagem: {e}")
            raise
    
    def send_image_message(self, to_phone, image_url, caption=None):
        """
        Envia uma mensagem com imagem
        
        Args:
            to_phone (str): Número de telefone do destinatário
            image_url (str): URL da imagem
            caption (str): Legenda da imagem (opcional)
            
        Returns:
            dict: Resposta da API
        """
        url = f"{self.base_url}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to_phone,
            "type": MESSAGE_TYPES['IMAGE'],
            "image": {
                "link": image_url
            }
        }
        
        if caption:
            payload["image"]["caption"] = caption
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=TIMEOUTS['MESSAGE_SEND']
            )
            response.raise_for_status()
            logger.info(f"Imagem enviada para {to_phone}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar imagem: {e}")
            raise
    
    def send_document_message(self, to_phone, document_url, filename=None, caption=None):
        """
        Envia uma mensagem com documento
        
        Args:
            to_phone (str): Número de telefone do destinatário
            document_url (str): URL do documento
            filename (str): Nome do arquivo (opcional)
            caption (str): Legenda do documento (opcional)
            
        Returns:
            dict: Resposta da API
        """
        url = f"{self.base_url}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to_phone,
            "type": MESSAGE_TYPES['DOCUMENT'],
            "document": {
                "link": document_url
            }
        }
        
        if filename:
            payload["document"]["filename"] = filename
        if caption:
            payload["document"]["caption"] = caption
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=TIMEOUTS['MESSAGE_SEND']
            )
            response.raise_for_status()
            logger.info(f"Documento enviado para {to_phone}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar documento: {e}")
            raise
    
    def send_video_message(self, to_phone, video_url, caption=None):
        """
        Envia uma mensagem com vídeo
        
        Args:
            to_phone (str): Número de telefone do destinatário
            video_url (str): URL do vídeo
            caption (str): Legenda do vídeo (opcional)
            
        Returns:
            dict: Resposta da API
        """
        url = f"{self.base_url}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to_phone,
            "type": MESSAGE_TYPES['VIDEO'],
            "video": {
                "link": video_url
            }
        }
        
        if caption:
            payload["video"]["caption"] = caption
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=TIMEOUTS['MESSAGE_SEND']
            )
            response.raise_for_status()
            logger.info(f"Vídeo enviado para {to_phone}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar vídeo: {e}")
            raise
    
    def send_interactive_buttons(self, to_phone, body_text, buttons):
        """
        Envia uma mensagem com botões interativos
        
        Args:
            to_phone (str): Número de telefone do destinatário
            body_text (str): Texto do corpo da mensagem
            buttons (list): Lista de botões (máximo 3)
            
        Returns:
            dict: Resposta da API
        """
        url = f"{self.base_url}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to_phone,
            "type": MESSAGE_TYPES['INTERACTIVE'],
            "interactive": {
                "type": "button",
                "body": {
                    "text": body_text
                },
                "action": {
                    "buttons": buttons
                }
            }
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=TIMEOUTS['MESSAGE_SEND']
            )
            response.raise_for_status()
            logger.info(f"Mensagem interativa enviada para {to_phone}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar mensagem interativa: {e}")
            raise
    
    def mark_message_as_read(self, message_id):
        """
        Marca uma mensagem como lida
        
        Args:
            message_id (str): ID da mensagem
            
        Returns:
            dict: Resposta da API
        """
        url = f"{self.base_url}/messages"
        
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=TIMEOUTS['API_REQUEST']
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao marcar mensagem como lida: {e}")
            raise
    
    def get_media_url(self, media_id):
        """
        Obtém a URL de um arquivo de mídia
        
        Args:
            media_id (str): ID da mídia
            
        Returns:
            str: URL da mídia
        """
        url = f"{WHATSAPP_API_BASE_URL}/{media_id}"
        
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=TIMEOUTS['API_REQUEST']
            )
            response.raise_for_status()
            data = response.json()
            return data.get('url')
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao obter URL da mídia: {e}")
            raise
    
    def download_media(self, media_url):
        """
        Faz download de um arquivo de mídia
        
        Args:
            media_url (str): URL da mídia
            
        Returns:
            bytes: Conteúdo do arquivo
        """
        try:
            response = requests.get(
                media_url,
                headers=self.headers,
                timeout=TIMEOUTS['MEDIA_UPLOAD']
            )
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao fazer download da mídia: {e}")
            raise
