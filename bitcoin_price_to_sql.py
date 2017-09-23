import pyodbc
import json

data_file = 'data/bitcoin_weekly_data.json'

server = 'tcp:mhacks.database.windows.net'
database = 'MHacks'
username = 'ajaykumar'
password = 'ILoveAjay!!!'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()
cursor.execute("CREATE TABLE Bitcoin_Price_Data ( Interval INTEGER, FinalPrice REAL, Delta REAL )")
cursor.commit()
with open(data_file) as json_data:
    json_data = json.load(json_data)

for week_num in json_data:
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO Bitcoin_Price_Data VALUES({interval},{finalprice},{delta})".format(
        interval=int(week_num),finalprice=json_data[week_num]['Final Price'],
        delta=json_data[week_num]['Delta Price']))
    cursor.commit()
