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
DATA_RECORDING_PERIOD = 20 # in seconds
LOG_PATH = "log/log.csv" # in a future version, we might have a different log name for each period of time

global_data_dict = {}
last_time = 0
arduino_serial_communication_chanel = 0

async def websocket_Handler(websocket):
    print("new websocket_Handler")
    # stop the last websocket handler if any
    try:
        print("essayons d'arrêter la dernière connexion websocket le cas échéant")
        global arduino_serial_communication_chanel
        arduino_serial_communication_chanel.close()
    except Exception as error:
        print(error)
    finally:
        print("Maintenant, nous créons une nouvelle connexion avec Arduino avec la certitude que c'est la seule")
        arduino_serial_communication_chanel = serial.Serial(USB_PORT,BAUDRATE,timeout=ARDUINO_CONNEXION_TIMEOUT)
        # we use global variables because this function could be reset by the client (F5)
        global last_time
        try:
            while True:
                data=arduino_serial_communication_chanel.readline().decode('utf-8').strip()
                if data:
                    # step 1 : record the data in a global_data_dict
                    key, value = data.split("=")
                    try:
                        global_data_dict[key] = value
                        # step 2 : send the data to the frond end through websocket
                        try:
                            await websocket.send(data)
                            await asyncio.sleep(0.1) # the program does not work without this line

                            # step 3 : if we waited long enough, we make one record on the local database
                            current_time = time.perf_counter()
                            if (current_time - last_time > DATA_RECORDING_PERIOD):
                                record_Current_Data_Into_Local_Log_File()
                                last_time = current_time

                        except Exception as error:
                            print(f'websocket.send error : {error}')
                            print("we will break the websocket handler")
                            break
                    except Exception as error:
                        print(f'global_data_dict[key] = value error with this key : {key} and that error : {error}')
                else:
                    print("we received empty data")
            # end of while True
        except Exception as error:
            print("Erreur lors de la lecture des données venant d'Arduino avec arduino_com.readline", error)
        finally: 
            print("Fin de la fonction websocket handler, nous fermons la communication avec Arduino")
            arduino_serial_communication_chanel.close()

async def start_Websocket():
    # https://websockets.readthedocs.io/en/stable/intro/tutorial1.html#download-the-starter-kit
    async with serve(websocket_Handler, "192.168.137.1", 8765):
        print("start websocket server, nous attendons la connexion du front")
        await asyncio.get_running_loop().create_future()

def record_Current_Data_Into_Local_Log_File():
    print(global_data_dict)
    csv_string = ""
    for value in global_data_dict.values():
        csv_string = csv_string + value + ";"
    try:
        file = open(LOG_PATH, "a")
        file.write(csv_string)
        file.write("\n")
        file.close
    except Exception as error:
        print("Erreur durant l'écriture du log dans un fichier local", error)

if __name__ == "__main__":
    print("Début du programme")
    asyncio.run(start_Websocket())
    


    