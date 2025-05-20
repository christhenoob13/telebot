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

class BotDaddy(Margelet):
  def __init__(self, token):
    self.token = token
    self.baseUrl = 'https://api.telegram.org'
    self.chats = BotChats()
    self.util = util
    self.types = types
    self.rich = Box({
      "Panel": Panel,
      "console": Console()
    })
    
    self.prefix = '/'
    self.admins = dict()
    self.commands = dict()
    self.events = dict()
    
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
      self.username = data['username']
      self.id = data['id']
      self.first_name = data['first_name']
      if self.id in active_bots:
        raise Exception('Bot already exist')
      return True
    return False
  
  # start polling the bot to listen
  def _start_polling(self):
    self.polling()
  
  # start the bot
  def start(self):
    cmd = load_commands(self)
    evnt = load_events(self)
    panel = self.rich.Panel(cmd + evnt, title="BOT CREATED")
    self.rich.console.print(panel)
    handler(self)
    active_bots[str(self.id)] = self
    threading.Thread(target=self._start_polling).start()
  
  # stop the bot
  def stop(self):
    del active_bots[self.id]
    self.stop_bot()
  
  def dd(self):
    return self.__dict__

if __name__ == '__main__':
  BotDaddy("7041468622:AAEvpBtCKt_wLOSIFWboeoo4tyBTErLKlIw").start()
  app = web_server(BotDaddy, active_bots)
  app.run()