# #!/usr/bin/python

"""
Created on: 06/02/2025

@author: TJ from Philanoe Consulting

Objective: create a simple websocket server aming to send information to tableau_de_bord.html

Launch me with : python main.py

Tutorial : 
- https://websockets.readthedocs.io/en/stable/index.html
- https://www.bilibili.com/video/BV1Rb4y1X7vw/?vd_source=f33f8677b3006d3f2ee60860f392b7ff
"""

#!/usr/bin/env python

"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve
from time import sleep

async def echo_Once(websocket):
    print("echo_once")
    for message in ["1=50","2=69","4=1112"]:
        print("send one message : ",message)
        await websocket.send(message)
        sleep(1)

async def echo_All_Messages(websocket):
    print("echo_all_messages")
    async for message in websocket:
        print("send one message : ",message)
        await websocket.send(message)
    
async def main():
    print("main")
    async with serve(echo_Once, "localhost", 8765) as server:
        print("start serve forever")
        await server.serve_forever()

if __name__ == "__main__":
    print("start the program")
    asyncio.run(main())