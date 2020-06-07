from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile

from myHelpers import createInlineMenu

import db

question = ' Выбирай '

answers = [
    ['Собрать своего робота-питомца','Завести кайфового песика'],
   # ['Улучшить жизнь людей на Земле','Найти источники жизни на других планетах'], 
   # ['Работать в команде','Делать все в одиночку'],
   # ['Играть, чиллить','Постигать новые навыки'],
    ['Реальный мир','Виртуальный'],
   # ['Структурировать','Прыгать в неизвестность'],
    #['Находить причину проблем','Защищать пострадавшего'],
    ['Распостранять информацию в массы','Стать источником новой информации, изобретателем'], # Любимчик публики \ Изобретатель
]

images = [
    './questions_images/1.jpg',
#     './questions_images/2.jpg',
#     './questions_images/3.jpg',
    './questions_images/4.jpg',
#     './questions_images/5.jpg',
#     './questions_images/6.jpg',
    './questions_images/7.jpg',
#     './questions_images/8.jpg',
]

async def gameHandler(callback, message, user_id):
    if (callback == 'game_'):
        await startGame(message, user_id)
    elif (callback.startswith('game_')):
        await mainPlayer(callback, message, user_id)

async def startGame(message, user_id):
    await message.edit_text('Начнём')
    callback = 'game_'
    await printQuestion(callback, message, user_id)

async def mainPlayer(callback, message, user_id):
    for button in message.reply_markup.inline_keyboard:
        if (callback == button[0].callback_data):
            await message.edit_text(message.text + "\n" + "Ваш ответ:  " + button[0].text)
    await printQuestion(callback, message, user_id)
    
async def finishGame(callback, message, user_id):
    result = callback[5:]
    db.createUser(user_id ,result)
    await message.answer('Тест закончен\nПришли свою фотографию и произойдёт магия')

async def printQuestion(callback, message, user_id):
    question_idx = len(callback[5:])
    if (question_idx == 3): 
        return await finishGame(callback, message, user_id)
    await message.answer_photo(InputFile(images[question_idx]))
    await message.answer("(" + str(question_idx+1) + "/3), " + question, reply_markup = createInlineMenu([
        [[answers[question_idx][0], callback + '1']], [[answers[question_idx][1], callback + '2']]
    ]))
