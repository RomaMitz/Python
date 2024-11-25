import asyncio
from aiogram import *
from aiogram.filters import Command

bot = Bot(token="7715682313:AAHXsvPbuenot_gKy_ADeQGoIS3mfGmTm54")

dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)


if __name__ == ():
    asyncio.run(main())