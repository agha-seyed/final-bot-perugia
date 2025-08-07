from aiogram import Router, types
from aiogram.filters import Command
from utils.advanced_gamification import get_active_quests, complete_quest, add_experience, get_user_level

router = Router()

@router.message(Command("quests"))
async def show_quests(message: types.Message):
    """Show active quests."""
    quests = get_active_quests()
    if not quests:
        await message.answer("No active quests available.")
        return
    
    response = "🎯 Active Quests:\n"
    for quest in quests:
        response += f"\n**{quest['title']}**\n{quest['description']}\nReward: {quest['reward_points']} points\n"
    
    await message.answer(response)

@router.message(Command("complete_quest"))
async def complete_user_quest(message: types.Message):
    """Mark a quest as completed."""
    try:
        quest_id = int(message.text.split()[1])  # Example: /complete_quest 1
        user_id = message.from_user.id
        complete_quest(user_id, quest_id)
        quest = [q for q in get_active_quests() if q["id"] == quest_id][0]
        add_experience(user_id, quest["reward_points"])
        await message.answer(f"✅ Quest '{quest['title']}' completed. You earned {quest['reward_points']} points!")
    except Exception as e:
        await message.answer("Failed to complete the quest. Please ensure you entered a valid quest ID.")
        print(e)

@router.message(Command("level"))
async def show_user_level(message: types.Message):
    """Show user level and experience."""
    user_data = get_user_level(message.from_user.id)
    response = (
        f"🏅 Your Level: {user_data['level']}\n"
        f"📈 Experience: {user_data['experience']}/{user_data['next_level_exp']}\n"
    )
    await message.answer(response)