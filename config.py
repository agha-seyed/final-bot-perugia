import os

# Bot and City Identifiers
BOT_ID = os.getenv("BOT_ID", "perugia")
CITY_NAME = os.getenv("CITY_NAME", "Perugia")

# Telegram Credentials
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_IDS = os.getenv("ADMIN_CHAT_IDS", "123456789").split(",")
CHANNEL_ID = os.getenv("CHANNEL_ID", "@YourChannel")

# Webhook Details
BASE_URL = os.getenv("BASE_URL", "https://your-bot.onrender.com")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "YourSecret")

# Database and Caching
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")
SQLITE_DB = os.getenv("SQLITE_DB", "data.db")

# Feature Flags
FEATURE_FLAGS = {
    "GAMIFICATION": True,
    "PODCASTS": True,
    "ROOMMATE": True,
    "NEWS": True,
}

# JSON File Versioning
JSON_VERSION = "1.0"