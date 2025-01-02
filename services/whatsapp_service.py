import requests

# Simulazione database locale (JSON)
DATABASE = {}

def send_whatsapp_message(phone_number: str, message: str) -> bool:
    """
    Invia un messaggio WhatsApp.
    """
    try:
        response = requests.post(
            "https://graph.facebook.com/v17.0/YOUR_PHONE_ID/messages",
            headers={
                "Authorization": "Bearer YOUR_ACCESS_TOKEN",
                "Content-Type": "application/json"
            },
            json={
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "text",
                "text": {"body": message}
            }
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Errore WhatsApp: {e}")
        return False

def process_whatsapp_reply(phone_number: str, message: str):
    """
    Elabora la risposta dell'utente su WhatsApp.
    """
    if phone_number in DATABASE and DATABASE[phone_number]["status"] == "pending":
        if message.strip().lower() == "ok":
            DATABASE[phone_number]["status"] = "confirmed"
            send_whatsapp_message(phone_number, "Conferma ricevuta. Il tuo numero è attivo per le prenotazioni.")


from services.calendar_service import check_availability

def process_whatsapp_reply(phone_number: str, message: str):
    if phone_number in DATABASE:
        if DATABASE[phone_number]["status"] == "confirmed":
            response = check_availability(phone_number)
            send_whatsapp_message(phone_number, response)
