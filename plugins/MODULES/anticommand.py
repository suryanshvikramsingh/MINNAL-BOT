# (c) @KoshikKumar17
import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import User, Message      
bughunter0 = Client(
    "pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)



@Client.on_message(filters.chat(-1001600925543) & filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()
