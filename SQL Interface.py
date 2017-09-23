import pyodbc
import Sentiment
import Aylien
import CloudTrain

connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
def createWeeklyURLTable():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE WeeklyUrls (StartDate nvarchar(255), URL nvarchar(MAX))")
    cursor.commit()

def Insert(startDate, URL):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO WeeklyUrls VALUES(startDate, URL)")
    cursor.commit()

def SentimentalitySendAndReceive():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM WeeklyUrls")
    row = cursor.fetchone()
    while row:
        sentScore = Sentiment.getSentiment(url=row[1]) #figure out the magnitude and scalar stuff
        cursor2 = connection.cursor()
        cursor2.execute("UPDATE AnalyzedData SET Sent = Sent + {sent}, numRecords = numRecords + 1, AvgSent = Sent / numRecords, Score = {score}, Mag = {mag} WHERE startdate = {startdate}".format(
            sent=sentScore[0]*sentScore[1], startdate=row[0], score=sentScore[0], mag=sentScore[1]))
        cursor2.commit()
        row = cursor.fetchone()
    Aylien.resetTimer()
    while Aylien.hasNext():
        for text in Aylien.getNextWeek():
            sentScore = Sentiment.getSentiment(text=text[1])
            cursor = connection.cursor()
            cursor.execute("UPDATE AnalyzedData SET Sent = Sent + {sent}, numRecords = numRecords + 1, AvgSent = Sent / numRecords, Score = {score}, Mag = {mag} WHERE startdate = {startdate}".format(
                sent=sentScore[0]*sentScore[1],startdate=text[0], score=sentScore[0], mag=sentScore[1]))
            cursor.commit()

def MLTrainingSend():
    cursor = connection.cursor()
    cursor.execute("SELECT [Sent],[Delta] FROM AnalyzedData")
    row = cursor.fetchone()
    while row:
#        CloudTrain.TrainData(row[0], row[1])
        row = cursor.fetchone()

SentimentalitySendAndReceive()