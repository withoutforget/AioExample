import asyncio

import structlog
from aiogram import Bot
from dishka import make_async_container

from src.config import Config, config
from src.infra.logging import setup_logger
from src.main.bot import setup_dispatcher
from src.main.di import DishkaProvider
from src.usecases.provider import UsecaseProvider

setup_logger(config.logging)
logger = structlog.get_logger()


async def main():
    container = make_async_container(  ## TO DO: мб вынести это куда-то?
        DishkaProvider(), UsecaseProvider(), context={Config: config}
    )
    bot = Bot(token=config.bot.api_key)
    dp = setup_dispatcher(container)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
