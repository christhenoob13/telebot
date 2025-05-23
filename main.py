from rich.panel import Panel
from rich.console import Console
from teleapp import web_server
from box import Box
from bot import (
  handler,
  load_commands,
  load_events,
  Margelet,
  BotChats
)
import telebot.util as util
import telebot.types as types
import threading
import requests

active_bots = {}
COMMANDS = load_commands()
EVENTS = load_events()

class BotDaddy(Margelet):
  def __init__(self,
    token: str,
    commands: list,
    events: list,
    admins: list,
    prefix: str|None = None
    ):
    self.token = token
    self.baseUrl = 'https://api.telegram.org'
    self.chats = BotChats()
    self.util = util
    self.types = types
    self.rich = Box({
      "Panel": Panel,
      "console": Console()
    })
    
    self.prefix = prefix if prefix else ''
    self.admins = admins
    self.commands = {cmd: COMMANDS[cmd] for cmd in commands} if commands[0]!="*" and len(commands)==1 else COMMANDS
    self.events = {ev: EVENTS[ev] for ev in events} if events[0]!="*" else EVENTS
    
    # callback
    self.ikMarkup = self.types.InlineKeyboardMarkup
    self.ikButton = self.types.InlineKeyboardButton
    
    if not self._isValidToken():
      raise ValueError("Invalid bot token")
    
    super().__init__(token)
  
  # check if the telegram token is valid, if not it will throw an error
  def _isValidToken(self) -> bool:
    res = requests.get(f"{self.baseUrl}/bot{self.token}/getMe")
    if res.status_code == 200:
      data = res.json()['result']
      if self.id in active_bots:
        raise Exception('Bot already exist')
      self.username = data['username']
      self.id = data['id']
      self.first_name = data['first_name']
      return True
    return False
  
  # start polling the bot to listen
  def _start_polling(self):
    self.polling()
  
  # start the bot
  def start(self):
    try:
      handler(self)
      active_bots[str(self.id)] = self
      threading.Thread(target=self._start_polling).start()
    except Exception as e:
      raise Exception(e)
  # stop the bot
  def stop(self):
    del active_bots[self.id]
    self.stop_bot()
  
  def dd(self):
    return self.__dict__

if __name__ == '__main__':
#  BotDaddy(
#    "7041468622:AAEvpBtCKt_wLOSIFWboeoo4tyBTErLKlIw",
#    ["*"],["*"],
#    [7075537944],
#    prefix='/'
#  ).start()
  command_form, event_form = COMMANDS, EVENTS
  for cmd in command_form:
    del command_form[cmd]['run']
  for ev in event_form:
    del event_form[ev]['run']
    del event_form[ev]['type']
  app = web_server(
    BotDaddy,
    active_bots,
    dict(
      commands=command_form,
      events=event_form
    )
  )
  app.run(debug=True)