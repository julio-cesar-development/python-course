# -*- coding: utf-8 -*-
numList = [10, 5, 40, 30, 20]

def bubbleSort(vector):
  lenVector = len(vector)
  i = lenVector - 1

  while i > 0:
    print('i', i)

    swapped = False
    print('range(i)', range(i))

    for j in range(i):
      print('vector[j] => vector[j + 1]', vector[j], vector[j + 1])

      if vector[j] > vector[j + 1]:
        vector[j], vector[j + 1] = vector[j + 1], vector[j]
        swapped = True
        print('swapped True')

    if not swapped:
      break

    i -= 1

bubbleSort(numList)
print(numList)
# [5, 10, 20, 30, 40]
