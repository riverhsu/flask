from flask import Flask, make_response, Response,request,g,url_for, jsonify
import requests

app = Flask(__name__)

# 靜態路由, root
@app.route("/")
def index():
	return "Hello World"

# endpoint 
@app.route("/index", endpoint="home")
def home():
	status = 200
	return make_response(str(status))

#動態路由
@app.route("/status/<int:pstatus>",endpoint="makestaus")
def defstatus(pstatus):
	resp = Response("this is an user defined status", status=200)
	return resp

#動態路由
@app.route('/getdparam')
def getdparam():
	name = request.args.get("name")  # 使用 args.get() 方法來獲取 URL 參數
	return f"Welcome {name}"  # 使用正確的字符串格式化方式

# send payload
@app.route('/getpayload', methods=["GET","POST"])
def getpayload():
	jsondata = request.get_json()
	return jsonify(jsondata)

# request object
@app.route("/askurl")
def askurl():
	return request.url

# request object / http paramters : user_agent
@app.route("/askagent")
def askagent():
	return request.user_agent.string

# request object / headers : dict{}
@app.route("/askheaders")
def askheaders():
	return list(request.headers.items())

# request object / headers : get key
@app.route("/askhosts")
def askhosts():
	return request.headers.get("host","")

# request object / headers : content_type 
@app.route("/askcontent")
def askcontent():
	return request.headers.get("content_type","None")

@app.route("/askg")
def askg():
	g.test = "adsf2"
	return g.test

if __name__ == "__main__":
	hosts=["192.168.209.128"]
	app.run(hosts[0], port="5000",debug=True)