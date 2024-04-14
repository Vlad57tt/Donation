from aiogram.filters.callback_data import CallbackData

class DonateAmountFac(CallbackData, prefix="selected_donate"):
    amount: int