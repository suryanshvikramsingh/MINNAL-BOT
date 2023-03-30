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
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)



@Client.on_message(filters.command(["settitle"]))
async def who_is(bot, message):
    sourse_message = message.reply_to_message
    title = sourse_message.text 
    await bot.set_chat_title(message.chat.id, title=title)


@Client.on_message(filters.command(["setd"]))
async def set_chat_description(bot, message):
    sourse_message = message.reply_to_message
    description = sourse_message.text 
    await bot.set_chat_description(message.chat.id, description=description)


@Client.on_message(filters.command(["setb"]))
async def set_chat_bio(bot, message):
    sourse_message = message.reply_to_message
    bio = sourse_message.text 
    await bot.set_chat_bio(message.chat.id, bio=bio)



# For bots only, send messages with keyboards attached





@Client.on_message(filters.command(["seti"]))
async def who_is(bot, message):
    chat_id = message.chat.id
    await bot.send_message(
        chat_id, "These are inline buttons",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Data", callback_data="callback_data")],
                [InlineKeyboardButton("Docs", url="https://docs.pyrogram.org")]
            ]))
