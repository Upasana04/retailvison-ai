from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os

app = FastAPI(
    title="RetailVision AI",
    description="Store Intelligence System",
    version="1.0"
)

# CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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



@app.get("/events")
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
        SELECT
            event_type,
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
        SELECT
            zone,
            COUNT(*)
        FROM events
        GROUP BY zone
    """)

    rows = cursor.fetchall()

    conn.close()

    return {
        "zone_activity": rows
    }


@app.get("/funnel")
def funnel():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE event_type='ENTRY'
    """)
    entries = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE zone='CASH_COUNTER'
    """)
    cash_counter = cursor.fetchone()[0]

    conn.close()

    conversion_rate = 0

    if entries > 0:
        conversion_rate = round(
            (cash_counter / entries) * 100,
            2
        )

    return {
        "entries": entries,
        "cash_counter_visitors": cash_counter,
        "conversion_rate": conversion_rate
    }


@app.get("/anomalies")
def anomalies():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            visitor_id,
            COUNT(*)
        FROM events
        GROUP BY visitor_id
        HAVING COUNT(*) > 5
    """)

    rows = cursor.fetchall()

    conn.close()

    return {
        "suspicious_visitors": rows
    }