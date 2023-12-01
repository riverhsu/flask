# 目的
# 	讀取 request, response 的回傳值


from flask import Flask, request, make_response
from wtforms import StringField

app = Flask(__name__)

@app.route('/')
def index():
	resp = make_response(request.endpoint)
	return resp

@app.route('/name')
def show():
	resp = make_response(request.host)
	return resp

@app.route('/link')
def ref():
	resp = make_response(request.host_url)
	return resp

if __name__ == '__main__':
	app.run(host='192.168.11.121', debug=True)
