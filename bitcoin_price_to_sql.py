import pyodbc
import json

data_file = 'data/bitcoin_weekly_data.json'

server = 'tcp:mhacks.database.windows.net'
database = 'MHacks'
username = 'ajaykumar'
password = 'ILoveAjay!!!'
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()
cursor.execute("DROP TABLE AnalyzedData")
cursor = cnxn.cursor()
cursor.execute("CREATE TABLE AnalyzedData ( Interval int, Sent REAL, NumRecords INT, AVGSent Real, FinalPrice REAL, Delta REAL )")
cursor.commit()
with open(data_file) as json_data:
    json_data = json.load(json_data)

for week_num in json_data:
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO AnalyzedData(Interval, FinalPrice, Delta) VALUES({interval},{finalprice},{delta})".format(
        interval=int(week_num),finalprice=json_data[week_num]['Final Price'],
        delta=json_data[week_num]['Delta Price']))
    cursor.commit()
