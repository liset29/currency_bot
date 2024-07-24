from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from app.database import r
router = Router()


@router.message(Command(commands=['exchange']))
async def handle_exchange(message: Message):
    try:
        func,currency1, currency2, value = message.text.split()
        currency1 = currency1.upper()
        currency2 = currency2.upper()
        value = float(value)

        if currency1 == 'RUB':
            rate_currency1 = 1.0
        else:
            rate_currency1 = float(r.get(currency1))

        if currency2 == 'RUB':
            rate_currency2 = 1.0
        else:
            rate_currency2 = float(r.get(currency2))

        result = round((value * rate_currency1 / rate_currency2),2)
        await message.answer(f'{value} {currency1} = {result} {currency2}')
    except:
        await message.reply(f'Неверный запрос. Пример запроса: */exchange USD RUB 10*')


@router.message(Command(commands=['rates']))
async def handle_rates(message: Message):
    keys = r.keys()
    lst = [f'{key.decode("utf-8")}: {float(r.get(key))}' for key in keys]
    await message.answer('*Актуальный курс валют на сегодняшний день:*\n' + '\n'.join(lst))
