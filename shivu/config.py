class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6087651372"
    sudo_users = "6845325416", "7667987606"
    GROUP_ID = -1002133191051
    TOKEN = "7589023976:AAFerTqtgkPEhmNsAU_5XOFtBaTcd7g-3EE"
    mongo_url = "mongodb+srv://surajmanikpuri601:surajgod112@cluster0.bmdh2.mongodb.net/
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "ntpcraj"
    UPDATE_CHAT = "ntpcdjk"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 29830137
    api_hash = "4fdb6b13530915e7b513ee4318f109b9"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
