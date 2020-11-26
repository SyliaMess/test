import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BPRTOOF\SQLEXPRESS;'
                      'Database=Gestion_de_personnel;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute("select * from Module;")
for row in cursor:
    print(row)
    
cursor.execute("INSERT INTO Module VALUES (('deeplearning'),('3'),('2'),('1'));")
conn.commit()