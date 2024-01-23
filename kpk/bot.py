import asyncio
from aiogram import Bot, Dispatcher, executor, types
from mozgi.cfg import TOKEN
import logging



bot = Bot(token=TOKEN)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)