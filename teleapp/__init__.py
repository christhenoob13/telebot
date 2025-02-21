from flask import Flask

# (°)
#from .views import view
from .api import api

def web_server(telebot):
  app = Flask(__name__)
  app.secret_key = "Teleeeeeeeeebotttt!!!"
  app.config['TELEBOT'] = telebot
  
  #app.register_blueprint(view)
  app.register_blueprint(api, url_prefix='/api')
  
  return app