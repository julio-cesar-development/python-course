# quick sort algorithm
# algorithm recursive
# not stable

import sys
import random

vector = [5, 1, 9, 7, 8]
print(vector)

recursive_counter = 0

def qs(l, recursive_counter):
  if l:
    left = [x for x in l if x < l[0]]
    print('left => ', left)

    right = [x for x in l if x > l[0]]
    print('right => ', right)

    print('recursive_counter %d\n' % (recursive_counter))

    if len(left) > 1:
      recursive_counter += 1
      left = qs(left, recursive_counter)

    if len(right) > 1:
      recursive_counter += 1
      right = qs(right, recursive_counter)

    print('l', l)
    print('left', left)
    print('right', right)
    print('l[0]]', l[0])
    print('l.count(l[0])', l.count(l[0]))
    print('return {} \n'.format(left + [l[0]] * l.count(l[0]) + right))

    return left + [l[0]] * l.count(l[0]) + right
  return []

print(qs(vector, recursive_counter))
