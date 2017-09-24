import pyodbc
import glob
import Sentiment as GS

connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
def Execute(query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.commit()
def LyndonShiAbandonedUs():
    files = glob.glob("D:\\Code\\Python\\Text\\*.txt")
    for fileName in files:
        print(fileName)
        articles =[]
        with open(fileName,'r', encoding='utf-8') as fileRead:
            try:
                articles = fileRead.read().split('\r\n\r\n\r\n\r\n\r\n')
            except Exception as e:
                print(e)
                print("Fuck you")
        for article in articles:
            sentScore= GS.getSentiment(text=article)
            cursor = connection.cursor()
            cursor.execute("UPDATE AnalyzedData SET Score = {score}, Mag = {mag} WHERE startdate = {startdate}".format(
                startdate="".join(fileName.split('\\')[-1][:-4].split('-')), score=sentScore[0], mag=sentScore[1]))
            cursor.commit()

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