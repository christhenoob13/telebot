import importlib
import os

def load_commands():
  #loaded = 0
  #unloaded = 0
  tambak = dict()
  files=list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./script/commands')))
  for file in files:
    filepath = f'script.commands.{os.path.splitext(file)[0]}'
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name').lower()
      function = config.get('run')
      permission = config.get('permission', 'member')
      config['permission'] = permission
      if not name or not function:
        print("\033[31mCOMMAND NOT LOADED \033[0m- there is no 'name' & 'run' key on config")
      elif not name.isalnum():
        print(f"\033[31mCOMMAND NOT LOADED \033[0m- Invalid command name. name: {name}")
      elif name in tambak:
        print(f"\033[31mCOMMAND NOT LOADED \033[0m- Invalid command name. name: {name}")
      elif permission not in ['member','admin','owner',0,1,2]:
        unloaded+=1
        config['permission'] = 'member'
      else:
        loaded+=1
        config['usage'] = config.get('usage', '').replace('{p}', bot_instance.prefix)
        config['description'] = config.get('description', 'No description.').replace('{p}', bot_instance.prefix)
        bot_instance.commands[name] = config
    else:
      unloaded+=1
  
  message = f"NAME: [blue]{bot_instance.username}[/blue]\n"
  message += f"COMMAND LOADED: [green]{loaded}[/green]\n"
  message += f"COMMAND UNLOAD: [red]{unloaded}[/red]\n"
  return message

def load_events(bot):
  load = 0
  unload = 0
  files=list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./script/events')))
  for file in files:
    filepath = f'script.events.{os.path.splitext(file)[0]}'
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name')
      type = config.get('type')
      run = config.get('run')
      author = config.get('author', 'Unknown')
      description = config.get('description', 'No description!')
      if not name or not type or not run:
        unload += 1
      elif not name.isalnum():
        unload += 1
      elif name in bot.events:
        unload += 1
      else:
        load += 1
        bot.events[name] = config
    else:
      unload += 1
  message = f"EVENT LOADED: [green]{load}[/green]\n"
  message += f"EVENT LOADED: [red]{unload}[/red]"
  return message