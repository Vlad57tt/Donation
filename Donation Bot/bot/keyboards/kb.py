from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.facrotry import DonateAmountFac

# Клавиатура главного меню


def start_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Задонатить", callback_data="donate")
    kb.button(text="Пустышка", callback_data="empty")

    return kb.as_markup()


def donate_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="50₽", callback_data=DonateAmountFac(amount=50))
    kb.button(text="100₽", callback_data=DonateAmountFac(amount=100))
    kb.button(text="Другая сумма", callback_data="chooseAmount")
    kb.button(text="Отмена", callback_data="back")
    kb.adjust(2, 1, 1)

    return kb.as_markup()


def special_donate(amount: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Подтвердить", callback_data=DonateAmountFac(amount=amount))
    kb.button(text="Отмена", callback_data="back")
    kb.button(text="Другая сумма", callback_data="chooseAmount")
    kb.adjust(2, 1)

    return kb.as_markup()


def back_button() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Отмена", callback_data="back")

    return kb.as_markup()


def pay_menu(url: str, id: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Перейти к оплате", url=url)
    kb.button(text="Проверить оплату", callback_data=f"pay/check?order_id={id}")
    kb.button(text="Назад", callback_data="back")
    kb.adjust(1, 1)

    return kb.as_markup()

