
from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "27876808"))
    API_HASH = environ.get("API_HASH", "414f022bf4a6620cb4bba3505605e374")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://jauharobaid:1VAOB4Fm5gvM2YKS@cluster0.1nc4nru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "7098324238"))


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

