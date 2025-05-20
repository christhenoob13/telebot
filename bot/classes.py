class BotChats:
  def __init__(self):
    self.chats = dict()
  
  def check(self, cid: str) -> bool:
    return True if cid in self.chats else False
  
  def add(self, chat_id: str, data: dict) -> bool:
    if chat_id in self.chats:
      return False
    self.chats[chat_id] = data
    return True
  
  def remove(self, chat_id: str) -> bool:
    if chat_id in self.chats:
      del self.chats[chat_id]
      return True
    else:
      return False
  
  def update(self, cid: str, data: dict) -> bool:
    if cid not in self.chats:
      return False
    self.chats[cid] = data
    return True
  
  def get_id(self, cid: str) -> dict:
    if cid in self.chats:
      return self.chats[cid]
    print(f"ERROR: {cid} id is not in BotChats data")
    return {}
  
  def get_all(self):
    return self.chats
  
  def get_all_type(self, type: str) -> list|None:
    if type.lower() not in ['private', 'group', 'supergroup', 'channel']:
      return None
    return [value for _,value in enumerate(self.chats) if value['type'] == type]