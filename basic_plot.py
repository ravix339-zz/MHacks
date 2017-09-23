import pyodbc
import matplotlib.pyplot as plt
import numpy as np
import datetime

cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

print('Change AnalyzedData.FinalPrice to AnalyzedData.Sent')
exit(1)
cursor.execute("SELECT AnalyzedData.Interval, AnalyzedData.Delta, AnalyzedData.FinalPrice FROM AnalyzedData")
raw_data = cursor.fetchall()

fig, ax = plt.subplots()
weeks = []
deltas = []
sentiments = []
for datum in raw_data:
    print(datum)
    weeks.append(datum[0])
    deltas.append(datum[1])
    sentiments.append(datum[2])

y_pos = np.arange(len(weeks))

plt.scatter(y_pos, deltas)
plt.scatter(y_pos, sentiments)
plt.xticks(y_pos, weeks, fontsize=6)
plt.ylabel('Change in BTC Value')
plt.title('Change in BTC Value and Average Sentiment vs Time', fontsize=10)

plt.ion()
plt.show()

fig, ax = plt.subplots()
y_pos = np.arange(len(sentiments))

plt.scatter(y_pos, deltas)
plt.xticks(y_pos, sentiments, fontsize=6)
plt.ylabel('Change in BTC Value')
plt.xlabel('Sentiment')
plt.title('Change in BTC Value vs Recent Article Sentiment', fontsize=10)

plt.show()

input('Press Enter to close')
