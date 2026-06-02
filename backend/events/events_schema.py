from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    visitor_id: str
    event_type: str
    zone: str
    timestamp: str