from fastapi import APIRouter
from services.whatsapp_service import process_whatsapp_reply
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/whatsapp/message")
async def receive_whatsapp_message(data: dict):
    """
    Riceve un messaggio da WhatsApp.
    """
    phone_number = data.get("from")
    message = data.get("text")
    
    if phone_number and message:
        process_whatsapp_reply(phone_number, message)
        return JSONResponse(content={"message": "Messaggio elaborato."})
    return JSONResponse(content={"error": "Dati mancanti."}, status_code=400)
