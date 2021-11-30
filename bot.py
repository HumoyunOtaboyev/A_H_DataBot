import logging
from config import Token
from aiogram import Bot, Dispatcher, executor, types
from button import menu

API_TOKEN=Token

logging.basicConfig(level=logging.INFO)

bot=Bot(API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start',"help"])
async def boshlash(message: types.Message):
    user=message.from_user.first_name
    await message.reply(f'Assalomu alaykum {user}', reply_markup=menu)

@dp.message_handler(Text(equals=["Data o'quv markazi haqida malumot"]))
async def accounts(message:types.Message):
    await message.answer("")

@dp.message_handler(Text(equals=["Data o'quv markazi kurslari haqida malumot"]))
async def course(message:types.Message):
    await message.answer("")








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)