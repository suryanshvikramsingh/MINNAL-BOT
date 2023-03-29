

from asyncio import sleep
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import random
from info import SP

MESSAGE = f"""
𝐓𝐧𝐱 𝐀𝐥𝐥 𝐔𝐬𝐞𝐫𝐬🥰🥰\n
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐀𝐧𝐧𝐝 𝐒𝐡𝐚𝐫𝐞\n
നിങ്ങളുടെ ഗ്രൂപ്പിൽ എന്നെ ആഡ് ചെയ്ത് അഡ്മിൻ ആക്കിക്കോ. എല്ലാ മൂവിയും കിട്ടും..\n
ഗ്രൂപ്പ് ഇല്ലെങ്കിൽ ഒരു ഗ്രൂപ്പ്‌ ഉണ്ടാക്കി @𝐦𝐢𝐧𝐧𝐚𝐥_𝐦𝐮𝐫𝐚𝐥𝐢_𝐫𝐨𝐛𝐨𝐭 നെ അല്ലെങ്കിൽ <a href='http://t.me/{temp.U_NAME}?startgroup=true'>@𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓</a> നെ ആഡ് ചെയ്തു അഡ്മിൻ ആക്കിക്കോ.. എന്നിട്ട് ചോദിക്കുന്ന മൂവീസ് അപ്പപ്പോൾ തന്നെ നിങ്ങളുടെ വിരൽ തുമ്പിൽ 😌😌\n\n
𝐈𝐭𝐬 𝐄𝐚𝐬𝐲 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞; 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧, 𝐓𝐡𝐚𝐭𝐬 𝐀𝐥𝐥, 𝐢 𝐰𝐢𝐥𝐥 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬 𝐓𝐡𝐞𝐫𝐞...🤓\n
𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞
𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐢𝐠𝐠𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 𝐟𝐢𝐥𝐭𝐞𝐫 𝐛𝐨𝐭 <a href='http://t.me/{temp.U_NAME}?startgroup=true'>@𝐌𝐢𝐧𝐧𝐚𝐥_𝐌𝐮𝐫𝐚𝐥𝐢_𝐑𝐨𝐛𝐨𝐭</a> 𝐨𝐫 @𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓
𝐀𝐥𝐥 𝐟𝐢𝐥𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭. 😌😌
𝐅𝐚𝐬𝐭 𝐣𝐨𝐢𝐧....
"""

ADS = f"""
𝐇𝐞𝐥𝐥𝐨\n
𝙉𝙚𝙬 𝙁𝙞𝙡𝙢 𝙇𝙤𝙬 𝙎𝙞𝙯𝙚 𝙈𝙤𝙫𝙞𝙚𝙨 𝘼𝙙𝙙𝙚𝙙 𝙏𝙝𝙞𝙨 𝘾𝙝𝙖𝙣𝙣𝙚𝙡...\n
𝐅𝐚𝐬𝐭𝐞𝐬𝐭 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥...\n
𝐅𝐚𝐬𝐭 𝐉𝐨𝐢𝐧 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥...\n
"""




@Client.on_message(filters.private & filters.command(["join"]))
async def sub(client, message):
    search = message.text           
    buttons = [[
        InlineKeyboardButton('𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
    ],[
        InlineKeyboardButton('𝐌𝐨𝐯𝐢𝐞𝐬 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/PYRO_BOTZ'),
        InlineKeyboardButton('𝐒𝐨𝐧𝐠 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/PYRO_BOTZ_CHAT')
    ],[
        InlineKeyboardButton('𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩', callback_data='about'),
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






@Client.on_message(filters.private & filters.command(["ads"]))
async def sub(client, message):
    search = message.text         
    buttons = [[
        InlineKeyboardButton('𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋', url=f'https://t.me/bigmoviesworld')   
    
    ],[
        InlineKeyboardButton("𝐃𝐞𝐥𝐞𝐭𝐞", callback_data = "de"),
        InlineKeyboardButton("𝐈𝐦𝐩𝐨𝐫𝐭𝐚𝐧𝐭", callback_data = "answ")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
    photo=random.choice(SP),
    caption=ADS.format(message.text),
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
        
    elif data == "answ":
        await query.answer(f"𝐓𝐡𝐞 𝐁𝐞𝐬𝐭 𝐅𝐢𝐥𝐦 𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐁𝐨𝐭", show_alert=True)
            
    elif data == "de":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()
