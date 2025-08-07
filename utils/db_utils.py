import sqlite3
from config import SQLITE_DB

def get_connection():
    conn = sqlite3.connect(SQLITE_DB)
    conn.row_factory = sqlite3.Row
    return conn

def save_news(news):
    conn = get_connection()
    with conn:
        conn.execute(
            "INSERT INTO news (title, content, file, timestamp) VALUES (?, ?, ?, ?)",
            (news["title"], news["content"], news["file"], news["timestamp"])
        )