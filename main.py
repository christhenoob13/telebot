from rich.panel import Panel
from rich.console import Console
from teleapp import web_server
from box import Box
from bot import (
  handler,
  load_commands,
  Margelet
)
import telebot.util as util
import threading
import requests

active_bots = {}

class BotDaddy(Margelet):
  def __init__(self, token):
    self.token = token
    self.baseUrl = 'https://api.telegram.org'
    self.util = util
    self.rich = Box({
      "Panel": Panel,
      "console": Console()
    })
    
    self.prefix = '/'
    self.commands = {}
    if not self._isValidToken():
      raise ValueError("Invalid bot token")
    
    super().__init__(token)
    
  def _isValidToken(self) -> bool:
    res = requests.get(f"{self.baseUrl}/bot{self.token}/getMe")
    if res.status_code == 200:
      data = res.json()['result']
      self.username = data['username']
      self.id = data['id']
      self.first_name = data['first_name']
      if self.id in active_bots:
        raise Exception('Bot already exist')
      active_bots[self.id] = {
        "id": self.id,
        "name": self.username
      }
      return True
    return False
  
  def _start_bot(self):
    self.polling()
  
  def start(self):
    handler(self)
    load_commands(self)
    BOT = threading.Thread(target=self._start_bot)
    BOT.start()
  
  def stop(self):
    del active_bots[self.id]
    self.stop_bot()

if __name__ == '__main__':
  toper = BotDaddy("7218544319:AAFI-ZCSjLPRh1tmNCIIpqAszp_ykG0yVGw")
  toper.start()
  
  app = web_server(BotDaddy)
  app.run()