from threading import Thread, ThreadError
import time

def func(thread_number):
  print('Initializing the thread %d' % (thread_number + 1))
  time.sleep(5)
  print('Ending the thread %d' % (thread_number + 1))

for i in range(10):
  t = Thread(target=func, args=(i,))
  t.start()
