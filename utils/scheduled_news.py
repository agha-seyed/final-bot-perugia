import json
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot

scheduler = AsyncIOScheduler()

def load_scheduled_news():
    """Load scheduled news from JSON file."""
    with open("scheduled_news.json", "r", encoding="utf-8") as f:
        return json.load(f)

def schedule_news_notifications(bot: Bot):
    """Schedule news notifications."""
    news_items = load_scheduled_news()
    for news in news_items:
        schedule_time = datetime.strptime(news["schedule_time"], "%Y-%m-%d %H:%M:%S")
        scheduler.add_job(
            bot.send_message,
            trigger="date",
            run_date=schedule_time,
            args=["-100123456789", f"📰 {news['title']}\n\n{news['message']}"],  # Example: Send to a channel
            id=f"news_{news['id']}",
            replace_existing=True
        )
    scheduler.start()