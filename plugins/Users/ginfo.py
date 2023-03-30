import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
import io 
from pyrogram.types import Message



@Client.on_message(filters.command(["settitle"]))
async def who_is(bot, message):
    sourse_message = message.reply_to_message
    title = sourse_message.text 
    await bot.set_chat_title(message.chat.id, title=title)


@Client.on_message(filters.command(["bio"]))
async def set_administrator_title(bot, message):
    sourse_message = message.reply_to_message
    title = sourse_message.text
    await bot.set_administrator_title(chat_id, user_id, title=title)


@Client.on_message(filters.command(["setname"]))
async def update_profile(bot, message):
    sourse_message = message.reply_to_message
#    first_name = message.from.user_first_name
    bio = sourse_message.text
    await bot.update_profile(chat_id, user_id, bio=bio)
#    await bot.update_profile(chat_id=chat_id, user_id=user_id, title=title)







