import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6695231436:AAH95THg8suRLmYEnqznkqggUZulLCxVeVE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("Salom Foydalanuvchi!\nBu bot siz hohlagan maqolani topib beradi.\nBu bot Python tilida yozilgan\nMurojat uchun: @artyom_uzb")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Cats is here 😺',
                             reply_to_message_id=message.message_id)


@dp.message_handler()
async def echo(message: types.Message):
    #await bot.send_message(message.chat.id, message.text)
    await message.reply("Ma\'lumot topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

