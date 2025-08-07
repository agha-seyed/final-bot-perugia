from flask import Blueprint, render_template
from utils.db_utils import get_connection

analytics_bp = Blueprint("analytics", __name__, template_folder="templates")

@analytics_bp.route("/analytics")
def analytics_dashboard():
    """Render the analytics dashboard."""
    conn = get_connection()
    daily_users = conn.execute("SELECT * FROM daily_active_users ORDER BY date DESC LIMIT 7").fetchall()
    popular_commands = conn.execute("""
        SELECT command, COUNT(*) as count FROM user_interactions
        GROUP BY command ORDER BY count DESC LIMIT 5
    """).fetchall()
    
    return render_template("analytics.html", daily_users=daily_users, popular_commands=popular_commands)