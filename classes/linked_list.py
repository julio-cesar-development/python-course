class Node:
  def __init__(self, label):
    self.label = label
    self.next = None

  def getLabel(self):
    return self.label

  def setLabel(self, label):
    self.label = label

  def getNext(self):
    return self.next

  def setNext(self, next):
    self.next = next

class LinkedList:
  def __init__(self):
    self.first = None
    self.last = None
    self.len_list = 0

  # def empty(self):
  #   if self.len_list == 0:
  #     return True
  #   return False

  def empty(self):
    if self.first == None:
      return True
    return False

  def push(self, label, index):
    if index >= 0:
      # creates a new Node
      node = Node(label)

      current_idx = 0

      # check if the list is empty, in this case this new Node will be the first
      if self.empty():
        self.first = node
        self.last = node
      else:
        if index == 0:
          # insertion in the begin
          node.setNext(self.first)
          self.first = node

        elif index >= self.len_list:
          # insertion in the end
          self.last.setNext(node)
          self.last = node

        else:
          # insertion in the middle
          prev_node = self.first
          current_node = self.first.getNext()
          current_idx += 1

          while current_node != None:
            if current_idx == index:
              node.setNext(current_node)
              prev_node.setNext(node)
              break
            prev_node = current_node
            current_node = current_node.getNext()
            current_idx += 1

      # update the list length
      self.len_list += 1

  def pop(self, index):
    if not self.empty() and index >= 0 and index < self.len_list:
      flag_removed = False
      current_idx = 0

      # there is only 1 element in the list
      if self.first.getNext() == None:
        self.first = None
        self.last = None
        flag_removed = True
      elif index == 0:
      # removes from begin but there is more than 1 element
        self.first = self.first.getNext()
        flag_removed = True
      else:
      # there is more than 1 element and the removal is not in begin of list
        prev_node = self.first
        current_node = self.first.getNext()
        current_idx += 1

        while current_node != None:
          if current_idx == index:
            prev_node.setNext(current_node.getNext())
            current_node.setNext(None)
            flag_removed = True
            break

          prev_node = current_node
          current_node = current_node.getNext()
          current_idx += 1

      if flag_removed:
        self.len_list -= 1

  def length(self):
    return self.len_list

  def show(self):
    current_node = self.first

    while current_node != None:
      print(current_node.getLabel(), end=' ')
      current_node = current_node.getNext()
    print('')


lista = LinkedList()

lista.push('Julio', 0)
lista.show()

lista.push('Cesar', 1)
lista.show()

lista.pop(0)
lista.show()

lista.pop(0)
lista.show()

lista.push('D', 0)
lista.push('C', 0)
lista.push('B', 0)
lista.push('A', 0)
lista.show()

lista.pop(0)
lista.pop(2)
lista.show()
