import json
from flask import (
  Blueprint,
  jsonify,
  render_template,
  current_app
)

view = Blueprint('view', __name__)

@view.route('/')
def root():
  commands = current_app.config['COMMANDS']
  events = current_app.config['EVENTS']
  return render_template('index.html',
    title='Telebot',
    aid='telebot',
    commands=commands,
    events=events
  ), 200

@view.route('/active')
def online():
  data = current_app.config.get('ONLINE_BOT', {})
  online = [
    {"id":value.id,"name":value.username} for key, value in data.items()
  ]
  return render_template('active.html', title='Active Bot', data=online, aid='active'), 200