#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27258217"))
API_HASH = environ.get("API_HASH", "5f8af721437e2c252757f0eca111e693")
BOT_TOKEN = environ.get("BOT_TOKEN", "AAE5mtYfuiukkcPtIxmYQ4fQ3e9K5Rhjry4")

OWNER = int(environ.get("OWNER", "5488182213"))
CREDIT = environ.get("CREDIT", "Roushan")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5488182213').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5488182213').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

