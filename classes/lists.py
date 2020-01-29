# -*- coding: utf-8 -*-
import random

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# concatenating
list3 = list1 + list2
print(list3)
# [1, 2, 3, 4, 5, 6, 7, 8]


print(type(list3))
# <class 'list'>


# pop by default removes the last element
# remove last element
list3.pop()
# or
# list3.pop(len(list3) - 1)
print(list3)
# [2, 3, 4, 5, 6, 7]

# remove first element
list3.pop(0)
print(list3)
# [2, 3, 4, 5, 6, 7, 8]


# remove through element itself
list3.remove(2)
print(list3)
# [3, 4, 5, 6, 7]


# append a given element in the final of list
list3.append(10)
print(list3)
# [3, 4, 5, 6, 7, 10]


# insert a given element in the specified index in the list
list3.insert(0, 2)
print(list3)
# [2, 3, 4, 5, 6, 7, 10]


# the remove method throws an error if the element isn't in the
# given list, this will check first if element is not absent
num = 10
if num in list3:
  list3.remove(num)
else:
  print('Element %d is not in list' % (num))
print(list3)
# [2, 3, 4, 5, 6, 7]


# the last element can be reached through index -1
print(list3[-1])
# 7

# from index 0 until index 1 (2-1)
print(list3[0:2])
# [2, 3]

# first element in reverse form
print(list3[-(len(list3))])
# [2]


# if we just assign the value of the list3 to another list, aiming to create a new list
# this will be by reference, but if we don't want this behavior, we must use the 'list' method
# that really creates a new list independently from the original source list
# list4 = list3
list4 = list(list3)
list4.pop()
list4.pop()
list4.pop()
list4.pop()
print(list4)
# [2, 3]

# unpacking values from list
two, three = list4
print(two, three)
# 2 3


# choice a number randomly from a given list
print(random.choice(list4))

# shuffle the list
random.shuffle(list4)
print(list4)


# tuple from list
tuple1 = tuple(list3)
print(tuple1)
# (3, 4, 5, 6, 7)
print(type(tuple1))
# <class 'tuple'>
