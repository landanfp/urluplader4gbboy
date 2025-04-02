import os
from flask import Flask, request
from plugins.config import Config
from pyrogram import Client

app = Flask(__name__)

if not os.path.isdir(Config.DOWNLOAD_LOCATION):
    os.makedirs(Config.DOWNLOAD_LOCATION)

plugins = dict(root="plugins")
Client = Client("@UploaderXNTBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=300,
    plugins=plugins
)

@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json()
    if update:
        bot.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    Client.start()
    print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")
    app.run(host="0.0.0.0", port=443)
