import time
import serial as sr
import sqlite3 as sl



db_path = 'PyQt/python_scripts/handler/BED.db'


print("Reading soon")
baudrate = 115200
port = "COM4"

portSerial = sr.Serial(port=port, baudrate=baudrate)
data = ""
if portSerial.is_open:
    time.sleep(5)
    size = portSerial.inWaiting()
    if size:
        data = portSerial.read(size)
        print(data)
else:
    print('serial not open')
