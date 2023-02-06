import time
import serial as sr
import sqlite3 as sl


db_path = 'PyQt/python_scripts/handler/BED.db'


print("Reading soon")
baudrate = 9600
port = "COM7"

portSerial = sr.Serial(port=port, baudrate=baudrate)

if portSerial.is_open:
    time.sleep(5)
    size = portSerial.inWaiting()
    if size:
        data = portSerial.read(size)
        print(data)
else:
    print('serial not open')


data = data.decode("utf-8").strip()
insert_list = data.split("\r\n")
Time = insert_list[0]
StudyID = int(insert_list[1])
Steps = int(insert_list[2])
HeartRate = int(insert_list[3])
ParticipantID = int(insert_list[4])
ActivityTimeMins = int(insert_list[5])
ActivityType = insert_list[6]
PromptGenerated = insert_list[7]
InPain = insert_list[8]
PainLevel = int(insert_list[9])

try:
    con = sl.connect(db_path)
    cursor = con.cursor()
    # Insert values into Records table in Database
    insert_query = """ INSERT INTO DATAVIEW (Time, StudyID, Steps, HeartRate, ParticipantID,
    ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel) VALUES 
    (?,?,?,?,?,?,?,?,?,?)"""

    record = (Time, StudyID, Steps, HeartRate, ParticipantID,
    ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel)

    cursor.execute(insert_query, record)
    con.commit()
    cursor.close()
    con.close()

except con.Error as error:
        print("Failed to insert into MySQL table {}".format(error))