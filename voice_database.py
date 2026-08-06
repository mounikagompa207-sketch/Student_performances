import sqlite3
from utils.voice_engine import get_voice_response

def create_voice_table():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS voice_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            question TEXT,

            answer TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()

    conn.close()