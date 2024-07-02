from aiogram.types import ReplyKeyboardMarkup , KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


channel_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Obuna bo'lish" , url='https://t.me/+ClZKu_QMDNM3MDky'),
            InlineKeyboardButton(text="➕ Obuna bo'lish" , url='https://t.me/sherzotvich_ss'),
            InlineKeyboardButton(text="➕ Obuna bo'lish" , url='https://www.instagram.com/nasimov_2528?igsh=YmhsdWNxOWFpNmF')
        ],
        [
            InlineKeyboardButton(text="Tekshrish ✅" , callback_data="check_subscription"),

        ]
    ]
)
