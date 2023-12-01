#coding: utf-8
#目的:
#	測試 flask request 物件的 path 屬性

from flask import Flask, request

app = Flask(__name__)


# demo
# http://192.168.11.115:5000/ask?func=path

@app.route('/ask')
def showReq():
	

	path = {'path':request.path}
	full_path = {'full_path':request.full_path}
	script_root ={'script_root': request.script_root}
	base_url = 	{'base_url':request.base_url}
	url = {'url':request.url}
	url_root = {'url_root':request.url_root}
	stmt = [path, full_path, script_root, base_url, url, url_root]
	return stmt


if __name__ == ('__main__'):
	hosts = ["192.168.209.128"]
	app.run(hosts[0], port = 5000,debug=True)
