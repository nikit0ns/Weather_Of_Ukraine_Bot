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


bot = Bot(token = config.TOKEN, parse_mode = 'HTML')
dp = Dispatcher()


def back_first_list():
    builder = InlineKeyboardBuilder()
    builder.button(text = '↩️ Інше місто', callback_data = 'First_List')
    return builder.as_markup()

#Кнопка назад ко второй клаве
def back_second_list():
    builder = InlineKeyboardBuilder()
    builder.button(text = '↩️ Інше місто', callback_data = 'Second_List')
    return builder.as_markup()

#Кнопк назад к третей клаве
def back_third_list():
    builder = InlineKeyboardBuilder()
    builder.button(text = '↩️ Інше місто', callback_data = 'Third_List')
    return builder.as_markup()