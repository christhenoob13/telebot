from flask import Flask

# (°)
from .views import view
from .api import api

def web_server(telebot, online, cmdevents):
  app = Flask(__name__)
  app.secret_key = "sikretong malupet pede pa bulong!!!"
  app.config['TELEBOT'] = telebot
  app.config['ONLINE_BOT'] = online
  app.config['COMMANDS'] = cmdevents['commands']
  app.config['EVENTS'] = cmdevents['events']
  
  app.register_blueprint(view)
  app.register_blueprint(api, url_prefix='/api')
  
  return app