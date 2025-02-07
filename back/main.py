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
import threading
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
        return False, _

async def echo_Once(websocket):
    print("echo_once")
    for message in ["1=50","2=69","4=1112"]:
        print("send one message : ",message)
        await websocket.send(message)
        await asyncio.sleep(1)

async def start_websocket():
    async with serve(echo_Once, "localhost", 8765) as server:
        print("start websocket server")
        await server.serve_forever()

def websocket():
    asyncio.run(start_websocket())

if __name__ == "__main__":
    print("start the program")
    success, arduino_com = serial_Communication_Init()
    if success:
        # launch the websocket server in another thread
        thread = threading.Thread(target=websocket)
        thread.start()
        # in the same time, start listening to arduino data
        try:            
            while True:
                data=arduino_com.readline().decode('utf-8').strip()
                if data:
                    print("recu : ",data)
                else:
                    print("we received empty data")
        except Exception as error:
            print("Erreur lors de la lecture des données venant d'Arduino", error)        

    