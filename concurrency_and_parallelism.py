#!/usr/bin/python3
#

import time
import asyncio


async def do(x):
    print("waiting: ", x)
    await asyncio.sleep(x)
    return f"done after {x}s"


start = time.time()

coroutine_1 = do(1)
coroutine_2 = do(2)
coroutine_3 = do(3)

tasks = [
    asyncio.ensure_future(coroutine_1),
    asyncio.ensure_future(coroutine_2),
    asyncio.ensure_future(coroutine_3)]

loop = asyncio.get_event_loop()

# loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(asyncio.gather(*tasks))

for t in tasks:
    print("task return: ", t.result())
print("time", time.time() - start)

