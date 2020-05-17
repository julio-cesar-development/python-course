# -*- coding: utf-8 -*-
numList = [10, 5, 40, 30, 20]

def selectionSort(vector):
  lenVector = len(vector)

  for i in range(lenVector):
    print('i', i)
    menor = i

    for j in range(i + 1, lenVector):
      print('j', j)

      print('vector[j] => vector[i]', vector[j], vector[i])

      if vector[j] < vector[menor]:
        print('menor')
        menor = j

    print('menor', vector[menor])
    print('vector[i]', vector[i])
    vector[i], vector[menor] = vector[menor], vector[i]

selectionSort(numList)
print(numList)
# [5, 10, 20, 30, 40]
