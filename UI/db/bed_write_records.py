import sqlite3 as sl

con = sl.connect('PyQt/python_scripts/db/BED.db')

insert_query = "INSERT INTO Records (FirstName, LastName, Age, ParticipantID, StudyID, Gender, Weight, Height, PhoneNumber,\
EmailID, Address, MonitoringPeriod, TrackerModel) VALUES ('Rose','Lindt',65,2,32,'Female',63,150,'(864) 315-3964','rose@gmail.com','Mundelein, IL 60060',12,'dhi2')"

insert_query = "INSERT INTO Records (FirstName, LastName, Age, ParticipantID, StudyID, Gender, Weight, Height, PhoneNumber,\
EmailID, Address, MonitoringPeriod, TrackerModel) VALUES ('Ashley','Dunder',63,3,32,'Female',57,160,'(238) 233-4530','ashley@gmail.com','9022 Jennings Drive',15,'Ah19')"


with con:
    con.execute(insert_query)
