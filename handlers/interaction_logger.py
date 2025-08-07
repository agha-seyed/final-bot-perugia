from aiogram import Router, types
from utils.analytics import log_user_interaction, update_daily_active_users

router = Router()

@router.message()
async def log_interaction(message: types.Message):
    """Log user interaction and update daily active users."""
    user_id = message.from_user.id
    command = message.text.split()[0]  # Extract the command (e.g., /start)
    log_user_interaction(user_id, command)
    update_daily_active_users(user_id)