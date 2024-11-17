from flask import request, jsonify, abort
import database as db
from config import Config

def post_sql():
  """ just execute sql. """
  body = request.json
  if not 'db' in body or not 'sql' in body:
    print('Post parameter must have "db" and "sql"')
    print(body)
    return abort(500, 'Post parameter must have "db" and "sql"')
  data = db.post_query(body['db'], body['sql'])
  return jsonify(data)


def fetch_db_list():
  """ return database list from ini file. """
  c = Config()
  return c.sections()
  

def fetch_table_list(database):
  """ fetch show tables """
  if database == '':
    return abort(500, 'Must select database.')
  result = db.fetch_tables(database)
  return result[1:]
