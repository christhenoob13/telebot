from flask import (
  Blueprint,
  jsonify,
  render_template,
  current_app
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