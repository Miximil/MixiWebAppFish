
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)

TOKEN = "9108912758:AAENSGNkG8JyIVKBtO1VIjHNGTXrsQndpgQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Открыть сайт",
                    web_app=WebAppInfo(
                        url="https://miximil.github.io/MixiWebAppFish/"
                    )
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "Привет! Нажми на кнопку ниже 👇",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
