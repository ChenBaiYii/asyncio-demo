#!/usr/bin/python3
import time
import asyncio


async def worker(arg):
    print(f"in {arg}")
    return "hello"


def callback(future):
    print("callback :", future.result())


start = time.time()
# 创建一个协程对象
coroutine = worker(19)
# 创建一个事件loop
loop = asyncio.get_event_loop()
print(loop)
# 创建一个task任务
task = asyncio.ensure_future(coroutine)
print("任务加入到事件循环之前的状态", task)
task.add_done_callback(callback)
print("任务添加callback之后的状态", task)
# 将task添加到事件循环
loop.run_until_complete(task)
print("任务完成之后的状态", task)

end = time.time()
print(f"time : {end - start}", )
