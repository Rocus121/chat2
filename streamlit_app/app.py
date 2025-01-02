import streamlit as st
from services.whatsapp_service import connect_whatsapp_number, verify_whatsapp_number
from services.calendar_service import get_available_slots

st.title("📲 Servizio di Gestione Appuntamenti WhatsApp")

# Sezione di registrazione numero WhatsApp
st.header("🔗 Collega il Tuo Numero WhatsApp")
phone_number = st.text_input("Inserisci il tuo numero WhatsApp", placeholder="+1234567890")

if st.button("Registra Numero"):
    if phone_number:
        success = connect_whatsapp_number(phone_number)
        if success:
            st.success("Numero collegato con successo!")
        else:
            st.error("Errore nel collegare il numero.")
    else:
        st.warning("Per favore, inserisci un numero valido.")

# Sezione verifica stato numero
st.header("✅ Verifica Stato Numero WhatsApp")
verify_phone = st.text_input("Verifica un numero WhatsApp", placeholder="+1234567890")

if st.button("Verifica Numero"):
    if verify_phone:
        connected = verify_whatsapp_number(verify_phone)
        if connected:
            st.success(f"Il numero {verify_phone} è connesso correttamente.")
        else:
            st.error(f"Il numero {verify_phone} non è connesso.")
    else:
        st.warning("Inserisci un numero valido.")

# Sezione disponibilità calendario
st.header("📅 Verifica Disponibilità Appuntamenti")
date = st.date_input("Seleziona una data")
time = st.time_input("Seleziona un orario")

if st.button("Controlla Disponibilità"):
    if date and time:
        availability = get_available_slots(str(date), str(time))
        if availability:
            st.success("L'orario è disponibile per un appuntamento.")
        else:
            st.error("L'orario non è disponibile, scegli un altro momento.")
    else:
        st.warning("Seleziona data e orario validi.")
