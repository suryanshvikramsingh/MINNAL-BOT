import os
import requests
from pyrogram import Client, filters
    
from pyrogram import Client,filters
import requests,os,wget
from info import BATCH_GROUP, REQST_CHANNEL, SUPPORT_CHAT_ID, ADMINS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio



    
@Client.on_message(filters.command("im") & filters.photo) 
async def photo(client, message):
    
    results = requests.get(API + requests.utils.requote_uri(update.search)).json()["result"][:50]
    try:
        await message.reply_photo(
        photo=results,
        title=update.search.capitalize(),
        description=result
    )
        
    
