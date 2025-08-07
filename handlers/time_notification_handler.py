from aiogram import Router, types
from utils.time_notifications.py import schedule_time_notification
from datetime import datetime, timedelta

router = Router()

@router.message(Command("set_reminder"))
async def set_reminder(message: types.Message):
    """Set a time-based reminder."""
    try:
        user_message = message.text.split(maxsplit=2)  # Example: /set_reminder 2023-08-10 18:00 Reminder Text
        notify_time = datetime.strptime(user_message[1], "%Y-%m-%d %H:%M")
        reminder_text = user_message[2]
        schedule_time_notification(message.bot, message.from_user.id, reminder_text, notify_time)
        await message.answer(f"⏰ Reminder set for {notify_time}.")
    except (IndexError, ValueError):
        await message.answer("Invalid format. Use: /set_reminder YYYY-MM-DD HH:MM Reminder Text")