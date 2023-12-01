# 目的
# 	使用 app.test_request_context() 作測試
# 	讀取 request, response 的回傳值


from flask import Flask, request
from wtforms import StringField

app = Flask(__name__)


@app.route('/')
def index():
	return 'test_request_context testing'

# 在沒有啟動 flask 下, 也可以檢測 web 物件資料
# 可以在 python CLI 中,直接執行
with app.test_request_context():
	print (request.headers)

with app.test_request_context():
	g.name = "river"
	print(g.name)
