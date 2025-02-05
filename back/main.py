# #!/usr/bin/python

# # Launch me with : python main.py

# # https://pypi.org/project/websockets/
 
# # import serial
# import asyncio
# import websockets
 
# # serial_connection = serial.Serial(
# #     port='/dev/ttyUSB0',\
# #     baudrate=115200,\
# #     parity=serial.PARITY_NONE,\
# #     stopbits=serial.STOPBITS_ONE,\
# #     bytesize=serial.EIGHTBITS,\
# #     timeout=0)

# async def print_To_Client_Via_Websocket(websocket, path):
#     count = 0
#     while 1 == 1:
#         count += 1
#         await websocket.send(f'temperature_1={count}')

# start_server = websockets.serve(print_To_Client_Via_Websocket, "127.0.0.1", 5678)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


 
# serial_connection.close()


#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())