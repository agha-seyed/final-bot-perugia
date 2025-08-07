import pytest
from handlers.podcast_handler import load_podcasts

def test_load_podcasts():
    """Test loading podcasts data."""
    podcasts = load_podcasts()["podcasts"]
    assert len(podcasts) > 0
    assert "title" in podcasts[0]
    assert "url" in podcasts[0]