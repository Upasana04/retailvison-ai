from fastapi import FastAPI
import sqlite3
import os

app = FastAPI(
    title="RetailVision AI",
    description="Store Intelligence System",
    version="1.0"
)

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "store.db"
)


@app.get("/")
def home():
    return {
        "message": "RetailVision AI API Running"
    }


@app.get("/events")
@app.get("/metrics")
def get_metrics():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
    """)
    total_visitors = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM events
        WHERE event_type='ENTRY'
    """)
    total_entries = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM events
        WHERE event_type='ZONE_ENTER'
    """)
    zone_transitions = cursor.fetchone()[0]

    conn.close()

    return {
        "total_visitors": total_visitors,
        "entries": total_entries,
        "zone_transitions": zone_transitions
    }
def get_events():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            visitor_id,
            event_type,
            zone,
            timestamp
        FROM events
        ORDER BY id DESC
        LIMIT 100
    """)

    rows = cursor.fetchall()

    conn.close()

    return {
        "count": len(rows),
        "events": rows
    }
@app.get("/visitor/{visitor_id}")
def visitor_journey(visitor_id: str):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT event_type,
               zone,
               timestamp
        FROM events
        WHERE visitor_id = ?
        ORDER BY id
    """, (visitor_id,))

    rows = cursor.fetchall()

    conn.close()

    return {
        "visitor_id": visitor_id,
        "journey": rows
    }
@app.get("/heatmap")
def heatmap():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT zone,
               COUNT(*)
        FROM events
        GROUP BY zone
    """)

    rows = cursor.fetchall()

    conn.close()

    return {
        "zone_activity": rows
    }