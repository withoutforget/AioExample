from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from src.usecases.start_command import StartCommandUsecase

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, usecase: FromDishka[StartCommandUsecase]):
    await message.answer(text=await usecase())
