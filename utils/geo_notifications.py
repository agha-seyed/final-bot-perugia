import json

def load_geo_notifications():
    """Load geo-specific notifications from a JSON file."""
    with open("geo_notifications.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_notification_for_location(location: str):
    """Retrieve the notification for a specific location."""
    data = load_geo_notifications()["regions"]
    for region in data:
        if region["location"].lower() == location.lower():
            return region["message"]
    return None