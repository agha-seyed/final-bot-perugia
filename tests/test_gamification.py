import pytest
from utils.gamification import add_points, get_total_points, add_badge, get_badges

def test_add_points():
    """Test adding points."""
    user_id = 123
    add_points(user_id, 10, "Test Reason")
    total_points = get_total_points(user_id)
    assert total_points == 10

def test_add_badge():
    """Test awarding a badge."""
    user_id = 123
    badge = "Test Badge"
    add_badge(user_id, badge)
    badges = get_badges(user_id)
    assert badge in badges