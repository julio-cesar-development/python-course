# fila = queue
# FIFO = First In First Out
class Queue:
  def __init__(self):
    # creating an empty list
    self.queue = []
    self.queue_length = 0

  def push(self, element):
    self.queue.append(element)

    self.queue_length += 1

  def pop(self):
    if not self.empty():
      self.queue.pop(0)

      self.queue_length -= 1

  def empty(self):
    if self.queue_length == 0:
      return True
    return False

  def length(self):
    return self.queue_length

  def front(self):
    if not self.empty():
      return self.queue[0]
    return None


q = Queue()

q.push(1)
print(q.queue)
print(q.front())

q.push(2)
print(q.queue)
print(q.front())

q.push(3)
print(q.queue)

print('Empty => %s' % (q.empty()))

print(q.front())

q.pop()
print(q.queue)

q.pop()
print(q.queue)

q.pop()
print(q.queue)

print('Empty => %s' % (q.empty()))

print('Lenght => %d' % (q.length()))
