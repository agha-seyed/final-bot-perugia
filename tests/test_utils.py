import pytest
from utils.db_utils import save_news, get_connection
from utils.notifications import set_user_preference, get_user_preference
from utils.reminders import schedule_reminder, cancel_reminder
from datetime import datetime, timedelta

def test_save_news():
    """Test saving news to the database."""
    news = {"title": "Test News", "content": "This is a test.", "file": None, "timestamp": "2025-08-07"}
    save_news(news)
    conn = get_connection()
    row = conn.execute("SELECT * FROM news WHERE title = ?", (news["title"],)).fetchone()
    assert row["content"] == news["content"]

def test_set_user_preference():
    """Test setting and getting user preferences."""
    user_id = 123
    set_user_preference(user_id, "language", "en")
    lang = get_user_preference(user_id, "language")
    assert lang == "en"

@pytest.mark.asyncio
async def test_schedule_and_cancel_reminder():
    """Test scheduling and canceling reminders."""
    bot_mock = None  # Mock bot instance
    user_id = 123
    message = "Test Reminder"
    reminder_time = datetime.now() + timedelta(minutes=1)
    schedule_reminder(bot_mock, user_id, message, reminder_time)

    # Verify reminder is scheduled
    scheduler = AsyncIOScheduler()
    job_id = f"reminder_{user_id}_{reminder_time}"
    job = scheduler.get_job(job_id)
    assert job is not None

    # Cancel reminder
    cancel_reminder(user_id, reminder_time)
    job = scheduler.get_job(job_id)
    assert job is None