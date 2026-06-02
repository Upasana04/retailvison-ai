import sqlite3

conn = sqlite3.connect("store.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    visitor_id TEXT,
    event_type TEXT,
    zone TEXT,
    timestamp TEXT
)
""")

conn.commit()