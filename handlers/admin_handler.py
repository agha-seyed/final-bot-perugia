from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_CHAT_IDS

router = Router()

@router.message(Command("admin_panel"))
async def admin_panel(message: types.Message):
    if str(message.from_user.id) not in ADMIN_CHAT_IDS:
        await message.answer("You are not authorized to access the admin panel.")
        return
    
    buttons = [
        [types.KeyboardButton(text="📢 Post News")],
        [types.KeyboardButton(text="📊 View Analytics")],
        [types.KeyboardButton(text="⚙️ Manage Settings")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("Welcome to the Admin Panel. Select an option:", reply_markup=keyboard)