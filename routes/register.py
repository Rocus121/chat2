from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.whatsapp_service import connect_whatsapp_number

router = APIRouter()

# Modello per i dati di registrazione
class RegistrationData(BaseModel):
    phone_number: str
    calendar_type: str

# Endpoint per registrazione e configurazione del numero
@router.post("/register")
async def register_user(data: RegistrationData):
    phone_number = data.phone_number
    calendar_type = data.calendar_type
    
    if not phone_number or not calendar_type:
        raise HTTPException(status_code=400, detail="Numero di telefono e tipo di calendario sono obbligatori.")
    
    # Simula il collegamento al servizio WhatsApp
    success = connect_whatsapp_number(phone_number)
    
    if success:
        return {
            "message": f"Numero {phone_number} registrato e collegato correttamente.",
            "calendar_type": calendar_type
        }
    else:
        raise HTTPException(status_code=500, detail="Errore durante il collegamento con WhatsApp.")
