import requests
from app.config import N8N_WEBHOOK_URL

def enviar_a_n8n(data):
    try:
        response = requests.post(N8N_WEBHOOK_URL, json=data)
        print(f"n8n response: {response.status_code}")
    except Exception as e:
        print("Error enviando a n8n:", e)
