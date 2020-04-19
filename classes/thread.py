from threading import Thread
import time

# time.sleep suspends only the execution in the specific Thread in multithreaded programs

def func1():
  print('START func1')
  # time.sleep(2)
  print('FINISH func1')

def func2():
  print('START func2')
  time.sleep(2)
  print('FINISH func2')

def func3():
  print('START func3')
  time.sleep(2)
  print('FINISH func3')

t1 = Thread(target=func1)
t2 = Thread(target=func2)
t3 = Thread(target=func3)

t1.start()
t2.start()
t3.start()
