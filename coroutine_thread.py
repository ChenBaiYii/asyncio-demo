#!/usr/bin/python3
import asyncio
import time
from threading import Thread


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do(x):
    print("waiting for: ", x)
    await asyncio.sleep(x)
    print(f"done after {x}s")


def more_work(x):
    print("work {}".format(x))
    time.sleep(x)
    print("finished more work {}".format(x))


start_time = time.time()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

asyncio.run_coroutine_threadsafe(do(6), new_loop)
asyncio.run_coroutine_threadsafe(do(4), new_loop)
print("time ", time.time() - start_time)
