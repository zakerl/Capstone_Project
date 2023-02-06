from server_db import *
import pandas as pd

mycursor = mydb.cursor()

sql_query = pd.read_sql('SELECT * FROM DATAVIEW', mydb)

# Convert SQL to DataFrame
df_data = pd.DataFrame(sql_query, columns = ['Time', 'StudyID', 'Steps', 'HeartRate', 'ParticipantID', 'ActivityTimeMins', 'ActivityType', 'PromptGenerated', 'InPain', 'PainLevel'])

print(df_data)