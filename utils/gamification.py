from utils.db_utils import get_connection

def add_points(user_id: int, points: int, reason: str = None):
    """Add points for a user."""
    conn = get_connection()
    with conn:
        conn.execute(
            "INSERT INTO points (user_id, points, reason) VALUES (?, ?, ?)",
            (user_id, points, reason)
        )

def get_total_points(user_id: int):
    """Get total points for a user."""
    conn = get_connection()
    row = conn.execute(
        "SELECT SUM(points) AS total FROM points WHERE user_id = ?",
        (user_id,)
    ).fetchone()
    return row["total"] if row["total"] else 0

def add_badge(user_id: int, badge: str):
    """Award a badge to a user."""
    conn = get_connection()
    with conn:
        conn.execute(
            "INSERT INTO badges (user_id, badge) VALUES (?, ?)",
            (user_id, badge)
        )

def get_badges(user_id: int):
    """Get all badges for a user."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT badge FROM badges WHERE user_id = ?",
        (user_id,)
    ).fetchall()
    return [row["badge"] for row in rows]