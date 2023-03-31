import bluetooth
import struct
loop_time = 10
ser = ""
s = struct.Struct('<' + str(10) + 'f')
SAMPLES = 30000
bd_addr = "d4:d4:da:1d:de:a6" 
port = 1
try:
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    print('Connected')
except Exception as e:
    print (e)
 
sock.send("Hello World")
print('Sent data')
