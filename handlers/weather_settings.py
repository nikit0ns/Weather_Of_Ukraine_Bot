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


def weather_city(r):
    data = r.json()
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%H:%M:%S')
    weather = data['weather'][0]['main']
    translate_weather = translators.translate_text(weather, from_language = 'en', to_language = 'uk')
    description = data['weather'][0]['description']
    translate_description = translators.translate_text(description,from_language = 'en', to_language = 'uk')
    temp = round(data['main']['temp'])
    feels_like = round(data['main']['feels_like'])
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    clouds = data['clouds']['all']
    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

    if weather == 'Thunderstorm':
        emodji = '⛈'
    elif weather == 'Drizzle' or weather == 'Rain':
        emodji = '🌧'
    elif weather == 'Snow':
        emodji = '❄️'
    elif weather == 'Clear':
        emodji = '☀️'
    elif weather == 'Tornado':
        emodji = '🌪'
    else:
        emodji = '☁️'

    sign_temp = '+' if temp > 0 else ''
    sign_feels_like = '+' if feels_like > 0 else ''

    if ',' in translate_description:
        translate_description = translate_description.replace(',', '')
    else:
        translate_description = translators.translate_text(description, from_language = 'en', to_language = 'uk')

    info_weather = (f'🗓 Дата: {date}\n'
            f'⏱ Час: {time}\n\n'
            f'{emodji} {translate_weather}: {translate_description}\n'
            f'🌡️ Сер. температура: {sign_temp}{temp}°C\n'
            f'🌡️ Відчувається: {sign_feels_like}{feels_like}°C\n'
            f'💧 Вологість: {humidity}%\n'
            f'💨 Вітер: {wind}м/с\n'
            f'☁️ Хмари: {clouds}%\n'
            f'🌅 Схід сонця: {sunrise}\n'
            f'🌇 Захід сонця: {sunset}')

    return info_weather