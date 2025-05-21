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
      if permission not in ['member','admin','botadmin',0,1,2]:
        config['permission'] = 'member'
      if not name or not function:
        print("\033[31mCOMMAND NOT LOADED \033[0m- Invalid 'name' & 'run' key on config")
      elif not name.isalnum():
        print(f"\033[31mCOMMAND NOT LOADED \033[0m- Invalid command name. name: {name}")
      elif name in tambak:
        print(f"\033[31mCOMMAND NOT LOADED \033[0m- command '{name}' already exists")
      else:
        config['usage'] = config.get('usage', 'No usage.')
        config['description'] = config.get('description', 'No description.')
        tambak[name] = config
        print(f"\033[32mCOMMAND LOADED \033[0m- {name} \033[33m({file}.py)\033[0m")
    else:
      print(f"\033[31mCOMMAND NOT LOADED \033[0m- Unable to load command at {file}.py")
  return tambak

def load_events():
  tambak = dict()
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
        print("\033[31mEVENT NOT LOADED \033[0m- Invalid 'name' & 'run' key on config")
      elif not name.isalnum():
        print("\033[31mEVENT NOT LOADED \033[0m- Invalid event name")
      elif name in tambak:
        print(f"\033[31mEVENT NOT LOADED \033[0m- Event name ({name}) already exists")
      else:
        tambak[name] = config
        print(f"\033[32mEVENT LOADED \033[0m- {name} \033[33m({file}.py)\033[0m")
    else:
      print(f"\033[31mEVENT NOT LOADED \033[0m- Unable to load event at {file}.py")
  return tambak