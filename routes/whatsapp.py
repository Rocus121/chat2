@router.post("/whatsapp/message")
async def whatsapp_message_handler(message: str):
    """
    Endpoint per processare i messaggi WhatsApp.
    """
    response = process_whatsapp_message(message)
    return {"response": response}
