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

def first_list():

    builder = InlineKeyboardBuilder()
    builder.button(text = 'Київ', callback_data = 'Kyiv')
    builder.button(text = 'Львів', callback_data = 'Lviv') 
    builder.button(text = 'Дніпро', callback_data = 'Dnipro') 
    builder.button(text = 'Харків', callback_data = 'Kharkiv')
    builder.button(text = 'Івано-Франківськ', callback_data = 'Ivano-Frankivsk') 
    builder.button(text = 'Тернопіль', callback_data = 'Ternopil')
    builder.button(text = 'Вінниця', callback_data = 'Vinnytsia') 
    builder.button(text = 'Запоріжжя', callback_data = 'Zaporizhzhia')
    builder.button(text = 'Хмельницький', callback_data = 'Khmelnytskyi')
    builder.button(text = 'Луцьк', callback_data = 'Lutsk')
    builder.button(text = 'Одеса', callback_data = 'Odesa')
    builder.button(text = 'Рівне', callback_data = 'Rivne')
    builder.button(text = '➡️', callback_data = 'Second_List')
    builder.adjust(2) 

    return builder.as_markup()

def second_list():

    builder = InlineKeyboardBuilder()
    builder.button(text = 'Житомир', callback_data = 'Zhytomyr')
    builder.button(text = 'Полтава', callback_data = 'Poltava') 
    builder.button(text = 'Миколаїв', callback_data = 'Mykolaiv') 
    builder.button(text = 'Черкаси', callback_data = 'Cherkasy')
    builder.button(text = 'Чернівці', callback_data = 'Chernivtsi') 
    builder.button(text = 'Кропивницький', callback_data = 'Kropyvnytskyi')
    builder.button(text = 'Чернігів', callback_data = 'Chernihiv')
    builder.button(text = 'Суми', callback_data = 'Sumy') 
    builder.button(text = 'Ужгород', callback_data = 'Uzhhorod')
    builder.button(text = 'Херсон', callback_data = 'Kherson')
    builder.button(text = 'Донецьк', callback_data = 'Donetsk')
    builder.button(text = 'Луганськ', callback_data = 'Luhansk')
    builder.button(text = '⬅️', callback_data = 'First_List')
    builder.button(text = '➡️', callback_data = 'Third_List')
    builder.adjust(2)

    return builder.as_markup()

def third_list():

    builder = InlineKeyboardBuilder()
    builder.button(text = 'Сімферополь', callback_data = 'Simferopol')
    builder.button(text = '⬅️', callback_data = 'Second_List')
    builder.adjust(1)

    return builder.as_markup()