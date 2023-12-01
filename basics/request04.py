# coding: utf-8

# 接收來自 req01.py 的請求, 並做回應.

from flask import Flask, request,jsonify


app = Flask(__name__)

@app.route('/')
def index():
	return ('welcome flask')

@app.route('/ask', methods=['GET', 'POST'])
def ask():
	stmt = 'Welcome to Flask, '
	if request.method == 'GET':
		name = request.args.to_dict()
		#name = str(request.args.to_dict())
		#datatype = str(type(request.args.to_dict()))

	else:
		name = request.form.to_dict()
		#name = str(request.form.to_dict())
		#datatype = str(type(request.form.to_dict()))

	# work return text/html
	#return stmt + str(name)

	# work , return application/json
	return jsonify(name)

if __name__ == '__main__':
	app.run(host='192.168.11.116', port = 5000, debug = True)	
