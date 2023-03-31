import bluetooth
import time
import sqlite3 as sl
# devices = bluetooth.discover_devices(lookup_names=True)
# print(type(devices))
 
# print("Devices found: %s" % len(devices))
 
# for item in devices:
#     print(item)

# db_path = 'pybluez_bluetooth/BED.db'
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
# insert_list = data.split("\n")
# print (insert_list)
# for entry in insert_list:
#     entry_list = entry.split(",")
#     Time = entry_list[0]
#     StudyID = int(entry_list[1])
#     Steps = int(entry_list[2])
#     HeartRate = int(entry_list[3])
#     ParticipantID = int(entry_list[4])
#     ActivityTimeMins = int(entry_list[5])
#     ActivityType = entry_list[6]
#     PromptGenerated = entry_list[7]
#     InPain = entry_list[8]
#     PainLevel = int(entry_list[9])
#     print (Time, StudyID, Steps, HeartRate, ParticipantID, ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel)
#     try:
#         con = sl.connect(db_path)
#         cursor = con.cursor()
#         # Insert values into Records table in Database
#         insert_query = """ INSERT INTO DATAVIEW (Time, StudyID, Steps, HeartRate, ParticipantID,
#         ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel) VALUES 
#         (?,?,?,?,?,?,?,?,?,?)"""

#         record = (Time, StudyID, Steps, HeartRate, ParticipantID,
#         ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel)
#         cursor.execute(insert_query, record)
#         con.commit()
#         cursor.close()
#         con.close()

#     except con.Error as error:
#         print("Failed to insert into MySQL table {}".format(error))