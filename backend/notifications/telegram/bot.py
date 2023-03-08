from aiogram import Bot, types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "6134430614:AAHsYxXjzYFXC84dTPeduv1dUC6XDHXNlwc"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text, reply_markup=main_keyboard)


@dp.callback_query_handler(text="YES")
async def call_echo(call: types.CallbackQuery):
    await call.message.answer("Вы подтвердили встречу!")

@dp.callback_query_handler(text="YES")
async def call_echo(call: types.CallbackQuery):
    await call.message.answer("Вы подтвердили встречу!")

@dp.callback_query_handler(text="YES")
async def call_echo(call: types.CallbackQuery):
    await call.message.answer("Вы подтвердили встречу!")
