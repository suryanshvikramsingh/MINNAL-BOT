
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import random
import os
from info import SP
from Script import script
import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE, LOGIN_CHANNEL, ADMINS
from utils import extract_user, get_file_id, get_poster, last_online
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings

import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
from info import IMDB, SUPPORT_CHAT_ID

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



START_MESSAGE = """
𝐇𝐞𝐥𝐥𝐨 <a href='tg://settings'>𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮⚡️</a>
<i>📌ഏതു മൂവി ആണോ വേണ്ടത് അത് സ്പെല്ലിങ് തെറ്റാതെ ഗ്രൂപ്പിൽ ചോദിച്ചാൽ മാത്രമേ കിട്ടുകയുള്ളു...!! \n\n
സിനിമകൾ/സീരിസുകൾ ലഭിക്കാൻ പേര് മാത്രം അയച്ചാൽ മതി, അങ്ങനെ കിട്ടിയില്ലെങ്കിൽ വർഷം/സീസൺ(s)+എപ്പിസോഡ്(E)
കൂടി ചേർത്ത് അയക്കുക, അതിന്റെ കൂടെ ഉണ്ടോ? കിട്ടുമോ? തരോ ഇങ്ങനെയുള്ളതോ അല്ലെങ്കിൽ വേറെ ഭാഷയോ ചേർക്കേണ്ടതില്ല.</i>

𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :-

𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 ✅
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝟐𝟎𝟐𝟑 ✅
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝐌𝐚𝐥𝐚𝐲𝐚𝐥𝐚𝐦 ✅
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝐌𝐚𝐥𝐚𝐲𝐚𝐥𝐚𝐦 𝐌𝐨𝐯𝐢𝐞 𝐍𝐞𝐰 ❌️
𝐑𝐨𝐦𝐚𝐧𝐣𝐚𝐦 𝐍𝐞𝐰 𝐌𝐨𝐯𝐢𝐞 ❌️
𝐀𝐯𝐞𝐧𝐠𝐞𝐫𝐬 𝐄𝐧𝐝𝐠𝐚𝐦𝐞 ✅
𝐀𝐯𝐞𝐧𝐠𝐞𝐫𝐬:𝐄𝐧𝐝𝐠𝐚𝐦𝐞 ❌️

𝐑𝐮𝐥𝐞𝐬 𝐀𝐧𝐝 𝐁𝐨𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 <a href='http://telegra.ph/Minnal-murali-03-06-12'>𝐂𝐥𝐢𝐜𝐤⚡️</a>

<i>📌നിങ്ങൾ റിക്വസ്റ്റ് ചെയ്ത മൂവി കിട്ടിയില്ലെങ്കിൽ വൈകാതെ തന്നെ ആഡ് ചെയ്യുന്നതായിരിക്കും..</i> 

🍿𝐃𝐨𝐧'𝐭 𝐀𝐤𝐬 𝐓𝐡𝐞𝐚𝐭𝐫𝐞 🎭 𝐑𝐞𝐥𝐞𝐚𝐬𝐞𝐝 𝐌𝐨𝐯𝐢𝐞𝐬
𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨 𝐧𝐨𝐭 𝐬𝐭𝐚𝐲 𝐢𝐧 𝐭𝐡𝐢𝐬 𝐠𝐫𝐨𝐮𝐩 𝐛𝐲 𝐚𝐬𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐚𝐧 𝐮𝐧𝐫𝐞𝐥𝐞𝐚𝐬𝐞𝐝 𝐟𝐢𝐥𝐦.  𝐘𝐨𝐮 𝐰𝐢𝐥𝐥 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐚 𝐰𝐚𝐫𝐧𝐢𝐧𝐠 𝐢𝐟 𝐲𝐨𝐮 𝐚𝐬𝐤.\n\n
𝐘𝐨𝐮 𝐖𝐢𝐥𝐥 𝐆𝐞𝐭 𝐅𝐢𝐫𝐞 🔥,𝐈𝐟 𝐘𝐨𝐮 𝐀𝐬𝐤𝐢𝐧𝐠 𝐍𝐨𝐧 𝐑𝐞𝐥𝐞𝐚𝐬𝐞𝐝 𝐌𝐨𝐯𝐢𝐞.

வெளியிடப்படாத படம் கேட்டு தயவுசெய்து இந்த குழுவில் தங்க வேண்டாம்.  நீங்கள் கேட்டால் எச்சரிக்கையைப் பெறுவீர்கள். \n
𝐎𝐰𝐧𝐞𝐫 𝐍𝐚𝐦𝐞 :- {}
𝐆𝐫𝐨𝐮𝐩 𝐍𝐚𝐦𝐞 :- {}
"""
UP_MESSAGE = """
{} 𝐌𝐨𝐯𝐢𝐞 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩
"""





@Client.on_message(filters.command("rules") & filters.group) 
async def r_message(client, message):
    mention = message.from_user.mention
    buttons = [[
        InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/nasrani_update')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(START_MESSAGE.format(message.from_user.mention, message.chat.title),
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
    )





# @Client.on_callback_query()
# async def callback(bot: Client, query: CallbackQuery):
#     if query.data== "r":
#         await query.message.edit(
#             text=f"ok da"
#         )







@Client.on_message(filters.chat(SUPPORT_CHAT_ID))
async def start_message(client, message):
    mention = message.from_user.mention
    chat_id = message.chat.id
#    mv_rqst = message.text
    searchh = message.text                 
#    reqstr1 = message.from_user.id if message.from_user else 0
#    reqstr = await client.get_users(reqstr1)   
    imdb = await get_poster(searchh) if IMDB else None    
            
    if imdb:
        cap = TEMPLATE.format(
            query=search,
            title=imdb['title'],
            votes=imdb['votes'],
            aka=imdb["aka"],
            seasons=imdb["seasons"],
            box_office=imdb['box_office'],
            localized_title=imdb['localized_title'],
            kind=imdb['kind'],
            imdb_id=imdb["imdb_id"],
            cast=imdb["cast"],
            runtime=imdb["runtime"],
            countries=imdb["countries"],
            certificates=imdb["certificates"],
            languages=imdb["languages"],
            director=imdb["director"],
            writer=imdb["writer"],
            producer=imdb["producer"],
            composer=imdb["composer"],
            cinematographer=imdb["cinematographer"],
            music_team=imdb["music_team"],
            distributors=imdb["distributors"],
            release_date=imdb['release_date'],
            year=imdb['year'],
            genres=imdb['genres'],
            poster=imdb['poster'],
            plot=imdb['plot'],
            rating=imdb['rating'],
            url=imdb['url'],
            **locals()
        )
#    else:
#        cap = script.NOR_TXT.format(search, total_results, message.from_user.mention, message.chat.title)
        if imdb and imdb.get('poster'):

            try:

                fmsg = await message.reply_photo(photo=imdb.get('poster'),

                                          reply_markup=InlineKeyboardMarkup(btn))

            except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):

                pic = imdb.get('poster')

                poster = pic.replace('.jpg', "._V1_UX360.jpg")

                fmsg = await message.reply_photo(photo=poster, reply_markup=InlineKeyboardMarkup(btn))

            except Exception as e:

                logger.exception(e)

                fmsg = await message.reply_photo(
                       caption=f"👮‍♂ {message.from_user.mention} ɴᴏᴛɪᴄᴇ :ɪ𝙵 ʏᴏᴜ ᴅᴏ ɴᴏᴛ sᴇᴇ ᴛʜᴇ 𝙵ɪʟᴇ𝚂 ᴏ𝙵 ᴛʜɪ𝚂 ᴍᴏᴠɪᴇ ʏᴏᴜ ᴀ𝚂ᴋᴇᴅ 𝙵ᴏʀ. ʟᴏᴏᴋ ᴀᴛ ɴᴇ𝚇ᴛ ᴘᴀɢᴇ🔎\n©️քօաɛʀɛɖ ɮʏ :{message.chat.title}",
                       photo="https://telegra.ph/file/8a8ba3e824e1d2482253f.jpg",
                       parse_mode=enums.ParseMode.HTML,
                       reply_markup=InlineKeyboardMarkup(btn))

        else:

        

            fmsg = await message.reply_photo(
                   caption=f"👮‍♂ {message.from_user.mention} ɴᴏᴛɪᴄᴇ :ɪ𝙵 ʏᴏᴜ ᴅᴏ ɴᴏᴛ sᴇᴇ ᴛʜᴇ 𝙵ɪʟᴇ𝚂 ᴏ𝙵 ᴛʜɪ𝚂 ᴍᴏᴠɪᴇ ʏᴏᴜ ᴀ𝚂ᴋᴇᴅ 𝙵ᴏʀ. ʟᴏᴏᴋ ᴀᴛ ɴᴇ𝚇ᴛ ᴘᴀɢᴇ🔎\n©️քօաɛʀɛɖ ɮʏ :{message.chat.title}",
                   photo="https://telegra.ph/file/8a8ba3e824e1d2482253f.jpg",
                   parse_mode=enums.ParseMode.HTML,
                   reply_markup=InlineKeyboardMarkup(btn))
