import configparser

class Config:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read('db.ini')


  def sections(self) -> list:
    """ Return section(database name) list. """
    return self.config.sections()
  
  def has_database(self, db) -> bool:
    """ Return exsist database or none """
    return db in self.config.sections()

  def value(self, db, key) -> str:
    """ Return specific value """
    if not self.config.has_section(db):
      return ''

    if self.config[db].get(key) == None:
      return ''
    
    return self.config[db][key]


  def update(self, db, key, value) -> bool:
    """ Update specific value and ini file. If key is none return false"""
    if self.value(db, key) == '':
      return False
    
    self.config[db][key] = value
    with open('db.ini', 'w') as file:
      self.config.write(file)
    
    return True
  

  def insert(self, db, obj) -> bool:
    """ Insert New DB configure. """
    if self.has_database(db):
      print('exists database')
      return False
    
    if not 'user' in obj or not 'password' in obj or not 'host' in obj: 
      print('need keys user, password, host.')
      print(obj)
      return False
    
    for key in obj.keys():
      if key != 'user' and key != 'password' and key != 'host':
        print('attributes only user, password, host. you set ' + key)
        return False
      
    self.config[db] = obj
    with open('db.ini', 'w') as file:
      self.config.write(file)
    
    return True
  

  def delete(self, db) -> bool:
    """ Delete Database configure. """
    if not self.has_database(db):
      print('not exists database')
      return False
    
    self.config.remove_section(db)
    with open('db.ini', 'w') as file:
      self.config.write(file)
    
    return True

