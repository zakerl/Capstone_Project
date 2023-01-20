from server_db import *
import pandas as pd

mycursor = mydb.cursor()

sql_query = pd.read_sql('SELECT * FROM RECORDS', mydb)

# Convert SQL to DataFrame
df_records = pd.DataFrame(sql_query, columns = ['FirstName', 'LastName', 'Age', 'ParticipantID', 'StudyID', 'Gender', 'Weight', 'Height', 'PhoneNumber',\
'EmailID', 'Address', 'MonitoringPeriod', 'TrackerModel'])

print(df_records)