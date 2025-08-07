from utils.db_utils import get_connection
from datetime import datetime

def add_quest(title: str, description: str, reward_points: int, frequency: str):
    """Add a new quest."""
    conn = get_connection()
    with conn:
        conn.execute("""
            INSERT INTO quests (title, description, reward_points, frequency)
            VALUES (?, ?, ?, ?) 
        """, (title, description, reward_points, frequency))

def get_active_quests():
    """Retrieve active quests."""
    conn = get_connection()
    return conn.execute("SELECT * FROM quests WHERE active = 1").fetchall()

def complete_quest(user_id: int, quest_id: int):
    """Mark a quest as completed for a user."""
    conn = get_connection()
    with conn:
        conn.execute("""
            INSERT OR REPLACE INTO user_quests (user_id, quest_id, completed, completion_date)
            VALUES (?, ?, TRUE, ?)
        """, (user_id, quest_id, datetime.now()))

def get_user_level(user_id: int):
    """Get the user's current level and experience."""
    conn = get_connection()
    row = conn.execute("""
        SELECT level, experience, next_level_exp FROM user_levels WHERE user_id = ?
    """, (user_id,)).fetchone()
    
    if not row:
        # Initialize user level if not exists
        conn.execute("""
            INSERT INTO user_levels (user_id) VALUES (?) 
        """, (user_id,))
        return {"level": 1, "experience": 0, "next_level_exp": 100}
    
    return {"level": row["level"], "experience": row["experience"], "next_level_exp": row["next_level_exp"]}

def add_experience(user_id: int, exp: int):
    """Add experience points to a user."""
    conn = get_connection()
    user_data = get_user_level(user_id)
    new_exp = user_data["experience"] + exp
    next_exp = user_data["next_level_exp"]
    level_up = False
    
    if new_exp >= next_exp:
        level_up = True
        new_exp -= next_exp
        next_exp = int(next_exp * 1.5)  # Increase next level requirement
    
    with conn:
        conn.execute("""
            UPDATE user_levels 
            SET experience = ?, next_level_exp = ?, level = level + 1
            WHERE user_id = ?
        """, (new_exp, next_exp, user_id)) if level_up else conn.execute("""
            UPDATE user_levels 
            SET experience = ?
            WHERE user_id = ?
        """, (new_exp, user_id))
    
    return level_up