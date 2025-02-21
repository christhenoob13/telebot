#from bembang import log
import importlib
import os

def load_bot_commands(bot_instance):
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
      # check if valid command name or function
      if not name or not function:
        unloaded+=1
        #log('error', 'Invalid config items')
      elif not name.isalnum():
        unloaded+=1
        #log('error', 'Invalid command name')
      elif name in bot_instance.commands:
        unloaded+=1
        #log('error', f"Command '{name}' already exist")
      else:
        loaded+=1
        config['usage'] = config.get('usage', '').replace('{p}', bot_instance.prefix)
        config['description'] = config.get('description', 'No description.').replace('{p}', bot_instance.prefix)
        bot_instance.commands[name] = config
    else:
      unloaded+=1
      #log('error', f'Missing config in {file}')
  log('success', f'COMMAND: \033[1;92m{loaded}\033[0m', label='LOAD')
  log('error', f'COMMAND: \033[1;91m{unloaded}\033[0m', label='UNLOAD')