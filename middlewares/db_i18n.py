from typing import Dict,Any

from aiogram.types import  TelegramObject
from aiogram.utils.i18n import I18nMiddleware


class DatabaseI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        return self.i18n.default_locale