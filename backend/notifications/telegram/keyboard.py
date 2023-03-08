from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить занятие", callback_data="YES")
         ],
        [
            InlineKeyboardButton(text="Внести изменения", callback_data="fix")
        ],
        [
            InlineKeyboardButton(text="Отказаться", callback_data="NO")
        ]
    ]
)

