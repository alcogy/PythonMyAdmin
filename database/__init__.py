import mysql.connector

# MySQL Core.
class Database:

  def __init__(self):
    self.conn = mysql.connector.connect(
      user='user',
      password='pass',
      host='localhost',
      database='mossapi',
    )

  def select(self) -> list:
    result = []
    cur = self.conn.cursor()
    cur.execute("select * from bland")
    for data in cur.fetchall():
      result.append(data)
    return result