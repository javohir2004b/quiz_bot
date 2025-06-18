import asyncio
import logging
import sys
from os import getenv
from typing import Dict, Any

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import TelegramObject
from aiogram.utils.i18n import I18n,I18nMiddleware
from dotenv import load_dotenv
load_dotenv()

from handler import start_router, register_router, menu_router
from utils.notify_admins import bot_start_up, bot_shut_down



TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher(storage=MemoryStorage())

class DatabaseI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        return self.i18n.default_locale






async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.startup.register(bot_start_up)
    dp.shutdown.register(bot_shut_down)
    dp.include_routers(start_router,register_router,menu_router)

    i18n = I18n(path="locales", default_locale="u", domain="messages")
    dp.update.outer_middleware.register(DatabaseI18nMiddleware(i18n))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
