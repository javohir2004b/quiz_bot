from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def courses_ibtn():
    kbs=[
        [InlineKeyboardButton(text='Python',callback_data='py'),
         InlineKeyboardButton(text='Go',callback_data='go'),
         ],
        [InlineKeyboardButton(text='C',callback_data='c'),]
    ]
    ikbs = InlineKeyboardMarkup(inline_keyboard=kbs)

    return ikbs