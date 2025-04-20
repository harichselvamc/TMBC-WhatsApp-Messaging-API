import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

def is_valid_phone(phone: str) -> bool:
    # Must start with country code, no '+' sign
    return re.fullmatch(r"\d{10,15}", phone) is not None

def send_whatsapp_message(phone_number: str) -> bool:
    url = f"https://graph.facebook.com/v18.0/{os.getenv('PHONE_NUMBER_ID')}/messages"
    headers = {
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": "Hello, this is a test message from our TMBC bot!"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    return response.status_code == 200
