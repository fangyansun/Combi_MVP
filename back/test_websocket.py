#!/usr/bin/env python

import asyncio

from websockets.asyncio.server import serve


async def websocket_handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)


async def main():
    async with serve(websocket_handler, "192.168.137.1", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())