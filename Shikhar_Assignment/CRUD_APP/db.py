import sqlite3
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Create the database path relative to this script
DB_NAME = os.path.join(BASE_DIR, "students.db")

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                faculty TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                subjects TEXT
            )
        """)
        conn.commit()
    except Exception as e:
        print("Database initialization error:", e)
    finally:
        if conn:
            conn.close()

def get_connection():
    return sqlite3.connect(DB_NAME)