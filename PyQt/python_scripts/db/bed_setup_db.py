from server_db import *
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE BED")
# mycursor.execute("SHOW DATABASES")

create_table_records_query = "CREATE TABLE Records (FirstName VARCHAR(25) NOT NULL,\
  LastName VARCHAR(25) NOT NULL,\
  Age int NOT NULL, \
  ParticipantID int PRIMARY KEY NOT NULL,\
  StudyID int NOT NULL, \
  Gender VARCHAR(25),\
  Weight float,\
  Height float,\
  PhoneNumber VARCHAR(20),\
  EmailID VARCHAR(25),\
  Address VARCHAR(255),\
  MonitoringPeriod int NOT NULL,\
  TrackerModel VARCHAR(50) NOT NULL)"



create_table_data_query = "CREATE TABLE DataView (Time VARCHAR(50) NOT NULL,\
  StudyID int,\
  Steps int NOT NULL,\
  HeartRate int NOT NULL, \
  ParticipantID int,\
  ActivityTimeMins int NOT NULL,\
  ActivityType VARCHAR(25),\
  PromptGenerated VARCHAR(20),\
  InPain VARCHAR(20),\
  PainLevel int)"

# mycursor.execute(create_table_records_query)
# mycursor.execute(create_table_data_query)