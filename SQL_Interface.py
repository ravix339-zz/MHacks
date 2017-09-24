import pyodbc
import glob
import Sentiment as GS
import numpy as np

connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

prev_file_name = ""
score_list = []
mag_list = []

def Execute(query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.commit()
def LyndonShiAbandonedUs():
    files = glob.glob("D:\\Code\\Python\\Text\\*.txt")
    for fileName in files:
        print(fileName)
        articles =[]
        with open(fileName,'r', encoding='utf-8', errors='ignore') as fileRead:
            try:
                articles = fileRead.read().split('\r\n\r\n\r\n\r\n\r\n')
            except Exception as e:
                print(e)
        for article in articles:
            global prev_file_name, score_list, mag_list
            sentScore= GS.getSentiment(text= article[1:-1])
            score_list.append(float(sentScore[0]))
            mag_list.append(float(sentScore[1]))
            if fileName[:11] != prev_file_name:
                cursor = connection.cursor()
                cursor.execute("UPDATE AnalyzedData SET Score = {score}, Mag = {mag} WHERE startdate = {startdate}".format(
                    startdate="".join(fileName.split('\\')[-1][:11].split('-')), score=np.mean(score_list), mag=np.mean(mag_list)))
                cursor.commit()
                score_list = []
                mag_list = []
            prev_file_name = fileName[:11]

LyndonShiAbandonedUs()

#
# def SentimentalitySendAndReceive():
#    Aylien.resetTimer()
#    while Aylien.hasNext():
#        for text in Aylien.getNextWeek():
#            sentScore = GS.getSentiment(text=text[1])
#            cursor = connection.cursor()
#            cursor.execute("UPDATE AnalyzedData SET Sent = Sent + {sent}, numRecords = numRecords + 1, AvgSent = Sent / numRecords, Score = {score}, Mag = {mag} WHERE startdate = {startdate}".format(
#                sent=sentScore[0]*sentScore[1],startdate=text[0], score=sentScore[0], mag=sentScore[1]))
#            cursor.commit()
#    cursor = connection.cursor()
#    cursor.execute("DELETE * FROM AnalyzedData WHERE Sent=NULL")
#    cursor.commit()

def MLTrainingSend():
    cursor = connection.cursor()
    cursor.execute("SELECT [Sent],[Delta] FROM AnalyzedData")
    row = cursor.fetchone()
    while row:
#        CloudTrain.TrainData(row[0], row[1])
        row = cursor.fetchone()
#connection.close()