import pymssql
conn = pymssql.connect(server='10.71.254.6', user='simon', password='simon563', database='qdtlzf')
cursor = conn.cursor()
cursor.execute('SELECT * from qdtlzf.dbo.userlist ;')
row = cursor.fetchone()
while row: 
 print (row[0])
 row = cursor.fetchone()
