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
USB_PORT = "COM6"
BAUDRATE = 9600
ARDUINO_CONNEXION_TIMEOUT = 5
WEBSOCKET_RETRY_PERIOD = 5
DATA_RECORDING_PERIOD = 20 # in seconds
LOG_PATH = "log/log.csv" # in a future version, we might have a different log name for each period of time

global_data_dict = {}
last_time = 0
arduino_serial_communication_chanel = 0

def debug_Print(message):
    print("-- ",message)

async def websocket_Handler(websocket):
    debug_Print(f'*********** New websocket_Handler *************')
    try:
        debug_Print("do something")
    except Exception:
        debug_Print(Exception)
    finally:    
        debug_Print(f'Fin du websocket handler actuel programmée dans {WEBSOCKET_RETRY_PERIOD} secondes')
        await asyncio.sleep(WEBSOCKET_RETRY_PERIOD)
    
    #         while True:
    #             data=arduino_serial_communication_chanel.readline().decode('utf-8').strip()
    #             if data:
    #                 # step 1 : record the data in a global_data_dict
    #                 key, value = data.split("=")
    #                 try:
    #                     global_data_dict[key] = value
    #                     # step 2 : send the data to the frond end through websocket
    #                     try:
    #                         await websocket.send(data)
    #                         await asyncio.sleep(0.1) # the program does not work without this line

    #                         # step 3 : if we waited long enough, we make one record on the local database
    #                         current_time = time.perf_counter()
    #                         if (current_time - last_time > DATA_RECORDING_PERIOD):
    #                             record_Current_Data_Into_Local_Log_File()
    #                             last_time = current_time

    #                     except Exception as error:
    #                         debug_Print(f'websocket.send error : {error}')
    #                         debug_Print("we will break the websocket handler")
    #                         break
    #                 except Exception as error:
    #                     debug_Print(f'global_data_dict[key] = value error with this key : {key} and that error : {error}')
    #             else:
    #                 debug_Print("we received empty data")
    #         # end of while True
    #     except Exception as error:
    #         debug_Print("Erreur lors de la lecture des données venant d'Arduino avec arduino_com.readline", error)
    #     finally: 
    #         debug_Print("Fin de la fonction websocket handler, nous fermons la communication avec Arduino")
    #         arduino_serial_communication_chanel.close()

async def start_Websocket():
    # https://websockets.readthedocs.io/en/stable/intro/tutorial1.html#download-the-starter-kit
    async with serve(websocket_Handler, "192.168.137.1", 8765):
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
    


    