import asyncio
import time

# working with coroutines using the asyncio APIs

async def sleepTime():
  await asyncio.sleep(1)
  return True

async def main():
  print(f"started at {time.strftime('%I:%M:%S %p')}")

  initialTime = time.time()

  await sleepTime()
  print("[sleepTime] took %.2f seconds" % (time.time() - initialTime))
  print(f"finished [sleepTime] at {time.strftime('%I:%M:%S %p')}")

  initialTime = time.time()

  # all tasks will run concurrently
  task1 = asyncio.create_task(sleepTime())
  task2 = asyncio.create_task(sleepTime())
  task3 = asyncio.create_task(sleepTime())
  await task1
  await task2
  await task3

  print("[TASKS] took %.2f seconds" % (time.time() - initialTime))
  print(f"finished [TASKS] at {time.strftime('%I:%M:%S %p')}")

asyncio.run(main())
