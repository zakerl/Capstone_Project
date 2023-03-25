import bluetooth
import time
 
# devices = bluetooth.discover_devices(lookup_names=True)
# print(type(devices))
 
# print("Devices found: %s" % len(devices))
 
# for item in devices:
#     print(item)

import struct
loop_time = 10
ser = ""
s = struct.Struct('<' + str(10) + 'f')
SAMPLES = 30000
bd_addr = "cc:db:a7:16:2e:ae" 
port = 1
try:
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    print('Connected')
except Exception as e:
    print (e)
#sock.settimeout(1.0)
 
sock.send("r")
print('Sent data')
data = ""

start_time = time.time()
start_end_bit = []
while True:
    rec_data = sock.recv(1024)
    if len(rec_data) == 0: break
    # print("received [%s]" % rec_data)
    rec_data = rec_data.decode("utf-8").strip()
    print (rec_data)
    if (rec_data != '0'):
        data += rec_data
    else:
        start_end_bit.append(rec_data)
    end_time = time.time()
    if (end_time - start_time > loop_time or len(start_end_bit) >= 2): # Run for t seconds
        break
print ("===================")
print (data)