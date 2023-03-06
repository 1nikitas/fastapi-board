from aiogram import Bot, types, Dispatcher

bot = Bot(token="6134430614:AAHsYxXjzYFXC84dTPeduv1dUC6XDHXNlwc")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)