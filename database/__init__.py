import mysql.connector

db = mysql.connector.connect(
  user='user',
  password='pass',
  host='localhost',
  database='mossapi',
)

def post_query(sql):
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