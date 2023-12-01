# using mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(host="localhost", user="river", password="zaq1xsw2", db="stockdb")

stmt = "select * from region limit 10"
cursor = connection.cursor()

cursor.execute(stmt)

res = cursor.fetchall()
for item in res:
	print(item[0], item[1],item[2])

cursor.close()
connection.close()

