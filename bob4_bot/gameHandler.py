from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile

from myHelpers import createInlineMenu

import db

questions = [
    'Привет, как дела? Аниме=сила_1',
    'Привет, как дела? Аниме=сила_2',
    'Привет, как дела? Аниме=сила_3',
    'Привет, как дела? Аниме=сила_4',
    'Привет, как дела? Аниме=сила_5',
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
    for button in message.reply_markup.inline_keyboard[0]:
        if (callback == button.callback_data):
            await message.edit_text(message.text + "\n" + "Ваш прогресс:" + button.callback_data)
    await printQuestion(callback, message, user_id)
    
async def finishGame(callback, message, user_id):
    result = callback[5:]
    db.createUser(user_id ,result)
    await message.answer('Тест закончен\nПришли свою фотографию и произойдёт магия')

async def printQuestion(callback, message, user_id):
    question_idx = len(callback[5:])
    if (question_idx == 2): 
        return await finishGame(callback, message, user_id)
    await message.answer_photo(InputFile('./questions_images/placeholder.jpg'))
    await message.answer(questions[question_idx], reply_markup = createInlineMenu([
        [['Ответ1', callback + '1'], ['Ответ2', callback + '2']]
    ]))
