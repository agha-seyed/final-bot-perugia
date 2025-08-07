from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot

scheduler = AsyncIOScheduler()

def schedule_time_notification(bot: Bot, user_id: int, message: str, notify_time: datetime):
    """Schedule a time-based notification."""
    scheduler.add_job(
        bot.send_message,
        trigger="date",
        run_date=notify_time,
        args=[user_id, message],
        id=f"notify_{user_id}_{notify_time.timestamp()}",
        replace_existing=True
    )
    scheduler.start()