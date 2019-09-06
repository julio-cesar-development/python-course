
def fat(n):
  if (n == 0):
    return 1
  return (n * fat(n - 1))

print(fat(4)) # 24 = 4 * 3 * 2 * 1


fat_lambda = lambda n: n * fat_lambda(n - 1) if n > 1 else 1

print(fat_lambda(4)) # 24 = 4 * 3 * 2 * 1
