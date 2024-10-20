from flask import Flask, render_template, request
import socket
import asyncio
import logging
from datetime import datetime
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
logging.basicConfig(level=logging.INFO)
bot = Bot(token="TOKEN")
dp = Dispatcher()
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="tap ☝️", web_app=WebAppInfo(url=f"url_web_app"))
    )
    await message.answer("Clicker HTML, sourse: https://github.com/ramplerrsky/HTML-clicker", reply_markup=builder.as_markup())
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
app = Flask(__name__)
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
@app.route('/')
def index():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return render_template('clicker.html', ip_address=local_ip)
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
async def main():
    await dp.start_polling(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(app.run(debug=True, use_reloader=False))
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker
if __name__ == '__main__':
    asyncio.run(main())
#simple html clicker by: https://github.com/ramplerrsky/HTML-clicker