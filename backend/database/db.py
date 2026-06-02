import os
import sqlite3

db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "store.db"
)

conn = sqlite3.connect(db_path)

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

print("Events table created successfully")