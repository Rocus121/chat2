import sys
import os

# Aggiunge la directory principale al percorso dei moduli Python
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
import uvicorn  
from routes import whatsapp, appuntamenti

# Istanza principale di FastAPI
app = FastAPI()

# Endpoint di test principale
@app.get("/")
async def read_root():
    return {"message": "Ciao, il tuo chatbot è pronto!"}

# Includere le route
app.include_router(appuntamenti.router)
app.include_router(whatsapp.router)

# Avvia il server solo se il file viene eseguito direttamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
