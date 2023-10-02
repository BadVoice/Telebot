from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types, F
import asyncio

from handlers import questions, different_types

load_dotenv()
BOT_ID = os.getenv('BOT_KEY')

# Запуск бота
async def main():
    bot = Bot(token=BOT_ID, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(questions.router, different_types.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
