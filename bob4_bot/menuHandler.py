from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from myHelpers import createInlineMenu

async def menuHandler(message):
    await message.edit_text('Главное меню', reply_markup = createInlineMenu([
        [['Пройти тест', 'game_']],
        [['Создатели', 'contacts']]
    ]))