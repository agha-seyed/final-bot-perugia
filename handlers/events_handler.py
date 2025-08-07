from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

@router.callback_query(lambda c: c.data == 'events')
async def events_menu(callback_query: types.CallbackQuery):
    """Show events and announcements menu."""
    events_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 مشاهده رویدادهای آینده", callback_data="view_events")],
        [InlineKeyboardButton(text="⏰ تنظیم یادآوری برای رویداد", callback_data="set_event_reminder")],
        [InlineKeyboardButton(text="📣 اطلاعیه‌های مهم", callback_data="important_announcements")],
        [InlineKeyboardButton(text="🔙 بازگشت به منوی اصلی", callback_data="main_menu")]
    ])

    await callback_query.message.edit_text("📅 منوی رویدادها و اطلاعیه‌ها:", reply_markup=events_menu)