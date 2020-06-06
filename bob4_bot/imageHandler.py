from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from myHelpers import createInlineMenu
import db

async def imageHandler(message):
    res = db.findResult(message.from_user.id)
    if (res):
        await message.photo[-1].download(str(message.from_user.id) + '.jpg')
        await message.answer('кажется кто-то забыл привязать EORA api к боту...')
        await message.answer('Красивая фотка... Жаль, что я бездушная машина...')

    else:
        await message.answer('Рановато кидаешь фотку\nПройди тест!', reply_markup = createInlineMenu([
            [['Меню', 'menu']]
        ]))