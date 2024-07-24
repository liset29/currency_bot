from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from app.database import collection_users

router = Router()


@router.message(Command(commands=['start']))
async def handle_start(message: Message):
    username = message.from_user.username
    check_username = await collection_users.find_one({'username': username})
    print('helo')
    if not check_username:
        new_user = await collection_users.insert_one({'username': username})
    await message.answer('Привет,выберите одну из возможных команд')



