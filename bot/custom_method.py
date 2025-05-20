from telebot import TeleBot

class Margelet(TeleBot):
  def __init__(self, token):
    self.callback_register = {}
    super().__init__(token)
  
  # reply to the message
  def send_reply(self, chatId: int|str, text: str, message_id: int|str, **kwargs) -> None:
    self.send_message(chatId, text, reply_to_message_id=message_id, **kwargs)
  
  # decorator to handle callbacks
  def callback(self, key):
    def decorator(func):
      self.callback_register[key] = func
      return func
    return decorator
  
  # get chat profile picture
  def file_to_link(self, file_id):
    info = self.get_file(file_id)
    return f"{self.baseUrl}/file/bot{self.token}/{info.file_path}"