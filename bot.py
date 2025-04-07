import os
import threading
from plugins.config import Config
from pyrogram import Client
from fastapi import FastAPI
import uvicorn

# راه‌اندازی سرور برای Health Check
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

def run_server():
    # اجرای سرور FastAPI در پورت 8000 برای Health Check
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

if __name__ == "__main__":
    # اجرای سرور در یک ترد جداگانه
    threading.Thread(target=run_server, daemon=True).start()
    
    # بررسی و ساخت پوشه دانلود در صورت نیاز
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    
    plugins = dict(root="plugins")
    
    # تعریف کلاینت Pyrogram
    client = Client("@UploaderXNTBot",
                    bot_token=Config.BOT_TOKEN,
                    api_id=Config.API_ID,
                    api_hash=Config.API_HASH,
                    sleep_threshold=300,
                    plugins=plugins)
    
    # نمایش پیغام
    print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")
    
    # اجرای Pyrogram Client
    client.run()
