# #!/usr/bin/python

# # Launch me with : python main.py

# https://pypi.org/project/websockets/
 
import asyncio
from websockets.server import serve
import time

async def echo(websocket):
    for i in range(10):
        await websocket.send(str(i))
        time.sleep(1)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())