# deque = deck
# double-ended queue
class Deck:
  def __init__(self):
    # creating an empty list
    self.deck = []
    self.len = 0

  def empty(self):
    if self.len == 0:
      return True
    return False

  def push_front(self, element):
    self.deck.insert(0, element)
    self.len += 1

  def push_back(self, element):
    self.deck.insert(self.len, element)
    self.len += 1

  def pop_front(self):
    if not self.empty():
      self.deck.pop(0)
      self.len -= 1

  def pop_back(self):
    if not self.empty():
      self.deck.pop(self.len - 1)
      self.len -= 1

  def front(self):
    if not self.empty():
      return self.deck[0]

  def back(self):
    if not self.empty():
      return self.deck[-1]

  def show(self):
    for i in self.deck:
      print(i, end = ' ')

d = Deck()
d.push_front(10)
d.push_front(5)

print(d.deck)
# [5, 10]

d.push_back(15)
d.push_back(20)

print(d.deck)
# [5, 10, 15, 20]

d.push_front(0)
d.push_back(25)

print(d.deck)
# [0, 5, 10, 15, 20, 25]

d.pop_back()

print(d.deck)
# [0, 5, 10, 15, 20]

d.pop_front()

print(d.deck)
# [5, 10, 15, 20]