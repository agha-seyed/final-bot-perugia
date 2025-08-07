from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_CHAT_IDS, CHANNEL_ID
from utils.db_utils import save_news
from utils.gdrive import upload_file
from datetime import datetime
import json

router = Router()

@router.message(Command("post_news"))
async def post_news(message: types.Message, state):
    if str(message.from_user.id) not in ADMIN_CHAT_IDS:
        await message.reply("Only admins can post news.")
        return
    
    await message.reply("Please enter the title of the news:")
    await state.set_state("news_title")

@router.message(state="news_title")
async def news_title_handler(message: types.Message, state):
    await state.update_data(title=message.text)
    await message.reply("Please enter the content of the news or upload a file:")
    await state.set_state("news_content")

@router.message(state="news_content")
async def news_content_handler(message: types.Message, state):
    data = await state.get_data()
    news = {"title": data["title"], "content": message.text, "file": None, "timestamp": str(datetime.now())}

    if message.document or message.photo or message.video:
        file = await (message.document or message.photo[-1] or message.video).download()
        news["file"] = upload_file(file.name)

    save_news(news)
    await message.bot.send_message(CHANNEL_ID, f"📢 **{news['title']}**\n\n{news['content']}")
    await message.reply("News posted successfully!")
    await state.clear()