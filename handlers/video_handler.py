import json
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

def load_videos():
    """Load video data from JSON file."""
    with open("videos.json", "r", encoding="utf-8") as f:
        return json.load(f)

@router.message(Command("list_videos"))
async def list_videos(message: types.Message):
    """List available videos."""
    videos = load_videos()["videos"]
    response = "🎥 Available Videos:\n"
    for video in videos:
        response += f"\n**{video['title']}**\n{video['description']}\n[▶️ Watch here]({video['url']})\n"
    await message.answer(response, disable_web_page_preview=True)