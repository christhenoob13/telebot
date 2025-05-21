import requests

def function(bot, data):
  if data.msg.args:
    return data.reply("This command dont need an arguments.")
  try:
    res = requests.get('https://sitebot-production-3143.up.railway.app/api/bible').json()
    message = f"<b>{res['verse']}</b>\n\n"
    message += f"{res['text']}"
    bot.send_message(data.chat.id, message, parse_mode='HTML')
  except Exception as e:
    bot.send_message(data.chat.id, e)

config = dict(
  name = "bible",
  run = function,
  author = "astro"
)