from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.i18n import gettext as _

def share_contact():
    keyboards=[
        [KeyboardButton(text=_('telefon ulashish'),request_contact=True)]
    ]
    kbs = ReplyKeyboardMarkup(keyboard=keyboards,resize_keyboard=True,input_field_placeholder=_('tugamadan foydalanishingiz ham mumkin'))
    return kbs

def confirm_button():
    keyboards=[
        [KeyboardButton(text=_('ha')),
         KeyboardButton(text=_('yoq'))]
    ]
    kbs = ReplyKeyboardMarkup(keyboard=keyboards,resize_keyboard=True,input_field_placeholder=_('tugmadan foydalaning'))
    return kbs

def menu():
    keyboards=[
        [KeyboardButton(text=_("Test yechish")),
         KeyboardButton(text=_("Natijalar"))]
    ]
    kbs=ReplyKeyboardMarkup(keyboard=keyboards,resize_keyboard=True,input_field_placeholder=_('tugmadan foydalaning'))