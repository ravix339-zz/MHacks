import pyodbc
import json
import datetime

data_file = 'data/bitcoin_weekly_data.json'

server = 'tcp:mhacks.database.windows.net'
database = 'MHacks'
username = 'ajaykumar'
password = 'ILoveAjay!!!'
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
#cursor = cnxn.cursor()
#cursor.execute("DROP TABLE AnalyzedData")
#cursor.commit()
#cursor = cnxn.cursor()
#cursor.execute("CREATE TABLE AnalyzedData ( Interval char(10), Sent REAL, NumRecords INT, AVGSent Real, FinalPrice REAL, Delta REAL, Score REAL, Mag REAL )")
#cursor.commit()
with open(data_file) as json_data:
    json_data = json.load(json_data)

for week_num in json_data:
    dt = str(datetime.datetime(int(week_num[:4]), int(week_num[5:7]), int(week_num[8:10])).date());
    print("".join(dt.split('-')))
    cursor = cnxn.cursor()
    cursor.execute("UPDATE AnalyzedData SET FinalPrice={finalprice}, Delta={delta} WHERE startdate={interval}".format(
        interval="".join(dt.split('-')),finalprice=json_data[week_num]['Final Price'],
        delta=json_data[week_num]['Delta Price']))
    cursor.commit()
