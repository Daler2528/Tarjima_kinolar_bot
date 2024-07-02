from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message , BotCommand , CallbackQuery
from keyboards import channel_list
from db import Database


async def start(bot: Bot):
    await bot.send_message(chat_id="5754977794" , text = "Bot ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="5754977794" , text = "Bot Tuxtadi ❌")

async def check_join(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Botimizdan foydanishiz uchun kanalarga azo buling", reply_markup=channel_list)


async def start_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Botimizdan foydanishiz uchun kanalarga azo buling", reply_markup=channel_list)


async def admin(message: Message, bot: Bot, state: FSMContext):
    await message.copy_to(chat_id=message.from_user.id , message=message)

# async def chadd(message: Message, bot: Bot, state: FSMContext):
#     await message.copy_to(chat_id=message.from_user.id , message="")

async def check_channel_join(query: CallbackQuery,bot:Bot,*args,**kwargs):
    await bot.send_message(chat_id=query.from_user.id , text="👋 Assalomu aleykum, botimizga xush kelipsiz")
    await query.answer("")

async def start_answer(message: Message):
    db = Database()
    await message.answer(f'Hello @{message.from_user.username}')
    if await db.select_user_id(str(message.from_user.id)):
        await db.insert_user_id(str(message.from_user.id))
    else:
        await message.answer('Siz royxatda borsiz!')