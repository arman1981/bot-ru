from telethon import TelegramClient, events
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern="/start"))
async def handler(event):
    await event.respond("👋 Привет! Это AI-Сетевик. Нажми на кнопку ниже:", buttons=[
        [event.button.url("🔗 Перейти в Mini App", "https://teambot.pro")]
    ])

bot.run_until_disconnected()
