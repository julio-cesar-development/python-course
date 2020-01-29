# using a ordered list
class Pessoa():
  '''
    nome
    priority
  '''
  def __init__(self, name, priority):
    self.name = name
    self.priority = priority

  def getName(self):
    return self.name

  def getPriority(self):
    return self.priority



class PriorityQueue:
  # this queue will be ordered by priority
  def __init__(self, order):
    self.pq = [] # priority queue
    self.len = 0 # length of priority queue
    self.order = order

  def empty(self):
    if (self.len == 0):
      return True
    return False

  def push(self, person):
    if self.empty():
      self.pq.append(person)
    else:
      flag_push = False

      # look up where to insert in queue
      for i in range(self.len):
        if (self.order == 'descendent'):
          if self.pq[i] != None and self.pq[i].getPriority() < person.getPriority():
            self.pq.insert(i, person)
            flag_push = True
            break
        else: # ascending
          if self.pq[i] != None and self.pq[i].getPriority() > person.getPriority():
            self.pq.insert(i, person)
            flag_push = True
            break

      # couldn't be inserted, will be in the last index
      if not flag_push:
        self.pq.insert(self.len, person)

    self.len += 1

  def pop(self):
    if not self.empty():
      self.pq.pop(0)

      self.len -= 1

  def show(self):
    for p in self.pq:
      print('Name => %s :: Priority => %d\n' % (p.getName(), p.getPriority()))



p1 = Pessoa('p1', 10)
p2 = Pessoa('p2', 50)
p3 = Pessoa('p3', 40)
p4 = Pessoa('p4', 30)
p5 = Pessoa('p5', 20)

pq = PriorityQueue('descendent')
pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)
pq.push(p5)

pq.show()

print('\n')

pq.pop()
pq.pop()
pq.pop()

pq.show()
