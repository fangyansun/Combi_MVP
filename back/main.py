# #!/usr/bin/python

"""
Created on: 06/02/2025

Objective: create a simple websocket server aming to send information to tableau_de_bord.html

Launch me with : python main.py

Tutorial : 
- https://websockets.readthedocs.io/en/stable/index.html
- https://www.bilibili.com/video/BV1Rb4y1X7vw/?vd_source=f33f8677b3006d3f2ee60860f392b7ff
"""

"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve
import serial
import time

# Global variables and constants
USB_PORT = "/dev/ttyACM0"
# USB_PORT = "COM6"
BAUDRATE = 9600
ARDUINO_CONNEXION_TIMEOUT = 5
WEBSOCKET_RETRY_PERIOD = 5
DATA_RECORDING_PERIOD = 20 # in seconds
LOG_PATH = "log/log.csv" # in a future version, we might have a different log name for each period of time

global_data_dict = {}
last_time = 0
arduino_serial_communication_chanel = None

def debug_Print(message):
    print("-- ",message)

async def stop_With_Delay():
    debug_Print(f'Fin du websocket handler actuel programmée dans {WEBSOCKET_RETRY_PERIOD} secondes')
    await asyncio.sleep(WEBSOCKET_RETRY_PERIOD)

async def websocket_Handler(websocket):
    debug_Print(f'*********** New websocket_Handler *************')
    try:
        debug_Print("Voyons si la connexion à Arduino est présente")
        global arduino_serial_communication_chanel
        if not arduino_serial_communication_chanel:
            debug_Print("Aucune connexion avec Arduino n'a été détectée, donc nous en créant une nouvelle")
            try:
                arduino_serial_communication_chanel = serial.Serial(USB_PORT,BAUDRATE,timeout=ARDUINO_CONNEXION_TIMEOUT)
                debug_Print("Nouvelle connexion à Arduino réussie !") 
            except Exception as error:
                arduino_serial_communication_chanel = None
                debug_Print(f'Arduino Communication failed : {error}')
                await stop_With_Delay()
                return 0
        else:
            debug_Print(f'Une connexion à Arduino a été détectée : {arduino_serial_communication_chanel}')
        debug_Print("On commence à écouter le port série et à retransmettre les données ")
        while True:
            data=arduino_serial_communication_chanel.readline().decode('utf-8').strip()
            debug_Print(f'Donnée reçue : {data}')
            # step 1 : record the data in a global_data_dict
            key, value = data.split("=")
            try:
                global_data_dict[key] = value
            except Exception as error:
                debug_Print(f'global_data_dict[key] = value error with this key : {key} and that error : {error}')
                await stop_With_Delay()
                return
            
            # step 2 : send the data to the frond end through websocket
            await websocket.send(data)
            await asyncio.sleep(0.1) # the program does not work without this line

            # step 3 : if we waited long enough, we make one record on the local database
            current_time = time.perf_counter()
            global last_time
            if (current_time - last_time > DATA_RECORDING_PERIOD):
                record_Current_Data_Into_Local_Log_File()
                last_time = current_time
        
    except Exception as error:
        debug_Print(f'Erreur non prévue : {error}')
        try:
            arduino_serial_communication_chanel.close()
        finally:
            arduino_serial_communication_chanel = None
    finally:
        await stop_With_Delay()        

async def start_Websocket():
    # https://websockets.readthedocs.io/en/stable/intro/tutorial1.html#download-the-starter-kit
    async with serve(websocket_Handler, "192.168.31.18", 8765):
        debug_Print("Start websocket asyncio loop")
        await asyncio.get_running_loop().create_future()

def record_Current_Data_Into_Local_Log_File():
    debug_Print(global_data_dict)
    csv_string = ""
    for value in global_data_dict.values():
        csv_string = csv_string + value + ";"
    try:
        file = open(LOG_PATH, "a")
        file.write(csv_string)
        file.write("\n")
        file.close
    except Exception as error:
        debug_Print("Erreur durant l'écriture du log dans un fichier local", error)

if __name__ == "__main__":
    debug_Print("Début du programme")
    asyncio.run(start_Websocket())