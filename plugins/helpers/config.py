import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "15823382")

API_HASH = os.environ.get("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945280153:AAEZFpMp-Plgwgoce0uVkT7RKk6rLTngCSA") 

# FORCE_SUB = os.environ.get("FORCE_SUB", "Film_Update_Official") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ae8701b26c6cf0db98c0b.jpg")

ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in os.environ.get('ADMINS', '').split()]

PORT = os.environ.get('PORT', '8000')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))


