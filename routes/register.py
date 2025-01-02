from fastapi import APIRouter
from services.whatsapp_service import send_whatsapp_message
import json

router = APIRouter()

# Simulazione database locale (JSON)
DATABASE = {}

@router.post("/register")
async def register_user(phone_number: str, calendar: dict):
    """
    Registra il numero di telefono e il calendario.
    """
    DATABASE[phone_number] = {"calendar": calendar, "status": "pending"}
    send_whatsapp_message(phone_number, "Registrazione completata. Rispondi 'OK' per confermare.")
    return {"message": "Registrazione in corso, attendere conferma."}
