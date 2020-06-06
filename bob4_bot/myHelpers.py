from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def createInlineMenu(array):
    menu = InlineKeyboardMarkup()
    for row in array:
        menu.row()
        for button in row:
            inlineBtn = InlineKeyboardButton(button[0], callback_data = button[1])
            menu.insert(inlineBtn)

    return menu