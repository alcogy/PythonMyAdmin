import mysql.connector
from config import Config

def post_query(database, sql):
  conf = Config()
  db = mysql.connector.connect(
    user=conf.value(database, 'user'),
    password=conf.value(database, 'password'),
    host=conf.value(database, 'host'),
    database=database,
  )
  result = []
  cur = db.cursor()
  try:
    cur.execute(sql)
    result.append([i[0] for i in cur.description])
    for data in cur.fetchall():
      result.append(data)
    cur.close()
  except ValueError as err:
    print(err)
  finally :
    cur.close()
  return result

def fetch_tables(db):
  sql = "show tables"
  return post_query(db, sql)