#!/usr/bin/python3
import asyncio
import time
from threading import Thread


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print("work {}".format(x))
    time.sleep(x)
    print("finished more work {}".format(x))


start_time = time.time()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print("time ", time.time() - start_time)

new_loop.call_soon_threadsafe(more_work, 6)
new_loop.call_soon_threadsafe(more_work, 3)
