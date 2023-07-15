from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject, Text
from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import Open_Weather_Token
import asyncio
import config
import requests
import datetime
import translators
from .functions_keyboard import first_list


router = Router()
bot = Bot(token = config.TOKEN, parse_mode = 'HTML')
dp = Dispatcher()
    
@router.message(Command(commands = ['weather']))
async def weather(message: types.Message, command: CommandObject):

    if command.args:
        await message.answer('<b>⚠️ Неправильно вибрана команда.</b>')
        return

    first_list_buttons = first_list()
    await message.answer('<b>🏠 Будь ласка виберіть ваше місто:</b>', reply_markup = first_list_buttons)