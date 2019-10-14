# sets
a = {1, 2, 3}
b = {3, 4, 5}

# difference = O(len(set1))
# c = a.difference(b)
c = a - b
print(c)
# {1, 2}

# intersection = O(min(len(set1), len(set2)))
# d = a.intersection(b)
d = a & b
print(d)
# {3}

# union = O(len(set1) + len(set2))
# e = a.union(b)
e = a | b
print(e)
# {1, 2, 3, 4, 5}
