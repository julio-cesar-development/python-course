# -*- coding: utf-8 -*-

s = {1, 2, 3, 5}
print(s)
# {1, 2, 3, 5}


# Create a set from other collection
l = [1, 2, 2, 3, 4, 4, 5]

# create a set from a list
s = set(l)
print(s)
# {1, 2, 3, 4, 5}

s.add(6)
print(s)
# {1, 2, 3, 4, 5, 6}

s.update([7, 8, 9, 10])
print(s)
# {1, 2, 3, 4, 6, 7, 8, 9, 10}

s.remove(1)
print(s)
# {2, 3, 4, 6, 7, 8, 9, 10}
