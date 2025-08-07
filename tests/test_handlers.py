import pytest
from aiogram.types import Message
from handlers.cmd_start import start_command
from handlers.gamification_handler import show_points, show_leaderboard

@pytest.mark.asyncio
async def test_start_command():
    """Test the /start command."""
    message = Message(text="/start", from_user={"id": 123})
    state = {}
    redis_mock = {}
    await start_command(message, state, redis_mock)
    assert "Please select your language" in message.text

@pytest.mark.asyncio
async def test_show_points():
    """Test the /points command."""
    message = Message(text="/points", from_user={"id": 123})
    total_points = 50  # Mocked total points
    await show_points(message)
    assert f"You have {total_points} points!" in message.text

@pytest.mark.asyncio
async def test_show_leaderboard():
    """Test the /leaderboard command."""
    message = Message(text="/leaderboard", from_user={"id": 123})
    leaderboard_data = [
        {"user_id": 1, "total_points": 100},
        {"user_id": 2, "total_points": 80},
    ]  # Mocked leaderboard data
    await show_leaderboard(message)
    assert "🏆 Leaderboard:" in message.text