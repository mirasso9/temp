from telethon import TelegramClient, events

# تنظیمات بات
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# ایجاد کلاینت
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# تعریف رویداد برای دستور /ping
@client.on(events.NewMessage(pattern='/ping'))
async def handler(event):
    await event.respond('pong')

# اجرای کلاینت
client.run_until_disconnected()
