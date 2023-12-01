import cryptography
import pymysql

# 資料庫連接
connection = pymysql.connect(host="localhost", user="river", password="zaq1xsw2", db = "stockdb")

# 獲取結果集 cursor
cursor = connection.cursor()

# query
stmt = "select * from region limit 10"
cursor.execute(stmt)

# 使用 fetchone() 逐行獲取結果
res = cursor.fetchall()

for item in res:
	print(item[0], item[1], item[2])

# close connection
cursor.close()
connection.close()
