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

router = Router()

bot = Bot(token = config.TOKEN, parse_mode = 'HTML')
dp = Dispatcher()

@router.message(Command(commands = ['start']))
async def cmd_start(message: types.Message):
    await message.answer('<b>👋 Привіт, я Бот Погода в Україні 🇺🇦\n'
                         '📌 Просто вибери своє місто 🏠\n\n'
                         '❓ Ви зможете дізнатися:\n'
                         ' —  Погоду 🌧\n'
                         ' —  Сер. температуру 🌡\n'
                         ' —  Як відчувається погода 🌡\n'
                         ' —  Вологість повітря💧\n'
                         ' —  Швидкість вітру 💨\n'
                         ' —  Хмари ☁️\n'
                         ' —  Час сходу сонця 🌅\n' 
                         ' —  Час заходу сонця 🌇\n\n'
                         '🗓 Прогноз Погоди - /weather\n'
                         '⁉️ Технічна підтримка - /help</b>', parse_mode = 'HTML')

@router.message(Command(commands = ['help']))
async def cmd_help(message: types.Message):
    await message.answer("<b>⁉️ Якщо у вас є проблеми. \n✉️ Напишіть мені</b> <a href = 'https://t.me/nikit0ns'>@nikit0ns</a><b>.</b>", disable_web_page_preview = 'True')