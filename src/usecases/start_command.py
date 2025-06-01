from dataclasses import dataclass

from src.config import Config
from src.usecases.base import Usecase


@dataclass(slots=True)
class StartCommandUsecase(Usecase):
    config: Config

    async def __call__(self) -> str:
        return f"Hi! I'm bot template {self.config.bot.version} version."
