import asyncio
import os
import time
import logging

logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

dotenv_file = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_file):
    load_dotenv(dotenv_file)

TOKEN: str = os.getenv('TOKEN')
MSG: str = 'Ты сегодня уже учился(-ась), {}?'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name

    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await message.answer(f'Привет, {user_name}!')

    await asyncio.sleep(.1)
    for i in range(7):
        await bot.send_message(user_id, MSG.format(user_name))
        await asyncio.sleep(60 * 60 * 24)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
