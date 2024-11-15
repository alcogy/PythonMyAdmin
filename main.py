import server

def run():
  print('Start app')
  app = server.create_app()
  app.run(host='0.0.0.0', port=9999)


if __name__ == "__main__":
  run()