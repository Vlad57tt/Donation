from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.keyboards import start_menu

router = Router()


@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer("Добро пожаловать!", reply_markup=start_menu())

