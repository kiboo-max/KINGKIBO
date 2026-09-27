from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
user = Client("KINGKIBO", api_id=API_ID, api_hash=API_HASH, plugins=dict(root="plugins"))
bot = Client("helper", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="plugins/bot"))
user.start()
bot.start()
print("BOT KINGKIBO ON")
idle()
