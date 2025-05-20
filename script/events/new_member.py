def function(bot, event):
  try:
    new_members = [user.username for user in event.new_chat_members]
    bot_info = bot.get_me()
    if bot_info.username in new_members:
      chatMember = bot.get_chat_member(event.chat.id, bot_info.id)
      if chatMember.status != 'administrator':
        bot.send_message(event.chat.id,
          f"🎉 <b>{bot_info.first_name}</b> has been successfully connected!\n\n" +
          f"Thank you for inviting me to <b>{event.chat.title}</b>. To unlock my full range of features, " +
          "please consider granting me admin privileges.",
          parse_mode='HTML'
        )
      return
    bot.send_message(event.chat.id,
      f"Hello <i>{', '.join(new_members) if len(new_members)>1 else new_members[0]}</i>. Welcome to <b>{event.chat.title}</b>\n" +
      f"Please enjoy your time here! 🥳♥\n\n" +
      f"Now we have <b>{bot.get_chat_member_count(event.chat.id)}</b> member of this group.",
      parse_mode='HTML'
    )
  except Exception as e:
    print("[ ERROR ]: ", e)

config = dict(
  run = function,
  name = "welcome",
  type = 'new_chat_members',
  author = 'Astro',
  description = "Welcome message to new member"
)