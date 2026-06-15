import sqlite3

conn = sqlite3.connect(
    'database/chat_app.db'
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT
)
""")

conn.commit()

print("Database created")
