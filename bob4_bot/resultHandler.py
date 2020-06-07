from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile

async def resultHandler(cQuery):
    await cQuery.answer('Ожидайте...')
    await cQuery.message.edit_text('Ваш результат:\n'+'Вы молодец') # TODO:)
