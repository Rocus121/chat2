# /routes/appuntamenti.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/appuntamenti/{giorno}/{ora}")
async def verifica_appuntamento(giorno: str, ora: str):
    return {
        "giorno": giorno,
        "ora": ora,
        "disponibile": False,
        "messaggio": "L'orario richiesto non è disponibile, ecco le alternative..."
    }
