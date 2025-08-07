import pytest
from handlers.video_handler import load_videos

def test_load_videos():
    """Test loading videos data."""
    videos = load_videos()["videos"]
    assert len(videos) > 0
    assert "title" in videos[0]
    assert "url" in videos[0]