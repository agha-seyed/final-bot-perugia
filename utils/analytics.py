from utils.db_utils import get_connection
from datetime import datetime

def log_user_interaction(user_id: int, command: str):
    """Log a user's interaction with the bot."""
    conn = get_connection()
    with conn:
        conn.execute("""
            INSERT INTO user_interactions (user_id, command)
            VALUES (?, ?)
        """, (user_id, command))

def update_daily_active_users(user_id: int):
    """Update the daily active users count."""
    conn = get_connection()
    today = datetime.now().date()
    with conn:
        # Check if the user has already interacted today
        already_active = conn.execute("""
            SELECT 1 FROM user_interactions
            WHERE user_id = ? AND DATE(timestamp) = ?
        """, (user_id, today)).fetchone()

        if not already_active:
            # Update daily active users count
            conn.execute("""
                INSERT INTO daily_active_users (date, active_users)
                VALUES (?, 1)
                ON CONFLICT(date) DO UPDATE SET active_users = active_users + 1
            """, (today,))