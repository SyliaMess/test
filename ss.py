import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BPRTOOF\SQLEXPRESS;'
                      'Database=WideWorldImporters-Full;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute("select * from Warehouse.StockItems;")
for row in cursor:
    print(row)
    
cursor.execute("INSERT INTO Module VALUES (('Pizza'),('15'),('20'),('10'));")
conn.commit()