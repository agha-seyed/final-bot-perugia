from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

@router.callback_query(lambda c: c.data == 'student_life')
async def student_life_menu(callback_query: types.CallbackQuery):
    """Show student life info menu."""
    student_life_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💰 هزینه‌های زندگی", callback_data="living_costs")],
        [InlineKeyboardButton(text="📌 نکات زندگی در پروجا", callback_data="life_tips")],
        [InlineKeyboardButton(text="🔙 بازگشت به منوی اصلی", callback_data="main_menu")]
    ])

    await callback_query.message.edit_text("🏠 اطلاعات زندگی دانشجویی:", reply_markup=student_life_menu)