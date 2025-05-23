from flask import (
  Blueprint,
  jsonify,
  render_template,
  current_app,
  request
)

api = Blueprint('api', __name__)

@api.route('/newbot/<token>')
def new_bot(token):
  try:
    telebot = current_app.config.get('TELEBOT')
    tb = telebot(token)
    tb.start()
    return jsonify({
      "name": tb.username,
      "id": tb.id
    })
  except Exception as e:
    tb.stop()
    return jsonify({"error": f"{e}"})

@api.route('/create-bot', methods=['POST'])
def create_bot():
  try:
    data = request.get_json()
    token = data.get('token')
    botadmin = data.get('botadmin')
    prefix = data.get('prefix')
    commands = data.get('commands')
    events = data.get('events')
    
    if not token or not botadmin:
      return jsonify({"error": "Invalid input data"}), 1504
    if len(commands) < 1:
      return jsonify({"error": "Please select commands at least one"}), 1501
    
    x_commands = [name for name in current_app.config['COMMANDS']]
    x_events = [name for name in current_app.config['EVENTS']]
    commands = commands if commands != x_commands else ["*"]
    events = events if events != x_events else ["*"]
    
    telebot = current_app.config.get('TELEBOT')
    tb = telebot(
      token,
      commands, events,
      botadmin,
      prefix or None
    )
    tb.start()
    return jsonify({
      "name": tb.username,
      "id": tb.id
    }), 200
  except Exception as e:
    tb.stop()
    return jsonify({"error": str(e)}), 1502
  except ValueError as ve:
    tb.stop()
    return jsonify({"error": str(ve)}), 1502