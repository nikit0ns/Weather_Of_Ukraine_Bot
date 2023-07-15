import asyncio
import config
from config import TOKEN, Open_Weather_Token
from aiogram import Bot, Dispatcher
import handlers
from handlers import handler, keyboards_lists, messages_city, personal_actions


# Запуск бота
async def main():
    bot = Bot(token=config.TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_router(handler.router)
    dp.include_router(keyboards_lists.router)
    dp.include_router(messages_city.router)
    dp.include_router(personal_actions.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

    