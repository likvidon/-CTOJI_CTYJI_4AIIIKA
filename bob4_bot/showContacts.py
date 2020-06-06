from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from myHelpers import createInlineMenu

contacts = [
    ['Иван Иванов1', '88005553535', '@ivan1'],
    ['Иван Иванов2', '88005553535', '@ivan2'],
    ['Иван Иванов3', '88005553535', '@ivan3'],
    ['Иван Иванов4', '88005553535', '@ivan4'],
]

async def showContacts(callback, message):
    print(callback)

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
            [["Иван Иванов1", "contact_1"]],
            [["Иван Иванов2", "contact_2"]],
            [["Иван Иванов3", "contact_3"]],
            [["Иван Иванов4", "contact_4"]]
        ]))    

async def printContact_1(message):
    info = contacts[0]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram^ " + info[2]) 

async def printContact_2(message):
    info = contacts[1]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram^ " + info[2])  

async def printContact_3(message):
    info = contacts[2]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram^ " + info[2])  

async def printContact_4(message):
    info = contacts[3]
    await message.edit_text(info[0] + "\nТелефон: " + info[1] + "\nTelegram^ " + info[2])  

