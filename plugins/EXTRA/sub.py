
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random
import os
from info import SP
from Script import script
import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE, LOGIN_CHANNEL, ADMINS, SP
from utils import extract_user, get_file_id, get_poster, last_online
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings

import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from info import IMDB

Muhammed = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

ALL_PIC = [
 "https://telegra.ph/file/d6693066f82ed4079c528.jpg",
 "https://telegra.ph/file/65a9972e351b02640d0f4.jpg"
 ]



MESSAGE = """
𝐓𝐧𝐱 𝐀𝐥𝐥 𝐔𝐬𝐞𝐫𝐬🥰🥰\n
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐀𝐧𝐧𝐝 𝐒𝐡𝐚𝐫𝐞\n
നിങ്ങളുടെ ഗ്രൂപ്പിൽ എന്നെ ആഡ് ചെയ്ത് അഡ്മിൻ ആക്കിക്കോ. എല്ലാ മൂവിയും കിട്ടും..\n
ഗ്രൂപ്പ് ഇല്ലെങ്കിൽ ഒരു ഗ്രൂപ്പ്‌ ഉണ്ടാക്കി <a href='http://t.me/minnal_murali_robot'>@𝐌𝐢𝐧𝐧𝐚𝐥_𝐌𝐮𝐫𝐚𝐥𝐢_𝐑𝐨𝐛𝐨𝐭</a> നെ അല്ലെങ്കിൽ <a href='http://t.me/NASRANI_BOT'>@𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓</a> നെ ആഡ് ചെയ്തു അഡ്മിൻ ആക്കിക്കോ.. എന്നിട്ട് ചോദിക്കുന്ന മൂവീസ് അപ്പപ്പോൾ തന്നെ നിങ്ങളുടെ വിരൽ തുമ്പിൽ 😌😌\n\n
𝐈𝐭𝐬 𝐄𝐚𝐬𝐲 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞; 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧, 𝐓𝐡𝐚𝐭𝐬 𝐀𝐥𝐥, 𝐢 𝐰𝐢𝐥𝐥 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬 𝐓𝐡𝐞𝐫𝐞...🤓\n
𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞
𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐢𝐠𝐠𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 𝐟𝐢𝐥𝐭𝐞𝐫 𝐛𝐨𝐭 @𝐦𝐢𝐧𝐧𝐚𝐥_𝐦𝐮𝐫𝐚𝐥𝐢_𝐫𝐨𝐛𝐨𝐭 𝐨𝐫 @𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓
𝐀𝐥𝐥 𝐟𝐢𝐥𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭. 😌😌
𝐅𝐚𝐬𝐭 𝐣𝐨𝐢𝐧....
"""



@Client.on_message(filters.private & filters.command(["sub"]))
async def sub(client, message):
    search = message.text           
    buttons = [[
        InlineKeyboardButton('𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
    ],[
        InlineKeyboardButton('𝐌𝐨𝐯𝐢𝐞𝐬 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/NasraniSeries'),
        InlineKeyboardButton('𝐒𝐨𝐧𝐠 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/NasraniChatGroup')
    ],[
        InlineKeyboardButton('𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/testpubliconly'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/bigmoviesworld')
    ],[
        InlineKeyboardButton('𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url=f'https://t.me/+obGgfOP2LZ0wYTBl')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
    photo=random.choice(SP),
    caption=MESSAGE.format(message.text),
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
)







# @Client.on_callback_query()
# async def callback(bot: Client, query: CallbackQuery):
#     if query.data== "r":
#         await query.message.edit(
#             text=f"ok da"
#         )








