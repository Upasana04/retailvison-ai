from datetime import datetime

visitor_last_zone = {}

def generate_event(visitor_id, current_zone):

    events = []

    previous_zone = visitor_last_zone.get(visitor_id)

    if previous_zone is None:

        events.append({
            "visitor_id": str(visitor_id),
            "event_type": "ENTRY",
            "zone": current_zone,
            "timestamp": datetime.now().isoformat()
        })

    elif (
    previous_zone != current_zone
    and current_zone != "UNKNOWN"
):

        events.append({
            "visitor_id": str(visitor_id),
            "event_type": "ZONE_EXIT",
            "zone": previous_zone,
            "timestamp": datetime.now().isoformat()
        })

        events.append({
            "visitor_id": str(visitor_id),
            "event_type": "ZONE_ENTER",
            "zone": current_zone,
            "timestamp": datetime.now().isoformat()
        })

    visitor_last_zone[visitor_id] = current_zone

    return events