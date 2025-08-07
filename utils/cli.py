@app.command()
def add_points_cli(user_id: int, points: int, reason: str = None):
    """Add points to a user via CLI."""
    from utils.gamification import add_points
    add_points(user_id, points, reason)
    typer.echo(f"Added {points} points to user {user_id} for reason: {reason}")

@app.command()
def add_badge_cli(user_id: int, badge: str):
    """Award a badge to a user via CLI."""
    from utils.gamification import add_badge
    add_badge(user_id, badge)
    typer.echo(f"Awarded badge '{badge}' to user {user_id}")