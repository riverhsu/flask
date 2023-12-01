import pymysql
from sqlalchemy import create_engine, text

dburi = "mysql+pymysql://river:zaq1xsw2@localhost:3306/stockdb?charset=utf8"
engine = create_engine(dburi)

stmt = text("select * from region limit 10")

with engine.connect() as connection:
	res = connection.execute(stmt)


for item in res:
	print(item[0],item[1],item[2])