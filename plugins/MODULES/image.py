import os
import requests
from pyrogram import Client, filters
    
from pyrogram import Client,filters
import requests,os,wget
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from pyrogram import Client, filters
from pyrogram.types import Message


    
@Client.on_message(filters.command.("i") & filters.photo) 
async def photo(client, message):
    
    results = requests.get(API + requests.utils.requote_uri(update.search)).json()["result"][:50]
    
    await message.reply_photo(
    photo=results,
    title=update.search.capitalize(),
    description=result
    )
        
    
