from box import Box

def extract_cmdarg(text, prefix, util):
  if prefix == '':
    text = f"/{text}"
  elif prefix != '/':
    text = text.replace(prefix, '/', 1)
  return (
    util.extract_command(text.lower()),
    util.extract_arguments(text)
  )

def handleCommand(bot, message):
  
  # seperate the command and arguments
  cmd, args = extract_cmdarg(message.text, bot.prefix, bot.util)
  
  # add custom attributes
  setattr(message, "msg", Box({
    "command": cmd,
    "arguments": args,
    "cmd": cmd,
    "args": args
  }))
  setattr(
    message,
    "reply",
    lambda text, **kwargs: bot.send_reply(message.chat.id, text, message.message_id, **kwargs)
  )
  
  # check if command in bot commands
  if cmd in bot.commands:
    function = bot.commands[cmd].get('run')
    function(bot, message)
  else:
    message.reply(f"⚠ Command <b>{cmd}</b> not found.", parse_mode='HTML')