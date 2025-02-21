from flask import (
  Blueprint,
  jsonify,
  render_template,
  current_app
)

api = Blueprint('view', __name__)

@api.route('/newbot/<token>')
def new_bot(token):
  try:
    telebot = current_app.config.get('TELEBOT')
    tb = telebot(token)
    tb.create()
    return jsonify({
      "name": tb.username,
      "id": tb.id
    })
  except Exception as e:
    return jsonify({"error": f"{e}"})