import pyodbc

cnxn = pyodbc.connect('Server=tcp:mhacks.database.windows.net,1433;Initial Catalog=MHacks;Persist Security Info=False;User ID=ajaykumar;Password=ILoveAjay!!!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;')
cursor = cnxn.cursor()
