from services.calendar_service import get_available_slots, add_appointment

def process_whatsapp_message(message: str) -> str:
    """
    Processa i messaggi WhatsApp per verificare disponibilità appuntamenti.
    """
    try:
        # Esempio di messaggio: "Appuntamento 2024-06-20 14:00"
        if message.startswith("Appuntamento"):
            _, date, time = message.split()
            available = get_available_slots(date, time)
            
            if available:
                add_appointment(date, time, status='booked')
                return f"✅ Appuntamento confermato per il {date} alle {time}."
            else:
                return f"❌ L'orario {time} del {date} non è disponibile. Scegli un altro orario."
        
        return "⚠️ Messaggio non riconosciuto. Scrivi 'Appuntamento AAAA-MM-GG HH:MM'"
    
    except Exception as e:
        return f"Errore nella gestione del messaggio: {str(e)}"
