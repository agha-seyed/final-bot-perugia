from aiogram import Router, types
from aiogram.filters import Command
from utils.notifications import set_user_preference, send_custom_notification
from utils.reminders import schedule_reminder, cancel_reminder
from datetime import datetime, timedelta

router = Router()

@router.message(Command("set_language"))
async def set_language(message: types.Message):
    """Set the user's preferred language."""
    lang_map = {"English": "en", "فارسی": "fa", "Italiano": "it"}
    if message.text in lang_map:
        set_user_preference(message.from_user.id, "language", lang_map[message.text])
        await message.reply("Language preference updated.")
    else:
        await message.reply("Invalid language selection.")

@router.message(Command("remind_me"))
async def remind_me(message: types.Message):
    """Set a reminder."""
    try:
        reminder_time = datetime.now() + timedelta(minutes=1)  # Example: 1 minute later
        schedule_reminder(
            bot=message.bot,
            user_id=message.from_user.id,
            message="This is your reminder!",
            reminder_time=reminder_time
        )
        await message.reply(f"Reminder set for {reminder_time}.")
    except Exception as e:
        await message.reply("Failed to set reminder.")
        print(e)

@router.message(Command("cancel_reminder"))
async def cancel_reminder_handler(message: types.Message):
    """Cancel a reminder."""
    try:
        reminder_time = datetime.now() + timedelta(minutes=1)  # Example: 1 minute later
        cancel_reminder(
            user_id=message.from_user.id,
            reminder_time=reminder_time
        )
        await message.reply(f"Reminder canceled for {reminder_time}.")
    except Exception as e:
        await message.reply("Failed to cancel reminder.")
        print(e)