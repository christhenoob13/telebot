from .bot_handler.command_handler import handleCommand

def handler(bot):
  @bot.message_handler(content_types=['text'])
  def content_type_text(msg):
    if msg.text.startswith(bot.prefix):
      handleCommand(bot, msg)