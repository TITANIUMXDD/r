import os
from os import getenv
from dotenv import load_dotenv

load_dotenv() # environment

###API_ID = int(getenv("API_ID", 3974784))
API_HASH = getenv("API_HASH", "c58c42689bdd066c7e64af20484a34f7")
BOT_TOKEN = getenv("BOT_TOKEN", "5373933240:AAFyzbScHY0rr4oJwOlcYnThhQ6tcBqW8kc")
SESSION_NAME = getenv("SESSION_NAME", "BQA4aVPn6amzgXnquTFc7JcSztr9nPRm9dBdsbMR3nfgt1QIMTHcJNji-DNocVHEcV9mKUaKBPwgTqeXjr9mTEStIc_YuwYlitxnALMbVwQD1VTfrXQJAp0Z9HjeNYnGZUyn8167luf_vk-_ULuuYBmvEzeI3MW0r-HaNh-LxGAh4eTv8rih2JWQoenvpqAvXEueGV1oxeeKsPmbRy4ewhrfSUg-kbJnzhPUTZXIwLKLlSwzcDHN_lUuKGHqBZj_8yw-rY9dQ9e4nhyqxnk-IoLgU5uSIRJeEmeRvFaO_we4PdWfkOI-QN61-2uVOfikTHewIEngW0RpOF9qIBtVzEoXAAAAASogKNEA")

ASS_ID = int(getenv("5001717969"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://akshaygamer:akshaygamer@cluster0.xf8b5.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 798393054))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 54000))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5001717969").split())) ###
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $ *").split())
#SUDO_USERS = list(map(int, getenv("SUDO_USERS", 5001717969).split()))
# fill with pyrogram session string
#SESSION_NAME= BQA4aVPn6amzgXnquTFc7JcSztr9nPRm9dBdsbMR3nfgt1QIMTHcJNji-DNocVHEcV9mKUaKBPwgTqeXjr9mTEStIc_YuwYlitxnALMbVwQD1VTfrXQJAp0Z9HjeNYnGZUyn8167luf_vk-_ULuuYBmvEzeI3MW0r-HaNh-LxGAh4eTv8rih2JWQoenvpqAvXEueGV1oxeeKsPmbRy4ewhrfSUg-kbJnzhPUTZXIwLKLlSwzcDHN_lUuKGHqBZj_8yw-rY9dQ9e4nhyqxnk-IoLgU5uSIRJeEmeRvFaO_we4PdWfkOI-QN61-2uVOfikTHewIEngW0RpOF9qIBtVzEoXAAAAASogKNEA

# fill with the token of bot you created from @BotFather
BOT_TOKEN= 5373933240:AAFyzbScHY0rr4oJwOlcYnThhQ6tcBqW8kc

# fill with your api_id
API_ID= 3974784

# fill with your api_hash
API_HASH= c58c42689bdd066c7e64af20484a34f7

# fill with IDs of user want to add into sudo user list
SUDO_USERS= 5001717969

# fill with your ID only !!
OWNER_ID= 5001717969

# set the limit of duration video can be played
DURATION_LIMIT=540000

# fill with database url you created from cloud.mongodb.com
MONGO_DB_URI= mongodb+srv://akshaygamer:akshaygamer@cluster0.xf8b5.mongodb.net/?retryWrites=true&w=majority

# create a group chat and add your bot with the assistant into the group
LOG_GROUP_ID=798393054

# fill with the Telegram ID of the assistant account
ASS_ID= 5001717969
