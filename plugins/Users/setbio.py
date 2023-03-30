import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE, SP
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
import io 
from pyrogram.types import Message
import random




@Client.on_message(filters.command(["setbio"]))
async def set_chat_description(bot, message):
    sourse_message = message.reply_to_message
    description = sourse_message.text 
    await bot.set_chat_description(message.chat.id, description=description)


@Client.on_message(filters.command(["setdp"]))
async def set_chat_bio(bot, message): 
    await app.set_profile_photo(photo=random.choice(SP))





