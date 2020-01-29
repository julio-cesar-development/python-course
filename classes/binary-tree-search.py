class Node:
  def __init__(self, label):
    self.label = label
    self.left = None
    self.right = None
    # self.root = None

  def getLabel(self):
    return self.label

  def setLabel(self, label):
    self.label = label

  def getLeft(self):
    return self.left

  def setLeft(self, left):
    self.left = left

  def getRight(self):
    return self.right

  def setRight(self, right):
    self.right = right


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def getRoot(self):
    return self.root

  def empty(self):
    if self.root == None:
      return True
    return False

  def showPreOrder(self, curr_node):
    if curr_node != None:
      print('%s' % curr_node.getLabel(), end=' ')
      self.showPreOrder(curr_node.getLeft())
      self.showPreOrder(curr_node.getRight())

  def insert(self, label):
    # creates a new node
    node = Node(label)

    # check if it is empty
    if self.empty():
      # if it is empty, assign the root to be the new node
      self.root = node
    else:
      # tree not empty
      dad_node = None
      # start the course on root node
      curr_node = self.root

      while True:
        # if current node had some value, find in which side to proceed
        if curr_node != None:
          dad_node = curr_node

          # if the node to be inserted will be less than current node, go to left in this subtree
          if node.getLabel() < curr_node.getLabel():
            curr_node = curr_node.getLeft()
          else:
            curr_node = curr_node.getRight()

        # current node is None, we must insert the new node here
        else:
          # if the node to be inserted will be less than the parent, insert it in the left
          if node.getLabel() < dad_node.getLabel():
            dad_node.setLeft(node)
          else:
            dad_node.setRight(node)

          break

  def remove(self, label):
    dad_node = None
    curr_node = self.root

    while curr_node != None:

      if label == curr_node.getLabel():

        if curr_node.getLeft() == None and curr_node.getRight() == None:

          if dad_node == None:
            self.root = None
          else:
            if dad_node.getLeft() == curr_node:
              dad_node.setLeft(None)
            elif dad_node.getRight() == curr_node:
              dad_node.setRight(None)

        elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
          (curr_node.getLeft() != None and curr_node.getRight() == None):

          if dad_node == None:
            if curr_node.getLeft() != None:
              self.root = curr_node.getLeft()
            else:
              self.root = curr_node.getRight()
          else:
            if curr_node.getLeft() != None:
              if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                dad_node.setLeft(curr_node.getLeft())
              else:
                dad_node.setRight(curr_node.getLeft())
            else:
              if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                dad_node.setLeft(curr_node.getRight())
              else:
                dad_node.setRight(curr_node.getRight())

        elif curr_node.getLeft() != None and curr_node.getRight() != None:
          dad_smaller_node = curr_node
          smaller_node = curr_node.getRight()
          next_smaller = curr_node.getRight().getLeft()

          while next_smaller != None:
            dad_smaller_node = smaller_node
            smaller_node = next_smaller
            next_smaller = smaller_node.getLeft()

          if dad_node == None:

            if self.root.getRight().getLabel() == smaller_node.getLabel():
              smaller_node.setLeft(self.root.getLeft())
            else:

              if dad_smaller_node.getLeft() and \
                dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
                dad_smaller_node.setLeft(None)
              else:
                dad_smaller_node.setRight(None)

              smaller_node.setLeft(curr_node.getLeft())
              smaller_node.setRight(curr_node.getRight())

            self.root = smaller_node

          else:

            if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
              dad_node.setLeft(smaller_node)
            else:
              dad_node.setRight(smaller_node)

            if dad_smaller_node.getLeft() and \
              dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
              dad_smaller_node.setLeft(None)
            else:
              dad_smaller_node.setRight(None)

            smaller_node.setLeft(curr_node.getLeft())
            smaller_node.setRight(curr_node.getRight())

        break

      dad_node = curr_node

      if label < curr_node.getLabel():
        curr_node = curr_node.getLeft()
      else:
        curr_node = curr_node.getRight()



bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)
# 8 3 1 6 4 7 10 14 13

# bst.insert(8)
# bst.insert(3)
# bst.insert(6)
# bst.insert(4)
# bst.insert(1)
# bst.insert(10)
# bst.insert(7)
# bst.insert(14)
# bst.insert(13)
# 8 3 1 6 4 7 10 14 13

bst.showPreOrder(bst.getRoot())

print('')

bst.remove(1)
bst.showPreOrder(bst.getRoot())

