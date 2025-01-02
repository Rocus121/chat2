import sqlite3

# Connessione al database
conn = sqlite3.connect("app.db", check_same_thread=False)
cursor = conn.cursor()

# Inizializzare la tabella appuntamenti
def init_calendar_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            status TEXT DEFAULT 'available'
        )
    ''')
    conn.commit()

# Ottenere disponibilità appuntamenti
def get_available_slots(date: str, time: str) -> bool:
    cursor.execute('''
        SELECT status FROM appointments WHERE date = ? AND time = ?
    ''', (date, time))
    result = cursor.fetchone()
    return result is None or result[0] == 'available'

# Aggiungere un appuntamento
def add_appointment(date: str, time: str, status: str = 'booked'):
    cursor.execute('''
        INSERT INTO appointments (date, time, status) VALUES (?, ?, ?)
    ''', (date, time, status))
    conn.commit()

# Inizializza il database calendario
init_calendar_db()

