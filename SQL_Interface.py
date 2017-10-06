import pyodbc
import glob
import Sentiment as GS
import WatsonSentiment as WS
import numpy as np

connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

def Execute(query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.commit()

def LyndonShiAbandonedUs():
    files = glob.glob("D:\\Code\\Python\\Text\\*.txt")
    score_list = []
    prev_file_name = ""
    mag_list=[]
    wDscore_list = []
    for fileName in files:
        print(fileName)
        # if fileName.split('\\')[-1] < "2017-07-18 (3).txt":
        #     continue
        articles =[]
        with open(fileName,'r', encoding='utf-8', errors='ignore') as fileRead:
            try:
                articles = fileRead.read().split('\r\n\r\n\r\n\r\n\r\n')
            except Exception as e:
                print(e)
        for article in articles:
            wsentScore = WS.getSentiment(text= "bitcoin "+article[1:-1])
            wDscore_list.append(float(wsentScore))
            sentScore = GS.getSentiment(text=article[1:-1])
            score_list.append(float(sentScore[0]))
            mag_list.append(float(sentScore[1]))
        if fileName.split('\\')[-1][:11] != prev_file_name:
            cursor = connection.cursor()
            cursor.execute("UPDATE AnalyzedData SET WatsonP2 = {wp2}, ScoreG = {score}, MagG = {mag} WHERE startdate = {startdate}".format(
                startdate="".join(fileName.split('\\')[-1][:11].split('-')), score=np.mean(score_list), mag=np.mean(mag_list), wp2 = np.mean(wDscore_list)))
            cursor.commit()
            cursor.close()
            score_list = []
            mag_list = []
            wDscore_list = []
            prev_file_name = fileName.split('\\')[-1][:11]

LyndonShiAbandonedUs()

# cursor = connection.cursor()
# rows = cursor.execute("SELECT * FROM AnalyzedData WHERE Score != Mag")
# print([row for row in rows])

#.format(
 #                   startdate="".join(fileName.split('\\')[-1][:11].split('-')), score=np.mean(score_list)))
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
