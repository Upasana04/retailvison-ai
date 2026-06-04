import os
import sqlite3
import json

def save_event(event):

    db_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "store.db"
    )

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO events(
            visitor_id,
            event_type,
            zone,
            timestamp
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            event["visitor_id"],
            event["event_type"],
            event["zone"],
            event["timestamp"]
        )
    )

    conn.commit()
    conn.close()

    # Save event to JSONL file
    jsonl_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "events.jsonl"
    )

    with open(jsonl_path, "a") as f:
        f.write(json.dumps(event) + "\n")