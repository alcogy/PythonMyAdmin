from flask import Flask, render_template
from flask_cors import CORS
import server.handler as h

app = Flask(__name__, static_folder='static', static_url_path="/static")
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  title= 'PythonMyAdmin'
  return render_template("index.html", **locals())

app.add_url_rule('/api/sql', 'sql', h.post_sql, None, methods=['POST'])
app.add_url_rule('/api/dblist', 'dblist', h.fetch_db_list, None, methods=['GET'])
app.add_url_rule('/api/tables/<database>', 'tablelist/<database>', h.fetch_table_list, None, methods=['GET'])
app.add_url_rule('/api/config/<database>', 'get_configure', h.get_configure, None, method=['GET'])
app.add_url_rule('/api/config', 'post_configure', h.post_configure, None, method=['POST'])
app.add_url_rule('/api/config', 'put_configure', h.post_configure, None, method=['PUT'])
app.add_url_rule('/api/config/<database>', 'delete_configure', h.post_configure, None, method=['DELETE'])


def create_app():
  return app
