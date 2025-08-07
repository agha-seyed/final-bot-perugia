import json
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

def load_podcasts():
    """Load podcast data from JSON file."""
    with open("podcasts.json", "r", encoding="utf-8") as f:
        return json.load(f)

@router.message(Command("list_podcasts"))
async def list_podcasts(message: types.Message):
    """List available podcasts."""
    podcasts = load_podcasts()["podcasts"]
    response = "🎙️ Available Podcasts:\n"
    for podcast in podcasts:
        response += f"\n**{podcast['title']}**\n{podcast['description']}\n[🎧 Listen here]({podcast['url']})\n"
    await message.answer(response, disable_web_page_preview=True)