import os
import requests
from pyrogram import Client, filters
    
from pyrogram import Client, filters
import requests,os,wget
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import requests
from bs4 import BeautifulSoup


from pyrogram.types import Message


@Client.on_message(filters.command("i") & filters.text)    
async def photo(client, message):
    args = message.text.split(None)

    results = requests.get(f"https://apibu.herokuapp.com/api/y-images+ requests.utils.requote_uri.json()["result"][:1] 
    img = r['data']['results'][0]['image'][2]['link']   
    await message.reply_photo(
    photo=img,
    results=message.query.capitalize()
    )
        
    
