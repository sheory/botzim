import os
import requests

from dotenv import load_dotenv
from spidermon import Action

load_dotenv()

WEBHOOK_ID = os.getenv("WEBHOOK_ID")
WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")

class DiscordNotification(Action):
    def run_action(self):
        response = {
            "test1": "sim",
            "test2": "sim",
            "erro": True,
        }
        data = {
            "content": get_message_discord(response)
        }
        url = f"https://discord.com/api/webhooks/{WEBHOOK_ID}/{WEBHOOK_TOKEN}"

        response = requests.post(url, json=data)
        return response

def get_message_discord(response):
    if response.get("erro"):
        message = f"❌ Comunicação finalizada\nErro: {response['erro']}"
    else:
        message = (
            "✅ Comunicação finalizada\n\n"
            "- Contratos\n"
            f"novos: {len(response['test1'])}\n"
            f"alterados: {len(response['test2'])}\n"
        )

    return message

DiscordNotification().run_action()
