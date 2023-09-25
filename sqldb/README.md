要先安裝 cryptography 庫
	安全連線機制

使用 Python 操作 mysql 資料庫的作法
	DBAPI(資料庫API)
		是Python中與資料庫進行交互的標準介面,不同的資料庫通常有相應的DBAPI驅動程式
		mysql-connector-python
			這是官方提供的MySQL資料庫連接器,支援MySQL的各種功能
			安裝
				pip install mysql-connector-python
		MySQLdb
			這是一個老牌的MySQL資料庫介面,也被稱為MySQL-Python
			它在較早的Python版本中廣泛使用,但不支持Python 3.x
			安裝(Python 2.x)
				pip install MySQL-python
		PyMySQL
			這是一個純Python編寫的MySQL資料庫介面,相容Python 2.x和3.x
			安裝
				pip install pymysql
		mysqlclient
			這是MySQL資料庫的C語言封裝庫的Python綁定,與MySQLdb類似,但在某些情況下更快
			安裝
				pip install mysqlclient
		SQLAlchemy
			SQLAlchemy不僅提供了SQL運算式語言(SQL Expression Language),還提供了ORM(物件關係映射)功能
			它可以與多個資料庫後端(包括MySQL)一起使用
			安裝
				pip install sqlalchemy
		aiomysql
			這是一個非同步的MySQL資料庫介面,適用於非同步Python框架(如Tornado、asyncio等)
			安裝
				pip install aiomysql

	使用 SQLAlchemy 連接
		要使用 SQLAlchemy 連接到 MySQL 資料庫,你需要選擇一個 MySQL DBAPI 驅動程式
		並使用 SQLAlchemy 創建一個資料庫引擎
		示例
			確保已安裝 SQLAlchemy
				pip install sqlalchemy
			MySQL DBAPI 驅動程式選擇
				創建 SQLAlchemy 引擎並連接到 MySQL 資料庫
					from sqlalchemy import create_engine
				mysql-connector-python
					pip install sqlalchemy mysql-connector-python
					作法
				mysqlclient
					這是一個純 Python 驅動程式,也是 MySQL-Python 的替代品
					安裝
						pip install mysqlclient
					使用方式
						與 mysql-connector-python 類似
				PyMySQL
					PyMySQL 是一個純 Python 驅動程式,它是 MySQL 官方推薦的替代 MySQL-Python 的驅動程式之一
					安裝
						pip install pymysql
					使用方式
						與 mysql-connector-python 類似
				SQLAlchemy
					SQLAlchemy 是一個強大的 ORM 工具,它支援多個資料庫後端,包括 MySQL
					可以使用 SQLAlchemy 創建資料庫引擎,並使用適當的 DBAPI 驅動程式來連接到 MySQL
					from sqlalchemy import create_engine
					使用 mysql-connector-python 作為 SQLAlchemy 的後端
						db_uri = "mysql+mysqlconnector://username:password@localhost:3306/database"
					使用 pymysql 作為 SQLAlchemy 的後端
						db_uri = "mysql+pymysql://username:password@localhost:3306/database"
					engine = create_engine(db_uri)

