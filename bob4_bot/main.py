import logging

from myHelpers import createInlineMenu


import showContacts as sc  

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, InputFile, ContentType


logging.basicConfig(level=logging.INFO)

bot = Bot(
    token = '1193779965:AAGf4TX5eT3_J77FRLkMHV-hXSLun321cL0',
)

dp = Dispatcher(bot = bot)

@dp.message_handler(content_types = ContentType.PHOTO)
async def toPhoto(message: types.Message):
    await message.photo[-1].download('test.jpg')

@dp.message_handler()
async def printall(message: types.Message):
    await message.answer('Привет, я бот!', reply_markup = createInlineMenu([ # простая функция для создания клавиатуры (см. helpers.py)
        [
            ['Пройти тест', 'start_test']
        ],
        [
            ['Создатели','contacts']
        ],
    ])) # отправка сообщения с фотографией кота и клавиатурой


@dp.callback_query_handler()
async def callback(cQuery):
    if (cQuery.data.startswith('contact')):
        print('off')
        await sc.showContacts(cQuery.data, cQuery.message)
    else:
        gameHandler(cQuery)
    print("Recieved data from user <" + str(cQuery.from_user.id) + "> with data: '"+ cQuery.data +"'") 

    
    await cQuery.answer('ok') # это что-то типа оповещения с текстом (по центру экрана)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)