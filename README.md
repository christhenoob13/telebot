# Telebot
basta bot to sa telegram

## echo command
```python
def echo(bot, data):
  if not data.msg.args:
    return data.reply("Please provide a message to echo.")
  bot.send_message(
    data.chat.id,
    f"ECHO: {data.msg.args}"
  )

config = dict(
  name = "echo",              # (required) command name
  run = echo,                 # (required) your command function
  author = "Greegmon",        # enter your name
  adminOnly = False,          # only admin can use the cmd (if True)
  usage = "{p}echo [text]",   # how to use your command
  description = "Your text.." # short desc of your command
)
```

### Docs
link: https://pytba.readthedocs.io/en/latest/sync_version/index.html