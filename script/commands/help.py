def byPage(commands,j, page=1):
  message = f"╭─── *COMMANDS* ──⟢\n"
  for cmd in commands[page-1]:
    message += f"│ {'○' if not j[cmd] else '⌬'} {cmd}\n"
  message += f"╰───{'─'*len('COMMANDS')}─⟢\n"
  message += f"📖 Page: ({page}/{len(commands)})\n"
  return message

def getAll(commands,j):
  message = f"╭─── *COMMANDS* ──⟢\n"
  dal = list()
  for cmd in commands:
    if j[cmd]:
      dal.insert(0, cmd)
    else:
      dal.append(cmd)
  for cmd in dal:
    message += f"│ {'○' if not j[cmd] else '⌬'} {cmd}\n"
  message += f"╰───{'─'*len('COMMANDS')}─⟢\n"
  return message


def function(bot, event):
  xzxc = {key:udo.get('adminOnly', False) for key, udo in bot.commands.items()}
  commands = list(bot.commands)
  chunk = 15
  COMMANDS = [commands[i:i+chunk] for i in range(0, len(commands), chunk)]
  sub, *_ = event.msg.args.split(' ',1) if event.msg.args else [event.msg.args,'']
  args = ' '.join(_)

  if args:
    return event.reply(f"ⓘ Invalid command usage, type '{bot.prefix}help help' to see how to use this command.")

  if sub.lower() == 'all':
    message = getAll(commands, xzxc)
    if hasattr(bot, 'events'):
      message += f"╭──── *EVENTS* ────⟢\n"
      for ib in bot.events:
        message += f"│ ○ {ib['fileName']}\n"
      message += f"╰────{'─'*len('EVENTS')}──⟢\n\n"
    message += f"📦 Total commands: {len(commands)}\n"
    message += f"ⓘ 𝖨𝖿 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝖺𝗇𝗒 𝗊𝗎𝖾𝗌𝗍𝗂𝗈𝗇𝗌 𝗈𝗋 𝗇𝖾𝖾𝖽 𝖺𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝖼𝖾, 𝗉𝗅𝖾𝖺𝗌𝖾 𝖼𝗈𝗇𝗍𝖺𝖼𝗍 𝗍𝗁𝖾 𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋."
    return event.reply(message, parse_mode='MARKDOWN')


  # command info
  if sub.lower() in commands:
    cmd = bot.commands.get(sub.lower())
    message = f"╭─── *{sub.lower()}* ───\n"
    message += f"*author:* {cmd.get('author', "Unknown")}\n"
    message += f"*adminOnly:* {cmd.get('adminOnly', False)}\n"
    message += f"*usage:* {cmd.get('usage')}\n"
    message += f"*description:* {cmd.get('description')}\n"
    message += f"╰────{'─'*len(sub.lower())}───\n"
    return event.reply(message, parse_mode="MARKDOWN")
  elif sub:
    try:
      __nothing__ = int(sub)
    except ValueError:
      return event.reply(f"ⓘ Command '{sub.lower()}' not found, type '{bot.prefix}help all' to see all the commands.")

  # by page
  if sub:
    if len(COMMANDS) < int(sub) or len(COMMANDS) > int(sub):
        return event.reply(f"Page {sub} not found, total command page {len(COMMANDS)}")
  message = byPage(COMMANDS, xzxc, page=int(sub) if sub else 1)
  message += f"📦 Total commands: {len(commands)}\n"
  message += f"ⓘ 𝖨𝖿 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝖺𝗇𝗒 𝗊𝗎𝖾𝗌𝗍𝗂𝗈𝗇𝗌 𝗈𝗋 𝗇𝖾𝖾𝖽 𝖺𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝖼𝖾, 𝗉𝗅𝖾𝖺𝗌𝖾 𝖼𝗈𝗇𝗍𝖺𝖼𝗍 𝗍𝗁𝖾 𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋."
  return event.reply(message, parse_mode='MARKDOWN')

config = dict(
  name = 'help',
  run = function,
  author = "Christopher Jr.",
  usage = "{p}help [<None>|<page>|<cmd>|all]",
  description = "Show bot's available commands"
)