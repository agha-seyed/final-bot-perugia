import pytest
from utils.advanced_gamification import add_quest, get_active_quests, complete_quest, get_user_level, add_experience

def test_add_and_retrieve_quests():
    """Test adding and retrieving quests."""
    add_quest("Test Quest", "Complete the test.", 50, "daily")
    quests = get_active_quests()
    assert len(quests) > 0
    assert quests[0]["title"] == "Test Quest"

def test_complete_quest_and_level_up():
    """Test completing a quest and leveling up."""
    user_id = 123
    quest_id = 1
    add_experience(user_id, 90)  # Close to level-up threshold
    complete_quest(user_id, quest_id)
    level_data = get_user_level(user_id)
    assert level_data["level"] >= 2  # User should have leveled up