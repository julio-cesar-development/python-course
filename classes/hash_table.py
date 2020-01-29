import sys

class HashTable:
  def __init__(self, table_size):
    # h(k) = k mod m
    # m is the table_size
    # k is the key
    # function hashing of k is the remnant of k divided by m
    if table_size < 1:
      print('Err: table size must be positive')
      sys.exit(1)

    self.table_size = table_size
    self.table = [[] for i in range(table_size)] # create an empty list for each entry in table

  def hash_func(self, key):
    # returns the remnant of key divided by table_size
    return key % self.table_size

  def insert(self, key):
    self.table[self.hash_func(key)].append(key)

  def search(self, key):
    if key in self.table[self.hash_func(key)]:
      return True
    return False

  def show(self):
    for key_linked_list, value_linked_list in enumerate(self.table):
      if value_linked_list:
        print('%d =>' % key_linked_list, end = ' ')
        for key in value_linked_list:
          print('%d' % key, end = ' ')
        print(' ')



ht = HashTable(9)

ht.insert(19) # 19 mod 9 = 1
ht.insert(28) # 28 mod 9 = 1
ht.insert(20) # 20 mod 9 = 2
ht.insert(5)  # 5  mod 9 = 5
ht.insert(33) # 33 mod 9 = 6
ht.insert(15) # 15 mod 9 = 6

ht.show()
# 1 => 19 28
# 2 => 20
# 5 => 5
# 6 => 33 15
