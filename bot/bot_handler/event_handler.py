def handleEvent(bot, event):
  for ev in bot.events:
    if bot.events[ev]['type'] == event.content_type:
      bot.events[ev]['run'](bot, event)