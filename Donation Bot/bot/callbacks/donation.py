from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.keyboards import donate_menu, pay_menu, back_button
from bot.facrotry import DonateAmountFac
from bot.state import ChoosePaymentAmonuntState
from bot.utills import create_invoice, getexchange, get_status

router = Router()


@router.callback_query(F.data == "donate")
async def donate(call: CallbackQuery):
    await call.message.edit_text("Выберите сумму для доната",
                                 reply_markup=donate_menu())


@router.callback_query(DonateAmountFac.filter())
async def donate_choosen(call: CallbackQuery, callback_data: DonateAmountFac):
    amount = callback_data.amount
    rates = await getexchange()
    usdt_amount = float(amount) / float(rates)
    total_usdt = usdt_amount * (1 + 15 / 100)
    invoice_link, invoice_id = await create_invoice(price=total_usdt)
    await call.message.edit_text(f"""
💲Сумма: {amount}₽
⏰Время на оплату: 15 минут
💸Для оплаты перейдите по ссылке ниже:
{invoice_link}
""",
                                 reply_markup=pay_menu(url=invoice_link,id=invoice_id))


@router.callback_query(F.data == "chooseAmount")
async def choose_donate_amount(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Напишите сумму для доната",
                                 reply_markup=back_button())
    await state.set_state(ChoosePaymentAmonuntState.wait_for_amount)


@router.callback_query(lambda c: c.data and c.data.startswith('pay/check'))
async def process_callback(callback_query: CallbackQuery):
    payload = callback_query.data
    user_id = callback_query.from_user.id
    _, order_id_param = payload.split('?', 1)
    order_id_key, order_id_value = order_id_param.split('=', 1)

    if order_id_key == 'order_id':
        order_id = order_id_value
        try:
            if await get_status(order_id):
                await callback_query.message.answer("Оплата найдена!")
            else:
                await callback_query.message.answer("Оплата не найдена или прошёл срок действия!")
        except Exception as e:
            await callback_query.message.answer(f"Произошла ошибка при обработке вашего запроса!\nКод ошибкт для тех.поддержки:{e}")


