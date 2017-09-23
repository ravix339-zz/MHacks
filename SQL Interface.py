import pyodbc
connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=MHacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!!!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
#cursor = connection.cursor()
#cursor.execute("CREATE TABLE TestTable (Hello int)")
#cursor.commit()
cursor = connection.cursor()
#cursor.execute("INSERT INTO TestTable VALUES(6)")
#cursor.commit()
cursor = connection.cursor()
cursor.execute("SELECT * FROM TestTable")
row = cursor.fetchone()
while row:
    print (str(row[0]))
    row = cursor.fetchone()