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

def is_valid_permission(bot, message, cmd):
  perm = bot.commands[cmd].get('permission')
  if perm in [2,'botadmin']:
    print("test")
    if message.from_user.id not in bot.admins:
      return False
  elif perm in [1, 'admin']:
    if message.chat.type != 'private':
      chat_admins = [user.user.id for user in bot.get_chat_administrators(message.chat.id)]
    else:
      chat_admins = [message.from_user.id]
    if message.from_user.id not in chat_admins:
      return False
  return True

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
  
  if not is_valid_permission(bot, message, cmd):
    return message.reply(f"⚠ You dont have permission to use this command.")
  
  if cmd not in bot.commands:
    # check if command not in bot commands
    message.reply(f"⚠ Command <b>{cmd}</b> not found.", parse_mode='HTML')
  else:
    function = bot.commands[cmd].get('run')
    function(bot, message)