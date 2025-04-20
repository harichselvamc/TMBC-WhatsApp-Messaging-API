from fastapi import FastAPI, Query, HTTPException
from dotenv import load_dotenv
from utils import send_whatsapp_message, is_valid_phone

load_dotenv()

app = FastAPI()

@app.get("/send_message")
async def send_message(phone_number: str = Query(..., example="919876543210")):
    if not is_valid_phone(phone_number):
        raise HTTPException(status_code=400, detail="Invalid phone number format. Use digits only, e.g., 919876543210")

    if send_whatsapp_message(phone_number):
        return {"status": "Message sent successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send message. Check API credentials or phone number.")
