import time
import asyncio


async def worker(arg):
    print(f"in {arg}")


start = time.time()

# 创建一个协程对象
coroutine = worker(19)
# 创建一个事件loop
loop = asyncio.get_event_loop()
# 将协程添加到事件循环
loop.run_until_complete(coroutine)
end = time.time()
print(f"time : {end - start}", )
