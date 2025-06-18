from aiogram import html,Router

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    fullname=html.bold(message.from_user.full_name)
    await message.answer(_
                         ("Hello,{name}!\n\n Registratsiyani bosing /register komandasini bosing!").format(name=fullname))

