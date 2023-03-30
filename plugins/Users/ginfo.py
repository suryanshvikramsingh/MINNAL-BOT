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


# For bots only, send messages with keyboards attached


@Client.on_message(filters.command(["setn"]))
async def who_is(bot, message):
    await bot.send_message(
        chat_id, "Look at that button!",
        reply_markup=ReplyKeyboardMarkup([["Nice!"]]))

@Client.on_message(filters.command(["seti"]))
async def who_is(bot, message):
    await bot.send_message(
        chat_id, "These are inline buttons",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Data", callback_data="callback_data")],
                [InlineKeyboardButton("Docs", url="https://docs.pyrogram.org")]
            ]))
