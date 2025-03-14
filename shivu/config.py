class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6675050163"
    sudo_users = "6675050163", "6087651372","7640076990"
    GROUP_ID = -1002499806698
    TOKEN = "7785998273:AAHER3KsHxhsZG2JFlA9uUOfeY0qwFW8i1c"
    mongo_url = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/"
    PHOTO_URL = ["https://graph.org/file/09e83a1d89aceabd480c5-2afc46a31083fe23f2.jpg", "https://graph.org/file/0aa659508c1add9ae4c86-2b335aa5262b7b64d2.jpg"]
    SUPPORT_CHAT = "notyourtypeGod"
    UPDATE_CHAT = "waifubotdjk"
    BOT_USERNAME = "Waifugrab17bot"
    CHARA_CHANNEL_ID = "-1002374252364"
    api_id = 29830137
    api_hash = "4fdb6b13530915e7b513ee4318f109b9"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
