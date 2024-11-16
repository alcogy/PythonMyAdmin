from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path="/static")
CORS(app)

@app.route('/api/<param>')
def api_sample(param):
  return jsonify({"param": param})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  title= 'PythonMyAdmin'
  return render_template("index.html", **locals())

def create_app():
  return app
