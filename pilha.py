# pilha = stack
# LIFO = Last In First Out
class Stack:
  def __init__(self):
    # creating an empty list
    self.stack = []
    self.stack_length = 0

  def push(self, element):
    self.stack.append(element)

    self.stack_length += 1

  def pop(self):
    if not self.empty():

      lastElement = self.stack[-1]

      self.stack = self.stack[0:self.stack_length-1]
      # self.stack.pop()
      # self.stack.pop(self.stack_length-1)

      self.stack_length -= 1

      return lastElement

  def top(self):
    if not self.empty():
      return self.stack[-1]
    return None

  def empty(self):
    if (self.stack_length == 0):
      return True
    return False

  def length(self):
    return self.stack_length

s = Stack()

s.push(1)
print(s.stack)

s.push(2)
print(s.stack)

s.push(3)
print(s.stack)

print('Empty => %s' % (s.empty()))

print(s.top())

s.pop()
print(s.stack)

s.pop()
print(s.stack)

s.pop()
print(s.stack)

print('Empty => %s' % (s.empty()))

print('Lenght => %d' % (s.length()))
