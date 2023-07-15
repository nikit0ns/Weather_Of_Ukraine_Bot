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
from .buttons_back import back_first_list, back_second_list, back_third_list
from .weather_settings import weather_city


router = Router()
bot = Bot(token = config.TOKEN, parse_mode = 'HTML')
dp = Dispatcher()


# Місто Київ
@router.callback_query(Text(startswith = 'Kyiv'))
async def Kyiv_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={50.4333}&lon={30.5167}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Київ\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Львів
@router.callback_query(Text(startswith = 'Lviv'))
async def SKyiv_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={49.8383}&lon={24.0232}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Львів\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Дніпро
@router.callback_query(Text(startswith = 'Dnipro'))
async def Dnipro_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={48.45}&lon={34.9833}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Дніпро\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Харків
@router.callback_query(Text(startswith = 'Kharkiv'))
async def Kharkiv_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={50}&lon={36.25}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Харків\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Івано-Франківськ
@router.callback_query(Text(startswith = 'Ivano-Frankivsk'))
async def IvanoFrankivsk_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={48.9215}&lon={24.7097}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Івано-Франківськ\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Тернопіль
@router.callback_query(Text(startswith = 'Ternopil'))
async def Ternopil_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={49.5559}&lon={25.6056}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Тернопіль\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Вінниця
@router.callback_query(Text(startswith = 'Vinnytsia'))
async def Vinnytsia_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={49.2328}&lon={28.481}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Вінниця\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Запоріжжя
@router.callback_query(Text(startswith = 'Zaporizhzhia'))
async def Zaporizhzhia_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={47.8508}&lon={35.1183}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Запоріжжя\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Хмельницький
@router.callback_query(Text(startswith = 'Khmelnytskyi'))
async def Khmelnytskyi_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={49.4216}&lon={26.9965}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Хмельницький\n{info_weather}</b>', reply_markup = back_list_buttons)  

# Місто Луцьк
@router.callback_query(Text(startswith = 'Lutsk'))
async def Lutsk_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={50.7593}&lon={25.3424}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Луцьк\n{info_weather}</b>', reply_markup = back_list_buttons) 

# Місто Одеса
@router.callback_query(Text(startswith = 'Odesa'))
async def Odesa_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={46.4775}&lon={30.7326}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Одеса\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Рівне
@router.callback_query(Text(startswith = 'Rivne'))
async def Rivne_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={50.6231}&lon={26.2274}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_first_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Рівне\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Житомир
@router.callback_query(Text(startswith = 'Zhytomyr'))
async def Zhytomyr_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={50.2649}&lon={28.6767}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Житомир\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Полтава
@router.callback_query(Text(startswith = 'Poltava'))
async def Poltava_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={49.5937}&lon={34.5407}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Полтава\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Миколаїв
@router.callback_query(Text(startswith = 'Mykolaiv'))
async def Mykolaiv_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={49.5237}&lon={23.9852}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Миколаїв\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Черкаси
@router.callback_query(Text(startswith = 'Cherkasy'))
async def Cherkasy_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={49.4285}&lon={32.0621}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Черкаси\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Чернівці
@router.callback_query(Text(startswith = 'Chernivtsi'))
async def Chernivtsi_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={48.2915}&lon={25.9403}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Чернівці\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Кропивницький
@router.callback_query(Text(startswith = 'Kropyvnytskyi'))
async def Kropyvnytskyi_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={48.5132}&lon={32.2597}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Кропивницький\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Чернігів
@router.callback_query(Text(startswith = 'Chernihiv'))
async def Chernihiv_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={51.5055}&lon={31.2849}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Чернігів\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Суми
@router.callback_query(Text(startswith = 'Sumy'))
async def Sumy_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={50.9216}&lon={34.8003}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Суми\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Ужгород
@router.callback_query(Text(startswith = 'Uzhhorod'))
async def Uzhhorod_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={48.6167}&lon={22.3}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Ужгород\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Херсон
@router.callback_query(Text(startswith = 'Kherson'))
async def Kherson_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={46.6558}&lon={32.6178}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Херсон\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Донецьк
@router.callback_query(Text(startswith = 'Donetsk'))
async def Donetsk_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={48}&lon={37.8}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Донецьк\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Луганськ
@router.callback_query(Text(startswith = 'Luhansk'))
async def Luhansk_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={48.5671}&lon={39.3171}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_second_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Луганськ\n{info_weather}</b>', reply_markup = back_list_buttons)

# Місто Сімферополь 
@router.callback_query(Text(startswith = 'Simferopol'))
async def Luhansk_City(callback: types.CallbackQuery):
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={44.9572}&lon={34.1108}&appid={Open_Weather_Token}&units=metric'
    )
    info_weather = weather_city(r)
    back_list_buttons = back_third_list()
    await callback.message.edit_text(f'<b>🏠 Місто: Сімферополь\n{info_weather}</b>', reply_markup = back_list_buttons)