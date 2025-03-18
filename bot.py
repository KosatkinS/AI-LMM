import aiogram

import os
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
from handlers import router

TOKEN="7959609187:AAGvjiuE0PgGhapW4JNgeMk1okTn1KpiBgg"


async def main():
    bot = aiogram.Bot(TOKEN)

    dp = aiogram.Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
