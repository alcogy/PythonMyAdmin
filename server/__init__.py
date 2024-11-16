from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import database as db

app = Flask(__name__, static_folder='static', static_url_path="/static")
CORS(app)

@app.post('/api/sql')
def post_sql():
  body = request.json
  print(body)
  data = db.post_query(body['sql'])
  return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  title= 'PythonMyAdmin'
  return render_template("index.html", **locals())

def create_app():
  return app
