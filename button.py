from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Data o'quv markazi haqida malumot")],
        [KeyboardButton(text="Data o'quv markazi kurslari haqida malumot")],
        [KeyboardButton(text="Admin bilan bog'lanish")]
    ],
    resize_keyboard=True



)