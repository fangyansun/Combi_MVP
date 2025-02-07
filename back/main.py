# #!/usr/bin/python

"""
Created on: 06/02/2025

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
import serial
import time

# Global variables and constants

BAUDRATE = 9600
TIMEOUT = 5
USB_PORT = 'COM6'# "/dev/ttyACMO"
INIT_DELAY = 2

def serial_Communication_Init():
    print("Initialisation en cours")
    try:
        arduino_com = serial.Serial(USB_PORT,BAUDRATE,timeout=TIMEOUT)
        # wait a few seconds, otherwise, the first commands are not taken into account
        time.sleep(INIT_DELAY)
        print("connexion établie !")
        return True, arduino_com

    except Exception as error:
        print("Erreur lors de l'initialisation de la communication avec Arduino : ", error)
        return False, None

async def websocket_Handler(websocket):
    print("websocket_Handler")
    success, arduino_com = serial_Communication_Init()
    if success:
        try:
            while True:
                data=arduino_com.readline().decode('utf-8').strip()
                if data:
                    print("recu : ",data)
                    print("we will send it to the front end")
                    await websocket.send(data)
                    await asyncio.sleep(0.1) # the program does not work without this line
                else:
                    print("we received empty data")
        except Exception as error:
            print("Erreur lors de la lecture des données venant d'Arduino", error)        

async def start_Websocket():
    # https://websockets.readthedocs.io/en/stable/intro/tutorial1.html#download-the-starter-kit
    async with serve(websocket_Handler, "localhost", 8765):
        print("start websocket server")
        await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    print("start the program")
    asyncio.run(start_Websocket())

    