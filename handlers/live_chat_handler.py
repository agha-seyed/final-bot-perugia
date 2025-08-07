from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_CHAT_IDS

router = Router()

@router.message(Command("live_chat"))
async def live_chat_start(message: types.Message):
    if str(message.from_user.id) not in ADMIN_CHAT_IDS:
        await message.reply("You are not authorized to start a live chat.")
        return
    
    await message.reply("Live chat started. Users can now send messages to admins.")