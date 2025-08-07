# StudentBot: Telegram Bot for Students in Perugia

StudentBot is a comprehensive Telegram bot designed to assist students in Perugia. The bot provides various features such as event notifications, cost of living details, live chat, gamification, and much more.

## Features
- **Multilingual Support**: English, Persian, and Italian.
- **Event Calendar**: Notify students about upcoming deadlines and events.
- **Cost of Living**: Provide details on living expenses in Perugia.
- **News Management**: Post and manage news updates.
- **Live Chat**: Enable communication between students and admins.
- **Gamification**: Reward users with points and badges.
- **Admin Dashboard**: A web-based interface for managing the bot.
- **AI-Powered Q&A**: Answer student queries using semantic search.

---

## Project Structure
```
studentbot/
├── main.py                      # Webhook entry point
├── config.py                    # Environment variables and settings
├── requirements.in              # Primary dependencies
├── requirements.txt             # Compiled dependencies
├── lang/                        # Language translations
├── ai/                          # AI-related modules
├── utils/                       # Utility modules
├── handlers/                    # Telegram bot handlers
├── admin_web/                   # Admin dashboard
├── tests/                       # Test cases
```

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL or SQLite
- Redis (for caching and scheduling tasks)
- Telegram Bot Token

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/agha-seyed/studentbot.git
   cd studentbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file and configure environment variables:
   ```env
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   BASE_URL=https://your-bot-url
   DATABASE_URL=sqlite:///data.db
   REDIS_URL=redis://localhost:6379
   ```

4. Initialize the database:
   ```bash
   python -c "from models_db import create_tables; create_tables()"
   ```

5. Run the bot:
   ```bash
   python main.py
   ```

---

## Usage

### Admin Commands
- `/admin_panel`: Access the admin panel.
- `/post_news`: Post news to the channel.
- `/live_chat`: Start or stop live chat.

### User Commands
- `/start`: Start the bot and select the language.
- `/points`: View your total points.
- `/leaderboard`: View the leaderboard.
- `/remind_me`: Set a reminder.

---

## Testing
Run all test cases using `pytest`:
```bash
pytest --asyncio-mode=auto
```

---

## Contributors
- **Agha Seyed** - [GitHub Profile](https://github.com/agha-seyed)

---

## License
This project is licensed under the MIT License.