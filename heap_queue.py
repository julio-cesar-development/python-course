import heapq

class Pessoa:
  def __init__(self, nome):
    self.nome = nome

  # private method to represent the object in a readable way
  def __repr__(self):
    return self.nome


class PriorityQueue:
  def __init__(self):
    self._queue = []
    self._index = 0

  def insert(self, item, priority):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1

  def remove(self):
    return heapq.heappop(self._queue)[-1]


p1 = Pessoa('Julio 1')
print(p1)

p2 = Pessoa('Julio 2')
print(p2)

p3 = Pessoa('Julio 3')
print(p3)

p4 = Pessoa('Julio 4')
print(p4)

print("\n")


q = PriorityQueue()

q.insert(p1, 40)
q.insert(p2, 25)
q.insert(p3, 5)
q.insert(p3, 15)

print(q.remove())
# p1 Julio 1
