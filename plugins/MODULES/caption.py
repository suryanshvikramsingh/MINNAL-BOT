from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    Poll,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)





non_anonymous_poll = filters.create(
    lambda *_: _[2].poll is not None and not _[2].poll.is_anonymous
)

forwardchannel = -1000000000000
startmsg: str = """
start message
"""


@Client.on_message(filters.command("cstart") & filters.private)
async def start(client, message):
    await message.reply(
        startmsg,
    )


@Client.on_message( ~filters.service & ~filters.text & ~filters.group)
    
async def viewcounter(client, message):
    forward = await message.forward(forwardchannel)
    await forward.forward(message.chat.id)
    await forward.delete()




