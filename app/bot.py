import asyncio
import schedule
import config as con
from aiogram.client.default import DefaultBotProperties
from app.comands import set_commands
from app.currency_update import update_data
from app.handlers import start_handler, currency_handler, handler_message
from aiogram import Bot, Dispatcher




schedule.every().day.at('12:00').do(update_data)


async def schedule_task():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


async def main():
    asyncio.create_task(schedule_task())
    bot = Bot(token=con.token, default=DefaultBotProperties(parse_mode='Markdown'))
    dp = Dispatcher()
    dp.include_routers(start_handler.router, currency_handler.router,handler_message.router)
    await set_commands(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




