import asyncio
from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = -1004364712516

bot = Bot(token=TOKEN)

async def main():
    while True:
        try:
            await bot.send_message(CHAT_ID, "مع")
            print("Sent")
        except Exception as e:
            print(e)

        await asyncio.sleep(277)

asyncio.run(main())
