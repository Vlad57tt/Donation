from aiogram.fsm.state import State, StatesGroup

class ChoosePaymentAmonuntState(StatesGroup):
    wait_for_amount = State()