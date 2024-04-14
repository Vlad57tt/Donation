from aiogram import Router
from aiogram.types import Message
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext

from bot.state import ChoosePaymentAmonuntState
from bot.keyboards import special_donate

router = Router()

def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

@router.message(StateFilter(ChoosePaymentAmonuntState.wait_for_amount))
async def choose_amount(msg: Message, state: FSMContext):
    amount = msg.text
    if not is_number(amount):
        await msg.answer("Напишите число!")
    elif int(amount) > 10000:
        await msg.answer("Cумма слишком большая!")
    elif int(amount) <= 0:
        await msg.answer("Cумма слишком маленькая или равно нулю!")
    else:

        await msg.answer(text=f"Сумма: {amount}₽\n",
                         reply_markup=special_donate(amount=amount))
        await state.clear()
