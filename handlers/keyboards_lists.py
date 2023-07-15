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
from .functions_keyboard import first_list, second_list, third_list

router = Router()
bot = Bot(token = config.TOKEN, parse_mode = 'HTML')
dp = Dispatcher()
    
@router.callback_query(Text(startswith = 'First_List'))
async def first_keyboard(callback: types.CallbackQuery):
    first_list_buttons = first_list()
    await callback.message.edit_text('<b>🏠 Будь ласка виберіть ваше місто:</b>', reply_markup = first_list_buttons)

#Вторая клавиатура вызов
@router.callback_query(Text(startswith = 'Second_List'))
async def second_keyboard(callback: types.CallbackQuery):
    second_list_buttons = second_list()
    await callback.message.edit_text('<b>🏠 Будь ласка виберіть ваше місто:</b>', reply_markup = second_list_buttons)

#Третья клавиатура вызов
@router.callback_query(Text(startswith = 'Third_List'))
async def second_keyboard(callback: types.CallbackQuery):
    third_list_buttons = third_list()
    await callback.message.edit_text('<b>🏠 Будь ласка виберіть ваше місто:</b>', reply_markup = third_list_buttons)