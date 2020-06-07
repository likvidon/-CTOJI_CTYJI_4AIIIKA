import logging
import os

from myHelpers import createInlineMenu


import contactsHandler as ch  
import gameHandler as gh
import menuHandler as mh
import resultHandler as rh
import imageHandler as ih

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, InputFile, ContentType

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token = str(os.environ.get('TELEGRAM_TOKEN')),
)

dp = Dispatcher(bot = bot)

@dp.message_handler(content_types = ContentType.PHOTO)
async def toPhoto(message: types.Message):
    await ih.imageHandler(message)

@dp.message_handler(commands = ['start'])
async def printall(message: types.Message):
    await message.answer('Привет, я создан с целью помочь тебе поразвлечься и получить полезную информацию. Жмякай ниже и да начнется веселье!', reply_markup = createInlineMenu([ # простая функция для создания клавиатуры (см. helpers.py)
        [['Приступим', 'menu']]
    ])) # отправка начального сообщения

@dp.message_handler()
async def logging(message: types.Message):
    print(message.text)

@dp.callback_query_handler()
async def callback(cQuery):
    if (cQuery.data.startswith('contact')):
        await ch.contactsHandler(cQuery.data, cQuery.message)
    elif (cQuery.data.startswith('game')):
        await gh.gameHandler(cQuery.data, cQuery.message, cQuery.from_user.id)
    elif (cQuery.data.startswith('menu')):
        await mh.menuHandler(cQuery.message)
    elif (cQuery.data.startswith('result')):
        await rh.resultHandler(cQuery)
    
    print("Recieved data from user <" + str(cQuery.from_user.id) + "> with data: '"+ cQuery.data +"'") 
    
    # await cQuery.answer('ok') # это что-то типа оповещения с текстом (по центру экрана)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
