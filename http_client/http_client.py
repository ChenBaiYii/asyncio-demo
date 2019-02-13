#!/usr/bin/python3
import asyncio
from asyncio import transports
from typing import Optional


class ClientProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop

    def connection_made(self, transport: transports.BaseTransport):
        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        transport.write(request.encode())

    def data_received(self, data: bytes):
        print(data.decode())

    def connection_lost(self, exc: Optional[Exception]):
        self.loop.stop()


async def main(loop):
    await loop.create_connection(
        lambda: ClientProtocol(loop), 'localhost', 8000)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))  # 协程 main() 只是创建好连接
loop.run_forever()  # 如果没有 run_forever()，在收到数据之前，loop 可能就结束了

print("done")
