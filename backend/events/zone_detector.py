from events.zones import ZONES


def get_zone(x, y):

    for zone_name, (x1, y1, x2, y2) in ZONES.items():

        if x1 <= x <= x2 and y1 <= y <= y2:

            return zone_name

    return "UNKNOWN"