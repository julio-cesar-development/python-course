def foo():
  list = [2, 4, 6]
  for x in list:
    yield x

callFoo1 = foo()
print(callFoo1)
# <generator object foo>
print(next(callFoo1))
# 2
print(next(callFoo1))
# 4
print(next(callFoo1))
# 6
# print(next(callFoo1))
# StopIteration

callFoo2 = foo()
for value in callFoo2:
  print(value)
# 2
# 4
# 6
