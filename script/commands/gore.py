from requests import get

def function(bot, data):
  ld = bot.send_message(data.chat.id, "Generating gore video...")
  api = get("https://api.zetsu.xyz/randgore?apikey=efb2a4171066dc2041298ca4251f90ef")
  if api.status_code != 200:
    bot.delete_message(data.chat.id, ld.message_id)
    return data.reply("⚠ Error while downloading the video")
  gore = api.json()
  title = gore["result"]['title']
  video = gore['result']['video2']
  thumbnail = gore['result']['thumb']

  bot.send_video(
    data.chat.id,
    video,
    thumbnail=thumbnail,
    caption=f"<b>{title}</b>",
    parse_mode='HTML'
  )
  bot.delete_message(data.chat.id, ld.message_id)

config = dict(
  name = 'gore',
  run = function,
  author = 'Astro',
  description = "Generate random gore videos"
)