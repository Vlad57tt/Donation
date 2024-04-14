from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.keyboards import start_menu

router = Router()


@router.callback_query(F.data == "back")
async def donate(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Добро пожаловать!", reply_markup=start_menu())
    await state.clear()

