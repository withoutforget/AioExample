from aiogram import Dispatcher

from src.presentation.start_command import router as start_router


def setup_routes(dp: Dispatcher):
    dp.include_router(start_router)
