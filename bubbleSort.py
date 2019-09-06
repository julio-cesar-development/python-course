# -*- coding: utf-8 -*-
numList = [50, 40, 30, 10, 20]

def bubbleSort(vector):
  i = 0
  j = i + 1

  for i in range (0, len(vector) - 1):
    for j in range (i + 1, len(vector)):
      print("vector[i] {} | vector[j] {} | > {}".format(vector[i], vector[j], vector[i] > vector[j]))
      print(vector)
      if vector[i] > vector[j]:
        vector[i], vector[j] = vector[j], vector[i]
      print(vector)

bubbleSort(numList)
print(numList)
