from googletrans import Translator
from pyrogram import Client, filters
# from plugins.helpers.list import list
# from plugins.helper.database import find_one

import pymongo 
import os

DATABASE_NAME = os.environ.get("DATABASE_NAME","")
DATABASE_URI = os.environ.get("DATABASE_URI","")
mongo = pymongo.MongoClient(DATABASE_URI)
db = mongo[DATABASE_NAME]
dbcol = db["USER"]



list = {
"afrikaans":"af",
"albanian":"sq",
"amharic":"am",
"arabic":"ar",
"armenian":"hy",
"azerbaijani":"az",
"basque":"eu",
"belarusian":"be",
"bengali":"bn",
"bosnian":"bs",
"bulgarian":"bg",
"catalan":"ca",
"cebuano":"ceb",
"chinese": "zh",
"corsican":"co",
"croatian":"hr",
"czech":"cs",
"danish":"da",
"dutch":"nl",
"english":"en",
"esperanto":"eo",
"estonian":"et",
"finnish":"fi",
"french":"fr",
"frisian":"fy",
"galician":"gl",
"georgian":"ka",
"german":"de",
"greek":"el",
"gujarati":"gu",
"haitian creole":"ht",
"hausa":"ha",
"hawaiian":"haw",
"hebrew":"he",
"hindi":"hi",
"hmong":"hmn",
"hungarian":"hu",
"icelandic":"is",
"igbo":"ig",
"indonesian":"id",
"irish":"ga",
"italian":"it",
"japanese":"ja",
"javanese":"jv",
"kannada":"kn",
"kazakh":"kk",
"khmer":"km",
"kinyarwanda":"rw",
"korean":"ko",
"kurdish":"ku",
"kyrgyz":"ky",
"lao":"lo",
"latin":"la",
"latvian":"lv",
"lithuanian":"lt",
"luxembourgish":"lb",
"macedonian":"mk",
"malagasy":"mg",
"malay":"ms",
"malayalam":"ml",
"maltese":"mt",
"maori":"mi",
"marathi":"mr",
"mongolian":"mn",
"myanmar":"my",
"nepali":"ne",
"norwegian":"no",
"nyanja":"ny",
"odia":"or",
"pashto":"ps",
"persian":"fa",
"polish":"pl",
"portuguese":"pt",
"punjabi":"pa",
"romanian":"ro",
"russian":"ru",
"samoan":"sm",
"scots gaelic":"gd",
"serbian":"sr",
"sesotho":"st",
"shona":"sn",
"sindhi":"sd",
"sinhala":"si",
"slovak":"sk",
"slovenian":"sl",
"somali":"so",
"spanish":"es",
"sundanese":"su",
"swahili":"sw",
"swedish":"sv",
"tagalog":"tl",
"tajik":"tg",
"tamil":"ta",
"tatar":"tt",
"telugu":"te",
"thai":"th",
"turkish":"tr",
"turkmen":"tk",
"ukrainian":"uk",
"urdu":"ur",
"uyghur":"ug",
"uzbek":"uz",
"vietnamese":"vi",
"welsh":"cy",
"xhosa":"xh",
"yiddish":"yi",
"yoruba":"yo",
"zulu":"zu"}



def find(chat_id):
	id =  {"_id":chat_id}
	x = dbcol.find(id)
	for i in x:
             lgcd = i["lg_code"]
             return lgcd 



@Client.on_message(filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```")
			except:
			   	await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```")
      			
				
			
		except :
			print("error")
	else:
			 ms = await message.reply_text("You can Use This Command by using reply to message")
			 await ms.delete()
