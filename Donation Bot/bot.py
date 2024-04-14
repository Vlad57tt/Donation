from dotenv import load_dotenv
import asyncio
import os
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handers import start, choosePaymentAmount
from bot.callbacks import common, donation

# Инициализация бота
load_dotenv()
starup_router = Router()


@starup_router.startup()
async def startup():
    print("----------<Бот запущен>----------")

async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(common.router, donation.router,
                       choosePaymentAmount.router, start.router)
    dp.include_router(starup_router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())