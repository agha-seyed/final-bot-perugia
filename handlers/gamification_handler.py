from aiogram import Router, types
from aiogram.filters import Command
from utils.gamification import add_points, get_total_points, add_badge, get_badges

router = Router()

@router.message(Command("points"))
async def show_points(message: types.Message):
    """Show the user's total points."""
    user_id = message.from_user.id
    total_points = get_total_points(user_id)
    await message.reply(f"You have {total_points} points!")

@router.message(Command("leaderboard"))
async def show_leaderboard(message: types.Message):
    """Show the leaderboard (top 10 users)."""
    conn = get_connection()
    rows = conn.execute("""
        SELECT user_id, SUM(points) AS total_points
        FROM points
        GROUP BY user_id
        ORDER BY total_points DESC
        LIMIT 10
    """).fetchall()
    
    leaderboard = "\n".join([f"{i+1}. User {row['user_id']}: {row['total_points']} points" for i, row in enumerate(rows)])
    await message.reply(f"🏆 Leaderboard:\n{leaderboard}")

@router.message(Command("badges"))
async def show_badges(message: types.Message):
    """Show the user's badges."""
    user_id = message.from_user.id
    badges = get_badges(user_id)
    if badges:
        await message.reply(f"You have the following badges:\n- " + "\n- ".join(badges))
    else:
        await message.reply("You have no badges yet.")