import sqlite3 as sl

con = sl.connect('PyQt/python_scripts/db/BED.db')

insert_query = "INSERT INTO DataView (Time, StudyID, Steps, HeartRate, ParticipantID, ActivityTimeMins, ActivityType, PromptGenerated) VALUES ('7:22',3,20,69,2,1,'walking','No')"
# insert_query = "INSERT INTO DataView (Time, StudyID, Steps, HeartRate, ParticipantID, ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel) VALUES ('9:20',3,50,100,2,6,'walking','Yes','Yes',2)"
# insert_query = "INSERT INTO DataView (Time, StudyID, Steps, HeartRate, ParticipantID, ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel) VALUES ('11:18',3,30,85,2,5,'Movement detected','Yes','Yes',4)"

with con:
    con.execute(insert_query)
