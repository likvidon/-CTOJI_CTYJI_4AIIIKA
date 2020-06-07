from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile

from swap_images.model_new import predict_batch
from myHelpers import createInlineMenu
import db

professions = [
    'cyber_investigator', 
    'ecologist', 
    'game_master', 
    'protez_worker',
    'janitor' # дворник
]

profBeautiful = {
    'cyber_investigator': 'Кибер исследователем', 
    'ecologist': 'Экологом', 
    'game_master': 'Игромастером', 
    'protez_worker': 'Разработчиком киберпротезов и имплантатов',
    'janitor': 'Дворник\nК сожалению, наш тест не помог тебе выбрать профессию, зато ты сломал систему'# дворник
}

async def imageHandler(message):
    res = str(db.findResult(message.from_user.id))
    print(res)
    if (res):
        if (res[4] == '2' and res[7] == '2'):
            res = professions[0]
        elif (res[1] == '1' and res[4] == '1'):
            res = professions[1]
        elif (res[2] == '1' and res[3] == '1'):
            res = professions[2]
        elif (res[3] == '1' and res[6] == '1'):
            res = professions[3]
        else:
            res = professions[4]

        img_path = "users_images/" + str(message.from_user.id) + '.jpg'
        await message.photo[-1].download(img_path)
        print(predict_batch(img_path, res))
        await message.answer_photo(InputFile(img_path + '_'), "Скорее всего в будущем ты будешь:\n" + profBeautiful[res])

    else:
        await message.answer('Рановато кидаешь фотку\nПройди тест!', reply_markup = createInlineMenu([
            [['Меню', 'menu']]
        ]))
