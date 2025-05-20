# Telebot
basta bot to sa telegram

## echo command
```python
def echo(bot, data):
  if not data.msg.args:
    return data.reply("Please provide a message to echo.")
  bot.send_message(
    data.chat.id,
    f"ECHO: {data.msg.args}"
  )

config = dict(
  name = "echo",              # (required) command name
  run = echo,                 # (required) your command function
  author = "Greegmon",        # enter your name
  adminOnly = False,          # only admin can use the cmd (if True)
  usage = "{p}echo [text]",   # how to use your command
  description = "Your text.." # short desc of your command
)
```

# Documentation

### event types
di ko alam ilalagay ko, basta sa events type to.

<h3>📩 Basic Content Types</h3>
<ul>
  <li><b>text</b> – Plain text messages.</li>
  <li><b>audio</b> – Audio files (e.g., music or voice memos in MP3 format).</li>
  <li><b>document</b> – Files like PDFs, ZIPs, DOCXs.</li>
  <li><b>animation</b> – Animated GIFs (treated as video).</li>
  <li><b>photo</b> – Image files (e.g., JPEG, PNG).</li>
  <li><b>video</b> – Video files (e.g., MP4).</li>
  <li><b>video_note</b> – Round, short video messages.</li>
  <li><b>voice</b> – Voice messages (OGG format).</li>
</ul>

<h3>🎮 Interactive & Entertainment</h3>
<ul>
  <li><b>game</b> – Telegram HTML5 games.</li>
  <li><b>sticker</b> – Static or animated Telegram stickers.</li>
  <li><b>dice</b> – Random dice roll (🎲, 🎯, etc.).</li>
</ul>

<h3>📍 Location & Contact</h3>
<ul>
  <li><b>location</b> – Shared GPS location.</li>
  <li><b>contact</b> – Shared contact information.</li>
  <li><b>venue</b> – Shared location with name and address.</li>
</ul>

<h3>👥 Chat Member Events</h3>
<ul>
  <li><b>new_chat_members</b> – New member(s) joined the group.</li>
  <li><b>left_chat_member</b> – A member left or was removed.</li>
</ul>

<h3>🛠 Chat Meta Changes</h3>
<ul>
  <li><b>new_chat_title</b> – Chat title was changed.</li>
  <li><b>new_chat_photo</b> – Chat photo was updated.</li>
  <li><b>delete_chat_photo</b> – Chat photo was removed.</li>
  <li><b>group_chat_created</b> – A basic group was created.</li>
  <li><b>supergroup_chat_created</b> – A supergroup was created.</li>
  <li><b>channel_chat_created</b> – A channel was created.</li>
  <li><b>migrate_to_chat_id</b> – Group was upgraded to supergroup.</li>
  <li><b>migrate_from_chat_id</b> – Supergroup created from a group.</li>
  <li><b>pinned_message</b> – A message was pinned in the chat.</li>
</ul>

<h3>💸 Payments</h3>
<ul>
  <li><b>invoice</b> – An invoice was sent to the user.</li>
  <li><b>successful_payment</b> – A payment was successfully completed.</li>
  <li><b>connected_website</b> – A website connected via Telegram login.</li>
</ul>

<h3>📊 Polls & Feedback</h3>
<ul>
  <li><b>poll</b> – A poll was sent.</li>
  <li><b>passport_data</b> – Telegram Passport data was sent.</li>
  <li><b>proximity_alert_triggered</b> – Nearby user alert triggered.</li>
</ul>

<h3>🎥 Video Chat</h3>
<ul>
  <li><b>video_chat_scheduled</b> – A video chat was scheduled.</li>
  <li><b>video_chat_started</b> – A video chat started.</li>
  <li><b>video_chat_ended</b> – A video chat ended.</li>
  <li><b>video_chat_participants_invited</b> – Participants were invited.</li>
</ul>

<h3>🌐 Web & Miscellaneous</h3>
<ul>
  <li><b>web_app_data</b> – Data received from a Telegram Web App.</li>
  <li><b>message_auto_delete_timer_changed</b> – Auto-delete timer updated.</li>
  <li><b>write_access_allowed</b> – Bot granted permission to write messages.</li>
  <li><b>user_shared</b> – A user profile was shared.</li>
  <li><b>chat_shared</b> – A chat was shared with the bot.</li>
  <li><b>story</b> – A Telegram Story was posted.</li>
</ul>

<h3>🧵 Forum Topics</h3>
<ul>
  <li><b>forum_topic_created</b> – A forum topic was created.</li>
  <li><b>forum_topic_closed</b> – A forum topic was closed.</li>
  <li><b>forum_topic_reopened</b> – A forum topic was reopened.</li>
  <li><b>forum_topic_edited</b> – A forum topic was edited.</li>
  <li><b>general_forum_topic_hidden</b> – The general topic was hidden.</li>
  <li><b>general_forum_topic_unhidden</b> – The general topic was unhidden.</li>
</ul>