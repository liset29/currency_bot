from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Текстовое сообщение")


@router.message(F.voice)
async def message_with_voice(message: Message):
    await message.answer("Голосовое сообщение")


@router.message(F.photo)
async def message_with_photo(message: Message):
    await message.answer("Изображение")


@router.message(F.animation)
async def message_with_animation(message: Message):
    await message.answer("Гифка")

