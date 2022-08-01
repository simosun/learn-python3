

import pyodbc 

server = '10.71.254.203' # 数据库地址
# 其他设置server的方法
# server = 'localhost\sqlexpress' # 实例名
# server = 'myserver,port' # 指定端口
database = 'qdtzlf' # 数据库名
username = 'simon' # 用户名
password = 'simon563' # 密码
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print (row[0])
    row = cursor.fetchone()