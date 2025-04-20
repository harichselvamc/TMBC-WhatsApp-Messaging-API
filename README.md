# TMBC WhatsApp Messaging API (FastAPI)

This project is a hiring task for The Madras Branding Company (TMBC).
It demonstrates a FastAPI application that integrates with Meta's WhatsApp Cloud API to send a custom message to a given WhatsApp number.

GitHub Repository: https://github.com/harichselvamc/TMBC-WhatsApp-Messaging-API.git

## API Features

- /send_message endpoint
- Accepts phone_number as a query parameter
- Validates the phone number format
- Sends a custom text message via Meta WhatsApp API
- Implements proper error handling and logs
- Environment variable usage for secure token management

## Tech Stack

- Python
- FastAPI
- Meta WhatsApp Cloud API
- Uvicorn
- Dotenv

## Message Sent

Hello, this is a test message from our TMBC bot!


## Setup Instructions

1. Clone the repository
git clone https://github.com/harichselvamc/TMBC-WhatsApp-Messaging-API.git
cd TMBC-WhatsApp-Messaging-API

2. Create a .env file
ACCESS_TOKEN=your_meta_whatsapp_access_token
PHONE_NUMBER_ID=your_phone_number_id

3. Install dependencies
pip install -r requirements.txt

4. Run the FastAPI server
uvicorn main:app --reload

## How to Use

Send a GET request to:
http://localhost:8000/send_message?phone_number=919876543210

Replace the number with the recipient's phone number (in international format without +)

Make sure the number is added in Meta sandbox or has recently interacted with your business

## Example Response

{
  "status": "Message sent successfully"
}
