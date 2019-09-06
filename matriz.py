matriz = [
  [0, 1, 2, 3, 4],
  [5, 6, 7, 8, 9],
  [10, 11, 12, 13, 14],
  [15, 16, 17, 18, 19],
  [20, 21, 22, 23, 24],
]

print(matriz[0][0])
# 0

print(matriz[1][1])
# 6

print(matriz[2][2])
# 12

print(matriz[3][3])
# 18

print(matriz[4][4])
# 24

print('')

for row in matriz:
  for col in row:
    print(str(col) + '\t', end = ' ')
  print('')
