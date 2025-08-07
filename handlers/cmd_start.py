from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from redis import Redis
import json

router = Router()

# Load language files
LANGUAGES = {
    "en": "lang/en.json",
    "fa": "lang/fa.json",
    "it": "lang/it.json"
}

def load_language(lang_code):
    with open(LANGUAGES[lang_code], "r", encoding="utf-8") as file:
        return json.load(file)

@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext, redis: Redis):
    # Show language options
    buttons = [
        [types.KeyboardButton(text="English")],
        [types.KeyboardButton(text="فارسی")],
        [types.KeyboardButton(text="Italiano")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("Please select your language:\nلطفاً زبان خود را انتخاب کنید:\nSeleziona la tua lingua:", reply_markup=keyboard)
    await state.set_state("choose_language")

@router.message(state="choose_language")
async def choose_language(message: types.Message, state: FSMContext, redis: Redis):
    lang_map = {"English": "en", "فارسی": "fa", "Italiano": "it"}
    chosen_lang = lang_map.get(message.text)
    if chosen_lang:
        redis.set(f"user:{message.from_user.id}:lang", chosen_lang)
        lang = load_language(chosen_lang)
        await message.answer(lang["start_message"], reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.answer("Invalid selection. Please choose a valid language.")