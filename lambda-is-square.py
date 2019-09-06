
numeros = list(range(0, 10))
print(numeros)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# The both sintaxes are corrects
is_square = [x % 2 == 0 for x in numeros]
# is_square = [x for x in numeros if (x % 2 == 0)]


print(is_square)
# [True, False, True, False, True, False, True, False, True, False]


filter_greater_than_five = filter(lambda x: x > 5, numeros)
filtered = []

for n in filter_greater_than_five:
  filtered.append(n)

print(filtered)
# filtered
