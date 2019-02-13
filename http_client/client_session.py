#!/usr/bin/python3
import asyncio
from asyncio import transports
from typing import Optional


class ClientProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop
        self.transport = None
        self._eof = False  # 没有收到 EOF
        self._waiter = None  # 用来等待接收数据的 future

    def connection_made(self, transport: transports.BaseTransport):
        self.transport = transport

    def eof_received(self):
        self._eof = True
        self._wakeup_waiter()

    def data_received(self, data: bytes):
        print(data.decode())

    def connection_lost(self, exc: Optional[Exception]):
        # self.loop.stop()
        pass  # 不再调用 self.loop.stop()

    async def wait_for_data(self):
        assert not self._eof
        assert not self._waiter


class ClientSession:
    def __init__(self, loop):
        self._loop = loop

    async def get(self, url, host, port):
        transport, protocol = await self._loop.create_connection(
            lambda: ClientProtocol(loop), host, port
        )
        request = f'GET {url} HTTP/1.1\r\nHost: {host}\r\n'
        transport.write(request.encode())


loop = asyncio.get_event_loop()
l = ClientSession(loop)
loop.run_until_complete(l.get('/', "localhost", 8000))  # 协程 main() 只是创建好连接
loop.run_forever()  # 如果没有 run_forever()，在收到数据之前，loop 可能就结束了

print("done")
