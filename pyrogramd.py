from pyrogram import Client, filters

bot_token = "6512626744:AAEhqUWmB-EgAUIekifqzbh1dmy_r8LmUaY"

api_id = 24711840
api_hash = "688506e29b7a58b24eae6823f73d372a"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

