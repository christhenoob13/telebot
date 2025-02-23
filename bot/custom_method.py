from telebot import TeleBot

class Margelet(TeleBot):
  def __init__(self, token):
    super().__init__(token)
  
  def send_reply(self, chatId: int|str, text: str, message_id: int|str, **kwargs) -> None:
    self.send_message(chatId, text, reply_to_message_id=message_id, **kwargs)