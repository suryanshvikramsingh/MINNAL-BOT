import os
import requests
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto
)



    results = requests.get
        (API + requests.utils.requote_uri(update.query)
    ).json()["result"][:50]

@Client.on_message(filters.private & filters.photo & filters.command("im"]))
async def search(bot, update):
    
    results = requests.get(
        API + requests.utils.requote_uri(update.search)
    ).json()["result"][:50]



    for result in results:
        await message.reply_photo(
        title=update.search.capitalize(),
        description=result,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
