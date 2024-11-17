import unittest
from config import Config

class TestConfig(unittest.TestCase):
  def init(self):
    c = Config()
    c.overwrite([{
      'db': 'mossapi',
      'config': {
        'user': 'user',
        'password': 'pass',
        'host': 'localhost',
      },
    }])

  def setUp(self):
    self.init()

  def tearDown(self):
    self.init()
    
  def test_read_config(self):
    c = Config()
    self.assertEqual(c.sections(), ['mossapi'])

  def test_config_value(self):
    c = Config()
    val = c.value('mossapi', 'user')
    self.assertEqual(val, 'user')  

  def test_config_none_db(self):
    c = Config()
    val = c.value('aaaa', 'bbbb')
    self.assertEqual(val, '') 

  def test_config_none_value(self):
    c = Config()
    val = c.value('mossapi', 'bbbb')
    self.assertEqual(val, '')  

  def test_update(self):
    import string
    import random
    new_value = ''.join(random.choices(string.ascii_letters, k=8))
    c = Config()
    result = c.update('mossapi', 'user', new_value)
    self.assertEqual(result, True)
    c2 = Config()
    self.assertEqual(c2.value('mossapi', 'user'), new_value)

  def test_has_database(self):
    c = Config()
    result = c.has_database('mossapi')
    self.assertEqual(result, True)

    result = c.has_database('none_database')
    self.assertEqual(result, False)

  def test_insert_and_delete(self):
    db_name = 'my_db'
    user_name = 'myuser'
    data_set = {'user': user_name, 'password': 'mypass', 'host': 'myhost.host.site'}
    
    c = Config()
    result = c.insert(db_name, data_set)
    self.assertEqual(result, True)

    # duplicate error.
    result = c.insert('mossapi', data_set)
    self.assertEqual(result, False)

    # addribute error.
    err_data = {'user': 'user', 'password': ''}
    result = c.insert('error_db', err_data)
    self.assertEqual(result, False)

    c2 = Config()
    result = c2.has_database(db_name)
    self.assertEqual(result, True)

    result = c2.value(db_name, 'user')
    self.assertEqual(result, user_name)


  def test_over_write(self):
    dbs = [
      {
        'db': 'db1',
        'config': {
          'user': 'myuser1',
          'password': 'pass1',
          'host': 'localhost',
        },
      },
      {
        'db': 'db2',
        'config': {
          'user': 'myuser2',
          'password': 'pass2',
          'host': 'localhost2',
        },
      },
      {
        'db': 'db3',
        'config': {
          'user': 'myuser3',
          'password': 'pass3',
          'host': 'localhost3',
        },
      },
    ]
    c = Config()
    c.overwrite(dbs)

    c2 = Config()
    self.assertEqual(c2.sections(), ['db1', 'db2', 'db3'])
    

if __name__ == '__main__':
  unittest.main()
