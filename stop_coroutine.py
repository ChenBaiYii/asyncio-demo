#!/usr/bin/python3

import time
import asyncio


async def do(x):
    print("waiting: ", x)
    await asyncio.sleep(x)
    return f"done after {x}s"


coroutine_1 = do(1)
coroutine_2 = do(2)
coroutine_3 = do(3)

tasks = [
    asyncio.ensure_future(coroutine_1),
    asyncio.ensure_future(coroutine_2),
    asyncio.ensure_future(coroutine_3)]

start = time.time()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print("is cancel?  ", task.cancel())
        print("is done? ", task.done())

    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print("time ", time.time() - start)

