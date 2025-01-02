# services/database.py

import sqlite3

# Connessione al database
conn = sqlite3.connect("app.db", check_same_thread=False)
cursor = conn.cursor()

# Creare la tabella per i numeri WhatsApp
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS whatsapp_numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT UNIQUE NOT NULL,
            connected BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()

# Aggiungere un numero WhatsApp
def save_whatsapp_number(phone_number: str, connected: bool = False):
    try:
        cursor.execute('''
            INSERT INTO whatsapp_numbers (phone_number, connected)
            VALUES (?, ?)
        ''', (phone_number, connected))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Il numero esiste già nel database.")
        return False

# Verificare se un numero esiste nel database
def check_whatsapp_number(phone_number: str):
    cursor.execute('''
        SELECT connected FROM whatsapp_numbers WHERE phone_number = ?
    ''', (phone_number,))
    result = cursor.fetchone()
    return result[0] if result else None

# Inizializzare il database all'avvio
init_db()
