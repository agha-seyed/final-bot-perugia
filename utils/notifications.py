from redis import Redis
from aiogram import Bot
from utils.logger import logger

redis = Redis()

def set_user_preference(user_id: int, key: str, value: str):
    """Set a user preference in Redis."""
    redis.hset(f"user:{user_id}:prefs", key, value)
    logger.info(f"Set preference {key} = {value} for user {user_id}")

def get_user_preference(user_id: int, key: str):
    """Get a user preference from Redis."""
    return redis.hget(f"user:{user_id}:prefs", key)

async def send_custom_notification(bot: Bot, user_id: int, message: str):
    """Send a custom notification to a user."""
    user_lang = get_user_preference(user_id, "language") or "en"
    # Optionally localize the message based on user_lang
    await bot.send_message(user_id, message)
    logger.info(f"Sent notification to user {user_id}: {message}")