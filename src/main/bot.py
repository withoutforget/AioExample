from aiogram import Dispatcher
from dishka import AsyncContainer
from dishka.integrations.aiogram import setup_dishka

from src.presentation.setup import setup_routes


def setup_dispatcher(container: AsyncContainer) -> Dispatcher:
    dp = Dispatcher()
    setup_dishka(container, dp, auto_inject=True)
    setup_routes(dp)
    return dp
