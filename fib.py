# recursive fibbonacci
def fib(n):
  print("fib(n) => fib(%d)" % (n))
  if (n == 1 or n == 2):
    return 1
  print("n-1 => %d  ::  n-2 => %d" % (n - 1, n - 2))
  return fib(n - 1) + fib(n - 2)

print(fib(3))
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987