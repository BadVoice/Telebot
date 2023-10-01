from dotenv import load_dotenv
import os
from aiogram import Bot, types, Dispatcher
from aiogram.filters import Filter
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

load_dotenv()

BOT_ID = os.getenv('BOT_KEY')

bot = Bot(token=BOT_ID)
dp = Dispatcher()

@dp.message(CommandStart())
async def my_env_bot_id(message: types.Message):
    await message.answer(BOT_ID)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(BOT_ID)
    # And the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())