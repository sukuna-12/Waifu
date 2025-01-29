class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6087651372"
    sudo_users = "6087651372", "7667987606", "7378476666", "6858718276"
    GROUP_ID = -1002316438413
    TOKEN = "7589023976:AAFerTqtgkPEhmNsAU_5XOFtBaTcd7g-3EE"
    mongo_url = "mongodb+srv://surajgod112:surajgod113@cluster0.v52wo.mongodb.net/"
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
