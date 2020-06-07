from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile

from swap_images.model_new import predict_batch
from myHelpers import createInlineMenu
import db

async def imageHandler(message):
    res = db.findResult(message.from_user.id)
    if (res):
        img_path = "users_images/" + str(message.from_user.id) + '.jpg'
        await message.photo[-1].download(img_path)
        print(predict_batch(img_path))
        await message.answer_photo(InputFile(img_path + '_'))

    else:
        await message.answer('Рановато кидаешь фотку\nПройди тест!', reply_markup = createInlineMenu([
            [['Меню', 'menu']]
        ]))
