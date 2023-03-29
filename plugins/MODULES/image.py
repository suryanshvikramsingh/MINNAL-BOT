import os
import requests
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto
)



    
@Client.on_message(filters.private & filters.photo & filters.command("im"))
async def search(bot, update):
    
    results = requests.get(
        API + requests.utils.requote_uri(update.search)
    ).json()["result"][:50]



    try:
        await message.reply_photo(
        photo=results,
        title=update.search.capitalize(),
        description=result,
        reply_markup=InlineKeyboardMarkup(buttons))
    
