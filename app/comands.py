from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="exchange", description="Конвертирует валюту. Пример - /exchange USD RUB 10"),
        BotCommand(command="rates", description="Показывает актуальный курс всех валют")
    ]
    await bot.set_my_commands(commands)