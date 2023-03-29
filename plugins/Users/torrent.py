import os
import aiohttp
import json
from pyrogram import Client, filters, enums, emoji
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

app = Client("trntsrcbot", api_id=int(os.environ.get("API_ID")), api_hash=os.environ.get("API_HASH"), bot_token=os.environ.get("BOT_TOKEN"))


print("\nBot Started\n")



m = None
i = 0
a = None
query = None


@Client.on_message(filters.command(["torrent"]))
async def find(_, message):
    global m
    global i
    global a
    global query
    try:
        await message.delete()
    except:
        pass
    if len(message.command) < 2:
        await message.reply_text("Usage: /find query")
        return
    query = message.text.split(None, 1)[1].replace(" ", "%20")
    m = await message.reply_text("Searching")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.api-zero.workers.dev/piratebay/{query}") \
                    as resp:
                a = json.loads(await resp.text())
    except:
        await m.edit("Found Nothing.")
        return
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['Name']}\n"
        f"➲{a[i]['Uploader']} on "
        f"{a[i]['Date']}\n" 
        f"➲Size: {a[i]['Size']}\n"
        f"➲Leechers: {a[i]['Leechers']} || "
        f"➲Seeders: {a[i]['Seeders']}\n"
        f"➲Type: {a[i]['Category']}\n"
        f"➲Magnet: `<code>{a[i]['Magnet']}</code>`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Next",
                                         callback_data="nextt"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="de")
                ]
            ]
        ),
        parse_mode=enums.ParseMode.HTML
    )
    

@Client.on_callback_query(filters.regex("nextt"))
async def callback_query_next(_, message):
    global i
    global m
    global a
    global query
    i += 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['Name']}\n"
        f"➲{a[i]['Uploader']} on "
        f"{a[i]['Date']}\n" 
        f"➲Size: {a[i]['Size']}\n"
        f"➲Leechers: {a[i]['Leechers']} || "
        f"➲Seeders: {a[i]['Seeders']}\n"
        f"➲Type: {a[i]['Category']}\n"
        f"➲Magnet: `<code> {a[i]['Magnet']}</code>`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Prev",
                                         callback_data="previouss"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="de"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="nextt")
                    
                ]
            ]
        ),
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_callback_query(filters.regex("previouss"))
async def callback_query_previous(_, message):
    global i
    global m
    global a
    global query
    i -= 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['Name']}\n"
        f"➲{a[i]['Uploader']} on "
        f"{a[i]['Date']}\n" 
        f"➲Size: {a[i]['Size']}\n"
        f"➲Leechers: {a[i]['Leechers']} || "
        f"➲Seeders: {a[i]['Seeders']}\n"
        f"➲Type: {a[i]['Category']}\n"
        f"➲Magnet: `<code>{a[i]['Magnet']}</code>`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Prev",
                                         callback_data="previouss"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="de"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="nextt")
                ]
            ]
        ),
        parse_mode=enums.ParseMode.HTML
    )


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
