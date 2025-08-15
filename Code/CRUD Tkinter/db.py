import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gender TEXT,
    subscribed TEXT
)
""")
conn.commit()

def add_user(name, gender, subscribed):
    cursor.execute("INSERT INTO users (name, gender, subscribed) VALUES (?, ?, ?)",
                   (name, gender, subscribed))
    conn.commit()

def get_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

def update_user(user_id, name, gender, subscribed):
    cursor.execute("UPDATE users SET name = ?, gender = ?, subscribed = ? WHERE id = ?",
                   (name, gender, subscribed, user_id))
    conn.commit()

def close_db():
    conn.close()
