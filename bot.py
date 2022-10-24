import logging
import wikipedia
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5727203893:AAH3FyOGFUKMdu7n5pra9yqEe3BN0Vhuc3M'
wikipedia.set_lang('uz')

url = 'https://v6.exchangerate-api.com/v6/7cc4db1be259f0d115eb9e24/pair/USD/UZS'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Salom Wikipedia botiga xush kelibsiz!\nMaqola nomini kiriting.")


@dp.message_handler(commands=['kurs'])
async def send_kurs(message: types.Message):
    response = requests.get(url)
    data = response.json()['conversion_rate']

    await message.reply(f"1 UDS = {data} UZS")


@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        url_res = wikipedia.page(message.text).url
        await message.answer(f'{respond}\nTo\'liq ma\'lumot uchun: {url_res}')
    except:
        await message.answer("Bunday mavzuga oid maqola topilmadi!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)