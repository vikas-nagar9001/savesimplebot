from dotenv import load_dotenv  #FOR LOCAL ENV ON HOSTING WE DONT NEED DOTENV

import os     #OS IMPORT IN BOTH HOST and local env             

load_dotenv()    #FOR LOCAL ENV ON HOSTING WE DONT NEED DOTENV
# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "0"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your API Hash from my.telegram.org
SESSION_STRING = os.environ.get("SESSION_STRING", "")





# Don't Remove Credit Tg - @Mod_Mick
# Ask Doubt on telegram @Mod_Mick