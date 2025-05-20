from .bot_handler import (
  handleEvent, handleCommand,
  handleChats
)

ALL_CONTENT_TYPES = [
    'text', 'audio', 'document', 'animation', 'game', 'photo', 'sticker', 'video', 'video_note',
    'voice', 'location', 'contact', 'venue', 'dice', 'new_chat_members', 'left_chat_member',
    'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created',
    'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id',
    'migrate_from_chat_id', 'pinned_message', 'invoice', 'successful_payment',
    'connected_website', 'poll', 'passport_data', 'proximity_alert_triggered',
    'video_chat_scheduled', 'video_chat_started', 'video_chat_ended',
    'video_chat_participants_invited', 'web_app_data', 'message_auto_delete_timer_changed',
    'forum_topic_created', 'forum_topic_closed', 'forum_topic_reopened', 'forum_topic_edited',
    'general_forum_topic_hidden', 'general_forum_topic_unhidden', 'write_access_allowed',
    'user_shared', 'chat_shared', 'story'
]

def handler(bot):
  @bot.message_handler(content_types=ALL_CONTENT_TYPES)
  def content_type_text(msg):
    handleEvent(bot, msg)
    handleChats(bot, msg)
    if msg.content_type == 'text':
      if msg.text.startswith(bot.prefix):
        handleCommand(bot, msg)
  
  @bot.callback_query_handler(func=lambda call: True)
  def callback_handler(call):
    action = bot.callback_register.get(call.data)
    if action:
      action(call)
    else:
      bot.send_message(call.message.chat.id, "❌ Unknown action!")