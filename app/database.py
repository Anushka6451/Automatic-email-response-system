import sqlite3

def save_email(sender, subject, category):
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        subject TEXT,
        category TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO emails (sender, subject, category) VALUES (?, ?, ?)",
        (sender, subject, category)
    )

    conn.commit()
    conn.close()