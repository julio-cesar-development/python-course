

numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x*x, numeros)

for n in quadrados:
  print(n)


quadrados2 = [x*x for x in numeros]
print(quadrados2)
# [1, 4, 9, 16, 25]

# for n in quadrados2:
#   print(n)

def cube(x):
  return x**2

nums = [i for i in range(1, 10)]
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# regular cubes
cubes = [i**i for i in range(1, 10)]
print(cubes)

# map
cubesMap = map(cube, nums)

for j in enumerate(cubesMap):
  print(j)

# lambda
cubesLambda = (lambda x: x**2)(2)
print(cubesLambda) # 4


#print(lambda x: x**2)(5)
#print(lambda x, y: x*y)(3, 4)

cubesFilter = filter(lambda x: x > 0 and x < 10, cubes)

for i, v in enumerate(cubesFilter):
  print(v)
# 1
# 4


