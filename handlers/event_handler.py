import json
from aiogram import Router, types
from datetime import datetime

router = Router()

def load_events():
    """Load events from JSON file."""
    with open("calendar.json", "r", encoding="utf-8") as f:
        return json.load(f)

@router.message(commands=["events"])
async def list_events(message: types.Message):
    """List upcoming events."""
    events = load_events()
    today = datetime.now().date()
    upcoming_events = [
        event for event in events if datetime.strptime(event["date"], "%Y-%m-%d").date() >= today
    ]
    
    if not upcoming_events:
        await message.answer("No upcoming events.")
        return
    
    response = "📅 Upcoming Events:\n"
    for event in upcoming_events:
        response += f"\n**{event['title']}**\nDate: {event['date']}\n{event['description']}\n"
    
    await message.answer(response)