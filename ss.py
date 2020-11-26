import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-GE0IH3H;'
                      'Database=BDD;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute("select * from  Bibliotheque")
for row in cursor:
    print(row)
cursor.execute("insert into Bibliotheque values ('7','11 AVENUE JACQUE','0665432')")
conn.commit()
    
