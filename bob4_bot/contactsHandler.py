from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from myHelpers import createInlineMenu

contacts = [
    ['Мария Качалова', '+7(905)558-66-65', '@Maryf0x'],
    ['Герасимова Ольга', '404 Not found', '@forestmaid'],
    ['Дмитрий Крючков', '+7(964)503-96-68', '@Vladyka_morey'],
    ['Артем Брызгалов', '404 Not found', '@abrizgalov'],
]

async def contactsHandler(callback, message):

    if (callback == 'contacts'):
        await printContacts(message)
    else:
        await printCurrContact(message, int(callback[8:]))

async def printContacts(message):
    await message.edit_text('Мои создатели:', reply_markup = createInlineMenu([
            [[contacts[0][0], "contact_1"]],
            [[contacts[1][0], "contact_2"]],
            [[contacts[2][0], "contact_3"]],
            [[contacts[3][0], "contact_4"]],
            [['Назад', 'menu']]
        ]))    

async def printCurrContact(message, contact_id):
    info = contacts[contact_id]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram: " + info[2], reply_markup = createInlineMenu([
        [['На главную', 'menu'],['Назад', 'contacts']]
    ])) 

