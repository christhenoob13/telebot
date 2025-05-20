def format_data(bot, data):
  AV = bot.get_chat(data.chat.id)
  if data.chat.type == 'private':
    return str(data.chat.id), {
      "type": 'private',
      "id": data.chat.id,
      "is_bot": data.from_user.is_bot,
      "first_name": data.from_user.first_name,
      "username": data.from_user.username,
      "last_name": data.from_user.last_name,
      "profile": bot.file_to_link(AV.photo.big_file_id) if AV.photo else None
    }
  else:
    return str(data.chat.id), {
      "id": AV.id,
      "type": AV.type,
      "title": AV.title,
      "photo": bot.file_to_link(AV.photo.big_file_id) if AV.photo else None,
      "members": bot.get_chat_member_count(data.chat.id),
      "pinned_message": AV.pinned_message,
      "invite_link": AV.invite_link,
      "status": bot.get_chat_member(data.chat.id, bot.get_me().id).status
    }

def handleChats(bot, data):
  chat = bot.chats
  
  # delete chat if bot leave/kicked
  if data.content_type == 'left_chat_member' and data.left_chat_member.id:
    j = chat.remove(data.chat.id)
    if not j:
      print(f"[ERROR]: Unable to delete ID:{data.cjat.id} on database")
    return
  
  # if chat is not in database
  if not chat.check(str(data.chat.id)):
    key, value = format_data(bot, data)
    aDd = chat.add(key, value)
    if not aDd:
      print("[ERROR]: unable to add chat-data to bot's database")
    # web log
  else:
    # update data if chat changed the photo/title etc.
    if data.content_type in ['new_chat_members', 'left_chat_member', 'delete_chat_photo', 'new_chat_title', 'new_chat_photo', 'pinned_message']:
      key2, value2 = format_data(bot, data)
      adD = chat.update(key2, value2)
      if not adD:
        print("[ERROR]: unable to update chat-data to bot's database")
      # web log