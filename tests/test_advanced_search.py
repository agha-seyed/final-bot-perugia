import pytest
from handlers.advanced_search_handler import load_search_data

def test_load_search_data():
    """Test loading search data."""
    data = load_search_data()
    assert "accommodations" in data
    assert "courses" in data
    assert len(data["accommodations"]) > 0
    assert len(data["courses"]) > 0