import json

def check_availability(phone_number: str) -> str:
    """
    Controlla la disponibilità nel calendario.
    """
    calendar = DATABASE.get(phone_number, {}).get("calendar", {})
    if calendar:
        available_slots = calendar.get("available_slots", [])
        if available_slots:
            return f"Orari disponibili: {', '.join(available_slots)}"
    return "Nessuna disponibilità trovata."
