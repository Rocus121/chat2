import streamlit as st
import requests
import json

# Titolo della Dashboard
st.title("📲 Registrazione Numero e Calendario per Prenotazioni WhatsApp")

# Input per numero di telefono e calendario
phone_number = st.text_input("📱 Inserisci il tuo numero WhatsApp", placeholder="+123456789")
calendar_data = st.text_area("📅 Incolla i tuoi dati del calendario in formato JSON", height=200)

# Bottone di registrazione
if st.button("✅ Registra Numero e Calendario"):
    if phone_number and calendar_data:
        try:
            # Validazione del JSON
            calendar_json = json.loads(calendar_data)
            
            # Chiamata API al backend FastAPI
            response = requests.post(
                "http://127.0.0.1:8000/register",
                json={
                    "phone_number": phone_number,
                    "calendar": calendar_json
                },
                timeout=10  # Timeout per evitare blocchi
            )
            
            # Gestione della risposta dal backend
            if response.status_code == 200:
                st.success("✅ Registrazione completata. Attendi il messaggio di conferma su WhatsApp.")
            else:
                st.error(f"❌ Errore durante la registrazione: {response.status_code} - {response.text}")
        
        except json.JSONDecodeError:
            st.error("❌ Il formato del calendario non è valido JSON.")
        
        except requests.exceptions.ConnectionError:
            st.error("❌ Errore di connessione al server FastAPI. Assicurati che sia in esecuzione.")
        
        except requests.exceptions.Timeout:
            st.error("❌ Timeout della richiesta al server. Riprova più tardi.")
    
    else:
        st.warning("⚠️ Compila entrambi i campi: Numero di telefono e Calendario JSON.")

