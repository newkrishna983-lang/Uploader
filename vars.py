# Don't Remove Credit Tg - @newstudent1885
# Ask Doubt on telegram @newstudent1885

from os import environ

API_ID = int(environ.get("API_ID", "")) #Replace with your api id
API_HASH = environ.get("API_HASH", "") #Replace with your api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "") #Replace with your bot token
API_ID = int(os.environ.get("API_ID", "34422904"))
API_HASH = os.environ.get("API_HASH", "7e0002469784f47fc08a6b3d93d7ebed")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8582068316:AAGvzsntvO2VyCUGJcZYsQuMlyrTBZf4zDE")

CREDIT = os.environ.get("CREDIT", "Krishna ❤️‍🔥")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "CpprivateApi")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://adarshppandey937:uIoPcln9vXQBF0vP@cluster0.o9mn6hb.mongodb.net/?")  # Add your own atlas db
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "5349573682"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]  # Default to owner ID
