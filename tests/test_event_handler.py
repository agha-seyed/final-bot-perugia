import pytest
from handlers.event_handler import load_events

def test_load_events():
    """Test loading events from JSON file."""
    events = load_events()
    assert len(events) > 0
    assert "title" in events[0]
    assert "date" in events[0]