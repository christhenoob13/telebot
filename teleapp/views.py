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
  return render_template('index.html', title='Telebot'), 200

@view.route('/online')
def online():
  data = current_app.config.get('ONLINE_BOT', {})
  online = [
    {"id":value.id,"name":value.username} for key, value in data.items()
  ]
  return render_template('online.html', title='Online Bot', data=online), 200