import json
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

def load_search_data():
    """Load search data from JSON file."""
    with open("search_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@router.message(Command("search_accommodation"))
async def search_accommodation(message: types.Message):
    """Search for accommodations."""
    data = load_search_data()["accommodations"]
    response = "🏠 Available Accommodations:\n"
    for item in data:
        response += f"\n**{item['title']}**\nPrice: €{item['price']} per month\nLocation: {item['location']}\n{item['description']}\n"
    await message.answer(response)

@router.message(Command("search_courses"))
async def search_courses(message: types.Message):
    """Search for courses."""
    data = load_search_data()["courses"]
    response = "📚 Available Courses:\n"
    for item in data:
        response += f"\n**{item['title']}**\nDuration: {item['duration']}\n{item['description']}\n"
    await message.answer(response)