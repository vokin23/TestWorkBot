from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Weather', callback_data='weather'),
            InlineKeyboardButton(text='Help', callback_data='help')
        ]
    ]
)

weather_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Погода на данный момент', callback_data='today')
        ]
    ]
)