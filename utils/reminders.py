from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.notifications import send_custom_notification
from utils.logger import logger

scheduler = AsyncIOScheduler()

def schedule_reminder(bot, user_id: int, message: str, reminder_time):
    """Schedule a reminder for a user."""
    scheduler.add_job(
        send_custom_notification,
        trigger="date",
        run_date=reminder_time,
        args=[bot, user_id, message],
        id=f"reminder_{user_id}_{reminder_time}",
        replace_existing=True
    )
    logger.info(f"Scheduled reminder for user {user_id} at {reminder_time}: {message}")

def cancel_reminder(user_id: int, reminder_time):
    """Cancel a scheduled reminder."""
    job_id = f"reminder_{user_id}_{reminder_time}"
    if scheduler.get_job(job_id):
        scheduler.remove_job(job_id)
        logger.info(f"Canceled reminder for user {user_id} at {reminder_time}")