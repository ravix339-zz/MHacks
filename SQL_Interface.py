import pyodbc
import glob
import Sentiment as GS

connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
def Execute(query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.commit()
def LyndonShiAbandonedUs():
    files = glob.glob("C:\\Users\\Ravi\\Desktop\\text\\*.txt")
    for fileName in files:
        stuff = ["Bitcoin is amazing!!!! I love it!"]
        print(fileName)
        with open(fileName,'r') as fileRead:
            try:
                something = fileRead.readline()
                stuff.append(something)
            except:
                print("Fuck you")
            while something:
                try:
                    something = fileRead.readline()
                    stuff.append(something)
                except Exception as e:
                    print("Fuck you")
        sentScore= GS.getSentiment(text=" ".join(stuff))
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