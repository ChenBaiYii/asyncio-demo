#!/usr/bin/python3
#
import asyncio
import time

now = lambda: time.time()


async def do(x):
    print("waiting: ", x)
    # await后面就是调用耗时的操作, 使用await将协程的控制权让出，以便loop调用其他协程
    await asyncio.sleep(x)
    return f"done after {x}s"


start = now()

coroutine = do(3)
loop = asyncio.get_event_loop()

task = loop.create_task(coroutine)
loop.run_until_complete(task)

print("task return: ", task.result())
print("time ", now() - start)
"并发和并行"
