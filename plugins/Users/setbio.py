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

import os
import shutil
from pyrogram import Client, filters, enums
from telegraph import upload_file
from plugins.helpers.get_file_id import get_file_id
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TMP_DOWNLOAD_DIRECTORY = "./DOWNLOADS/"


@Client.on_message(filters.command(["setbio"]))
async def set_chat_description(bot, message):
    sourse_message = message.reply_to_message
    description = sourse_message.text 
    await bot.set_chat_description(message.chat.id, description=description)


@Client.on_message(filters.command(["setdp"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    koshik = await message.reply_text("**Processing...😪**")
        return
    replied = message.reply_to_message
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as photo:
        await client.set_profile_photo(photo=response)
    else:
        await client.set_profile_photo(photo=response)


    finally:
        shutil.rmtree(
            _t,
            ignore_errors=True
        )
        



