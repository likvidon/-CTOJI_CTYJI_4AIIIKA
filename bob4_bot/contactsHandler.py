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
    elif (callback == 'contact_1'):
        await printContact_1(message)
    elif (callback == 'contact_2'):
        await printContact_2(message)
    elif (callback == 'contact_3'):
        await printContact_3(message)
    elif (callback == 'contact_4'):
        await printContact_4(message)

async def printContacts(message):
    await message.edit_text('Мои создатели:', reply_markup = createInlineMenu([
            [[contacts[0][0], "contact_1"]],
            [[contacts[1][0], "contact_2"]],
            [[contacts[2][0], "contact_3"]],
            [[contacts[3][0], "contact_4"]],
            [['Назад', 'menu']]
        ]))    

async def printContact_1(message):
    info = contacts[0]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram: " + info[2], reply_markup = createInlineMenu([
        [['На главную', 'menu'],['Назад', 'contacts']]
    ])) 

async def printContact_2(message):
    info = contacts[1]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram: " + info[2], reply_markup = createInlineMenu([
        [['На главную', 'menu'],['Назад', 'contacts']]
    ]))   

async def printContact_3(message):
    info = contacts[2]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram: " + info[2], reply_markup = createInlineMenu([
        [['На главную', 'menu'],['Назад', 'contacts']]
    ]))   

async def printContact_4(message):
    info = contacts[3]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram: " + info[2], reply_markup = createInlineMenu([
        [['На главную', 'menu'],['Назад', 'contacts']]
    ]))   

