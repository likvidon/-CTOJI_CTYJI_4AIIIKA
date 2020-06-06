from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile

from myHelpers import createInlineMenu

questions = [
    'hello?','hello2?','hello3?','hello4?','hello5?',
]

async def gameHandler(callback, message):
    if (callback == 'game_'):
        await startGame(message)
    elif (callback.startswith('game_')):
        await mainPlayer(callback, message)

async def startGame(message):
    await message.edit_text('Начнём')
    callback = 'game_'
    await printQuestion(callback, message)

async def mainPlayer(callback, message):
    for button in message.reply_markup.inline_keyboard[0]:
        if (callback == button.callback_data):
            await message.edit_text(message.text + "\n" + "Ваш прогресс:" + button.callback_data)
    await printQuestion(callback, message)
    
async def finishGame(callback, message):
    await message.answer('Тест закончен', reply_markup = createInlineMenu([
        [['Узнать результат', "result_" + callback[5:]]]
    ]))

async def printQuestion(callback, message):
    question_idx = len(callback[5:])
    if (question_idx == 5): 
        return await finishGame(callback, message)
    await message.answer_photo(InputFile('./test.jpg'))
    await message.answer(questions[question_idx], reply_markup = createInlineMenu([
        [['Ответ1', callback + '1'], ['Ответ2', callback + '2']]
    ]))
