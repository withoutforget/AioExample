from dataclasses import dataclass

from aiogram.types import Message

from src.config import Config
from src.usecases.base import Usecase


@dataclass(slots=True)
class StartCommandUsecase(Usecase):
    config: Config

    async def __call__(self, message: Message):
        await message.answer(f"Hi! I'm bot template {self.config.bot.version} version.")
