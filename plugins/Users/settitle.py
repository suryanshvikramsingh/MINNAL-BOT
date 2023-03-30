import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE, BOT_TOKEN
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
import io 
from pyrogram.types import Message
from pyrogram import enums


@Client.on_message(filters.command(["setname"]))
async def who_is(bot, message):
    sourse_message = message.reply_to_message
    title = sourse_message.text 
    await bot.set_chat_title(message.chat.id, title=title)


@Client.on_message(filters.command(["setbio"]))
async def set_chat_description(bot, message):
    sourse_message = message.reply_to_message
    description = sourse_message.text 
    await bot.set_chat_description(message.chat.id, description=description)







@Client.on_message(filters.command(["poll"]))
async def who_is(bot, message):
    chat_id = message.chat.id
    await bot.send_poll(chat_id, "new movies add cheyyano?", ["Yes", "No", "Maybe"])
    await bot.vote_poll(chat_id, message_id, 6)


@Client.on_message(filters.command(["stext"]))
async def who_is(bot, message):
    async for message in bot.search_messages(chat_id, query="hello", limit=120):
        print(message.text)

