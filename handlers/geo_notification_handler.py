from aiogram import Router, types
from aiogram.filters import Command
from utils.geo_notifications import get_notification_for_location

router = Router()

@router.message(Command("geo_notify"))
async def geo_notification(message: types.Message):
    """Send location-based notification."""
    try:
        user_location = message.text.split(maxsplit=1)[1]  # Example: /geo_notify Perugia
        notification = get_notification_for_location(user_location)
        if notification:
            await message.answer(f"📍 Notification for {user_location}:\n{notification}")
        else:
            await message.answer(f"🌍 Sorry, no notifications available for {user_location}.")
    except IndexError:
        await message.answer("Please provide a location. Example: /geo_notify Perugia")