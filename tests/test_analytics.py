import pytest
from utils.analytics import log_user_interaction, update_daily_active_users
from utils.db_utils import get_connection

def test_log_user_interaction():
    """Test logging user interaction."""
    log_user_interaction(123, "/start")
    conn = get_connection()
    row = conn.execute("SELECT * FROM user_interactions WHERE user_id = 123").fetchone()
    assert row["command"] == "/start"

def test_update_daily_active_users():
    """Test updating daily active users."""
    update_daily_active_users(123)
    conn = get_connection()
    row = conn.execute("SELECT * FROM daily_active_users ORDER BY date DESC LIMIT 1").fetchone()
    assert row["active_users"] > 0