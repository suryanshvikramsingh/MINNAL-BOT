import os

import asyncio
import datetime
from pyrogram import Client, filters



from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from info import LOGIN_CHANNEL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

import threading
import asyncio

from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, UniqueConstraint, func


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    DB_URL = os.environ.get("DATA_URL", "")




import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)





def start() -> scoped_session:
    engine = create_engine(Config.DB_URL, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()

class custom_button(BASE):
    __tablename__ = "button"
    id = Column(Integer, primary_key=True)
    button = Column(String)

    def __init__(self, id, button):
        self.id = id
        self.button = button

custom_button.__table__.create(checkfirst=True)

class custom_caption(BASE):
    __tablename__ = "caption"
    id = Column(Integer, primary_key=True)
    caption = Column(String)
    
    def __init__(self, id, caption):
        self.id = id
        self.caption = caption

custom_caption.__table__.create(checkfirst=True)

async def update_caption(id, caption):
    with INSERTION_LOCK:
        cap = SESSION.query(custom_caption).get(id)
        if not cap:
            cap = custom_caption(id, caption)
            SESSION.add(cap)
            SESSION.flush()
        else:
            SESSION.delete(cap)
            cap = custom_caption(id, caption)
            SESSION.add(cap)
        SESSION.commit()

async def del_caption(id):
    with INSERTION_LOCK:
        msg = SESSION.query(custom_caption).get(id)
        SESSION.delete(msg)
        SESSION.commit()

async def get_caption(id):
    try:
        caption = SESSION.query(custom_caption).get(id)
        return caption
    finally:
        SESSION.close()

async def update_button(id, button):
    with INSERTION_LOCK:
        btn = SESSION.query(custom_button).get(id)
        if not btn:
            btn = custom_button(id, button)
            SESSION.add(btn)
            SESSION.flush()
        else:
            SESSION.delete(btn)
            btn = custom_button(id, button)
            SESSION.add(btn)
        SESSION.commit()

async def del_button(id):
    with INSERTION_LOCK:
        msg = SESSION.query(custom_button).get(id)
        SESSION.delete(msg)
        SESSION.commit()

async def get_button(id):
    try:
        button = SESSION.query(custom_button).get(id)
        return button
    finally:
        SESSION.close()






@Client.on_message(filters.private & ~filters.edited)
async def set(bot, message):
    if ("/set_cap" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
        await message.reply_text("🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set custom caption for any of your channels.\n\n👉 `/set_cap -1001448973320 My Caption`", quote = True)
    elif ("/set_cap" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
        caption = message.text.markdown.split(' ', 2)[2]
        channel = message.text.split(' ', 2)[1].replace("-100", "")
        try:
            a = await get_caption(channel)
            b = a.caption
        except:
            await update_caption(channel, caption)
            return await message.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)
        await message.reply_text("⚠️\n\nA caption already seted for this channel, you should first use /rmv_cap command to remove the current caption and then try seting new.", quote=True)
           
    if ("/set_btn" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
        await message.reply_text("🖊️ 𝐒𝐄𝐓 BUTTON \n\nUse this command to set button for any of your channels.\nSend a Button name and URL(separated by ' | ').\n\n👉 `/set_btn -1001448973320 Channel | https://t.me/channel`", quote = True)
    elif ("/set_btn" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
        button = message.text.split(' ', 2)[2]
        channel = message.text.split(' ', 2)[1].replace("-100", "").replace("1", "")
        try:
            a = await get_button(channel)
            b = a.button
        except:
            await update_button(channel, button)
            return await message.reply_text(f"**--Your Button--:**\n\n{button}", quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button.split(' | ')[0], url=f"{button.rsplit(' ', 1)[1]}")]]))
        await message.reply_text("⚠️\n\nA button already seted for this channel, you should first use /rmv_btn command to remove the current button and then try seting new.", quote=True)
           
    if (message.text == "/rmv_cap"):
        await message.reply_text("Use this command to remove the current caption of any of your channels.\n\n👉 `/rmv_cap -1001448973320`", quote = True)
    elif ("/rmv_cap" in message.text) and (len(message.text.split(' ')) != 1):
        channel = message.text.split(' ', 1)[1].replace("-100", "")
        try:
            a = await get_caption(channel)
            b = a.caption
        except:
            return await message.reply_text("Caption not setted yet!", quote=True)     
        await del_caption(channel)
        await message.reply_text("✅The Caption Removed Successfully.", quote=True)

    if (message.text == "/rmv_btn"):
        await message.reply_text("Use this command to remove the current button of any of your channels.\n\n👉 `/rmv_btn -1001448973320`", quote = True)
    elif ("/rmv_btn" in message.text) and (len(message.text.split(' ')) != 1):
        channel = message.text.split(' ', 1)[1].replace("-100", "").replace("1", "")
        try:
            a = await get_button(channel)
            b = a.button
        except:
            return await message.reply_text("Button not setted yet!", quote=True)     
        await del_button(channel)
        await message.reply_text("✅The Button Removed Successfully.", quote=True)



@autocaption.on_message(filters.chat(LOGIN_CHANNEL) & (filters.video | filters.document | filters.audio ) & ~filters.edited, group=-1)
async def edit(bot, message):
    m = message.video or message.document or message.audio
    try:
        channel = str(message.chat.id).replace('-100', '').replace('1', '')
        btn = await get_button(int(channel))
        button = btn.button
    except:
        button = None
        pass
    try:
        channel = str(message.chat.id).replace('-100', '')
        cap = await get_caption(int(channel))
        if message.audio:
            caption = cap.caption.replace("{duration}", str(datetime.timedelta(seconds = m.duration))).replace("{mime_type}", m.mime_type).replace("{filename}", m.file_name).replace("{artist}", m.performer).replace("{title}", m.title).replace("{ext}", "." + m.file_name.rsplit('.', 1)[1])
        elif message.video:
            caption = cap.caption.replace("{duration}", str(datetime.timedelta(seconds = m.duration))).replace("{mime_type}", m.mime_type).replace("{filename}", m.file_name).replace("{width}", str(m.width)).replace("{height}", str(m.height)).replace("{ext}", "." + m.file_name.rsplit('.', 1)[1])
        elif message.document:
            caption = cap.caption.replace("{mime_type}", m.mime_type).replace("{filename}", m.file_name).replace("{ext}", "." + m.file_name.rsplit('.', 1)[1])
    except:
        caption = None
        pass
       
    if button is not None:
        Url = button.rsplit(' ', 1)[1]
        Name = button.split(' | ')[0]
        if caption is not None:
            try:
                await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = caption, parse_mode = "markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Name, url=f"{Url}")]]))
            except FloodWait as e:
                print(f"Sleeping for {e.x}s")
                await asyncio.sleep(e.x)
            except Exception as e:
                print(e)
        elif caption is None:
            try:
                await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Name, url=f"{Url}")]]))
            except FloodWait as e:
                print(f"Sleeping for {e.x}s")
                await asyncio.sleep(e.x)
            except Exception as e:
                print(e)
    elif (button is None) and (caption is not None):
        try:
            await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = caption, parse_mode = "markdown")
        except FloodWait as e:
            print(f"Sleeping for {e.x}s")
            await asyncio.sleep(e.x)
        except Exception as e:
            print(e)
