import unittest
from config import Config

class TestConfig(unittest.TestCase):
  def test_read_config(self):
    c = Config()
    self.assertEqual(c.sections(), ['mossapi', 'db2'])

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
    result = c.update('db2', 'user', new_value)
    self.assertEqual(result, True)
    c2 = Config()
    self.assertEqual(c2.value('db2', 'user'), new_value)

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
    result = c.insert('db2', data_set)
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

    # closing
    result = c2.delete(db_name)
    self.assertEqual(result, True)

if __name__ == '__main__':
  unittest.main()
