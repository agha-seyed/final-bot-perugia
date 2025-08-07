def create_analytics_tables():
    conn = get_connection()
    with conn:
        # User Interaction Logs
        conn.execute("""
            CREATE TABLE IF NOT EXISTS user_interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                command TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Daily Active Users
        conn.execute("""
            CREATE TABLE IF NOT EXISTS daily_active_users (
                date DATE PRIMARY KEY,
                active_users INTEGER DEFAULT 0
            )
        """)