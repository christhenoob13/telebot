from telebot import TeleBot
from teleapp import web_server
from bot.telegram_event import handler as tg_handle
import threading
import requests

active_bots = {}

class BotDaddy(TeleBot):
  def __init__(self, token):
    self.token = token
    self.baseUrl = 'https://api.telegram.org'
    
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
        print(active_bots)
        raise Exception('Bot already exist')
      active_bots[self.id] = {
        "id": self.id,
        "name": self.username
      }
      return True
    return False
  def _start_bot(self):
    self.polling()
  def create(self):
    self.message_handler(func=lambda x: True)(tg_handle)
    BOT = threading.Thread(target=self._start_bot)
    BOT.start()

if __name__ == '__main__':
  app = web_server(BotDaddy)
  app.run()