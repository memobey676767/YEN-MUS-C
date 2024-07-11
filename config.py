import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6532412571))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/mamakli06/mamaklimusic1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kumsaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kumsalmuzikk")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 30))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", "AgFipAAAeF5c00wqZp-rK8xg8A104yygUVgUydB52A5K0yipOfL8_jFLdbsA_hvf97jibOaNdJQ5Lp5g1mwvNDf_lpiLv8ITQskHE2JVIWOYE8fSm8n4PDQ9HzfGC28CZQTbhuVyy2625qfzAqDGW4p83pYNvq_VZo9szrPmMWIYnMyGCm5BYfW3zvgs596C7Gmeh_-VY6IBTdoqwQnPck6uZ2iPBc-hFufeY2gMUIw7CKC4sHpttHk-bjJphFyQ0CVNHBVbN7PN8Wsm8qAuQY-ZM_jKepvtQaTONeFS1pzd4AloPpClb_NGxAdoaUVLU8ZCOKoBswSW4ctezMfW9aN6mdOXUwAAAAG8nzf6AA")
STRING3 = getenv("STRING_SESSION3", "BAHHpwsAaJEVH7AhUy5uEYebqhAjdsLzpAB-t5w3aLBTI4B9zOjs2hvMTY42inb3ClJZaCzljYXOXLPKBpKR8Mk1RGa7qwgapNSS5X2bdWhcG9SQ70LRVtTtpgn3lJpGRPN3agfs7qpLX7i2lb9_vHDs9F0uMmSkxen0dr0OkRYpz104vCLzCgo38c72EwvAcyLgVZBYNIh96pm3jIfbzR8hJs12SO05pFXYoyW9kaAakt9F3XQSfsbcwazri-kuj2VKxxVxnHydxMdHe_KwiBwD-VaoYASe_U0-S3M1nlXj8X07fWFViboUs61m8-BFXS7X3k73f8bMg_NIEheNGpXfwub9KgAAAAG3uweMAA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
   "START_IMG_URL", "https://telegra.ph/Jww-06-18"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Jww-06-18"
)
PLAYLIST_IMG_URL = "https://telegra.ph/Jww-06-18"
STATS_IMG_URL = "https://telegra.ph/Jww-06-18"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Jww-06-18"
TELEGRAM_VIDEO_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
STREAM_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/6c6cce625f4a721569703.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
