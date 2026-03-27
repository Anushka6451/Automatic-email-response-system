import sqlite3

def init_db():
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        subject TEXT,
        body TEXT,
        category TEXT,
        response TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_email(sender, subject, body, category, response):
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO emails (sender, subject, body, category, response)
    VALUES (?, ?, ?, ?, ?)
    """, (sender, subject, body, category, response))

    conn.commit()
    conn.close()