import importlib
import os

def load_commands(bot_instance):
  loaded = 0
  unloaded = 0
  files=list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./script/commands')))
  for file in files:
    filepath = f'script.commands.{os.path.splitext(file)[0]}'
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name').lower()
      function = config.get('run')
      if not name or not function:
        unloaded+=1
      elif not name.isalnum():
        unloaded+=1
      elif name in bot_instance.commands:
        unloaded+=1
      else:
        loaded+=1
        config['usage'] = config.get('usage', '').replace('{p}', bot_instance.prefix)
        config['description'] = config.get('description', 'No description.').replace('{p}', bot_instance.prefix)
        bot_instance.commands[name] = config
    else:
      unloaded+=1
  
  message = f"NAME: [blue]{bot_instance.username}[/blue]\n"
  message += f"COMMAND LOADED: [green]{loaded}[/green]\n"
  message += f"COMMAND UNLOAD: [red]{unloaded}[/red]"
  panel = bot_instance.rich.Panel(message, title="BOT CREATED")
  bot_instance.rich.console.print(panel)