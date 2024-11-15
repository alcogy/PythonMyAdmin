from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder='static', static_url_path="/static")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return render_template("index.html", title="PythonMyAdmin")

def create_app():
  return app
