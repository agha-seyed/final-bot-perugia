from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

@router.message(commands=['start'])
async def start_command(message: types.Message):
    """Handle the /start command."""
    user_name = message.from_user.first_name
    # Welcome message
    welcome_text = f"""
👋 سلام {user_name}! به ربات دانشجویی ما خوش آمدید! 🎓

🎯 امکانات ویژه ما:
- مشاهده رویدادها و اطلاعیه‌ها 📅
- جست‌وجوی پیشرفته برای دوره‌ها، هم‌خانه و املاک 🔍
- پخش پادکست‌ها و ویدیوهای آموزشی 🎙️
- گیمیفیکیشن برای یادگیری جذاب 🎮
- مشاهده آمار و تحلیل داده‌ها 📊
- تنظیم یادآوری‌ها و اعلان‌ها ⏰

📍 از منوی زیر برای شروع استفاده کنید!
    """

    # Inline keyboard for the main menu
    main_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 رویدادها و اطلاعیه‌ها", callback_data="events")],
        [InlineKeyboardButton(text="🏠 اطلاعات زندگی دانشجویی", callback_data="student_life")],
        [InlineKeyboardButton(text="🔍 جست‌وجوی پیشرفته", callback_data="advanced_search")],
        [InlineKeyboardButton(text="🎙️ پادکست‌ها و ویدیوها", callback_data="media")],
        [InlineKeyboardButton(text="⏰ یادآوری‌ها", callback_data="reminders")],
        [InlineKeyboardButton(text="🎮 گیمیفیکیشن و امتیازها", callback_data="gamification")],
        [InlineKeyboardButton(text="📊 داشبورد تحلیل داده‌ها", callback_data="analytics")],
        [InlineKeyboardButton(text="👤 پروفایل من", callback_data="profile")]
    ])

    await message.answer(welcome_text, reply_markup=main_menu)