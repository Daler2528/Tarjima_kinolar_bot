import os
from asyncio import run
from aiogram.types import Message , BotCommand
from dotenv import load_dotenv
from functions import start,stop,check_join,admin,start_menu,check_channel_join,start_answer
from filters import CheckSubFilter
from aiogram import Bot , Dispatcher
from aiogram.filters import Command ,CommandStart
from aiogram import F


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()


# bu hamasi register qlish uchun
async def main(dp) -> None:
    bot = Bot(token=TOKEN,skip_updates=True)
    await bot.set_my_commands(

        [
            BotCommand(command="/start" , description="Bot ni ishga tushrish"),
            BotCommand(command="/admin" , description="/admin"),
            #BotCommand(command="/Kanal ulash", description="/chadd")
        ]
    )
    dp.startup.register(start)
    dp.message.register(start_answer, CommandStart())
    dp.message.register(admin, Command('admin'))
    dp.message.register(start_menu, Command('start'))
    dp.callback_query.register(check_channel_join, F.data == "check_subscription")
    #dp.message.register(chadd, Command('chadd'))
    dp.message.register(check_join,CheckSubFilter())
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))


