

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import random
from info import SP

START_MESSAGE = """
𝐓𝐧𝐱 𝐀𝐥𝐥 𝐔𝐬𝐞𝐫𝐬🥰🥰
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐀𝐧𝐧𝐝 𝐒𝐡𝐚𝐫𝐞

നിങ്ങളുടെ ഗ്രൂപ്പിൽ എന്നെ ആഡ് ചെയ്ത് അഡ്മിൻ ആക്കിക്കോ. എല്ലാ മൂവിയും കിട്ടും..

ഗ്രൂപ്പ് ഇല്ലെങ്കിൽ ഒരു ഗ്രൂപ്പ്‌ ഉണ്ടാക്കി @𝐦𝐢𝐧𝐧𝐚𝐥_𝐦𝐮𝐫𝐚𝐥𝐢_𝐫𝐨𝐛𝐨𝐭 നെ അല്ലെങ്കിൽ @𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓 നെ ആഡ് ചെയ്തു അഡ്മിൻ ആക്കിക്കോ.. എന്നിട്ട് ചോദിക്കുന്ന മൂവീസ് അപ്പപ്പോൾ തന്നെ നിങ്ങളുടെ വിരൽ തുമ്പിൽ 😌😌

𝐈𝐭𝐬 𝐄𝐚𝐬𝐲 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞; 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧, 𝐓𝐡𝐚𝐭𝐬 𝐀𝐥𝐥, 𝐢 𝐰𝐢𝐥𝐥 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬 𝐓𝐡𝐞𝐫𝐞...🤓

𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞

𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐢𝐠𝐠𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 𝐟𝐢𝐥𝐭𝐞𝐫 𝐛𝐨𝐭 @𝐌𝐢𝐧𝐧𝐚𝐥_𝐌𝐮𝐫𝐚𝐥𝐢_𝐑𝐨𝐛𝐨𝐭 𝐨𝐫 @𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓
𝐀𝐥𝐥 𝐟𝐢𝐥𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭. 😌😌

𝐅𝐚𝐬𝐭 𝐣𝐨𝐢𝐧....
"""

ADS = """
𝐇𝐞𝐥𝐥𝐨
𝐃𝐕𝐃 𝐂𝐨𝐦𝐢𝐧𝐠...𝐅𝐚𝐬𝐭𝐞𝐬𝐭 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥...
𝐅𝐚𝐬𝐭 𝐉𝐨𝐢𝐧 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥
"""




@Client.on_message(filters.private & filters.command(["sub"]))
async def sub(client, message):
                 
    button = [[
        InlineKeyboardButton('𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
    ],[
        InlineKeyboardButton('𝐌𝐨𝐯𝐢𝐞𝐬 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/PYRO_BOTZ'),
        InlineKeyboardButton('𝐒𝐨𝐧𝐠 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/PYRO_BOTZ_CHAT')
    ],[
        InlineKeyboardButton('𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩', callback_data='about'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/bigmoviesworld')
    ], [
        InlineKeyboardButton('𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url=f'https://t.me/+obGgfOP2LZ0wYTBl')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
    photo=SP,
    text=START_MESSAGE,
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
    )


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "s.":
        await query.message.edit_text(
            text=f"""👋 Hai {query.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 & 𝙲𝚞𝚜𝚝𝚘𝚖 𝙲𝚊𝚙𝚝𝚒𝚘𝚗 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", callback_data='dev')                
                ],[
                InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/PYRO_BOTZ'),
                InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/PYRO_BOTZ_CHAT')
                ],[
                InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
                InlineKeyboardButton('ℹ️ 𝙷𝙴𝙻𝙿', callback_data='help')
                ]]
                )
            )
    elif data == "ja.":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("❤️‍🔥 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴  ❤️‍🔥", url='https://youtu.be/BiC66uFJsio')
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "a.":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("🖥️ 𝙷𝙾𝚆 𝚃𝙾 𝙼𝙰𝙺𝙴", url="https://youtu.be/GfulqsSnTv4")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "d.":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ 𝚂𝙾𝚄𝚁𝙲𝙴", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("🖥️ 𝙷𝙾𝚆 𝚃𝙾 𝙼𝙰𝙺𝙴", url="https://youtu.be/GfulqsSnTv4")
               ],[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "c.":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()


@Client.on_message(filters.private & filters.command(["sub"]))
async def sub(client, message):
                 
    button = [[
        InlineKeyboardButton('𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/{temp.U_NAME}?startgroup=true')   
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
    photo=PIC,
    text=START_MESSAGE,
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
    )


