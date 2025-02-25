import requests

def shoti(bot, data):
  if data.msg.args:
    return data.reply("This command dont need an arguments")
  loading = bot.send_message(data.chat.id, "Generating shoti video...")
  try:
    res = requests.get('https://sitebot-production-3143.up.railway.app/api/shoti')
    if res.status_code == 200:
      response = requests.get(res.json()['videoSource'])
      if response.status_code == 200:
        with open('script/commands/cache/shoti.mp4', 'wb') as f:
          f.write(response.content)
          message = f"<b><a href='https://tiktok.com/{res.json()['username']}'>{res.json()['username']}</a></b>\n\n"
          message += res.json()['description']
          bot.send_video(
            data.chat.id,
            bot.types.InputFile("script/commands/cache/shoti.mp4"),
            parse_mode='HTML',
            show_caption_above_media=True,
            caption=message
          )
      else:
        print(response['videoSource'])
        data.reply("⚠ Error while downloading the video")
    else:
      data.reply("⚠ Error while requesting to API")
    bot.delete_message(data.chat.id, loading.message_id)
  except Exception as e:
    bot.delete_message(data.chat.id, loading.message_id)
    return data.reply(e)

config = dict(
  name='shoti',
  run=shoti,
  author="Christopher Jr.",
  description="Generate a random girl videos"
)