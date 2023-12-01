# coding: utf-8

# 目的:
# 測試 session 的基本功能
# 將 username 存入 session , 並在另一個 endpoint 顯示

from flask import Flask, session
from datetime import timedelta
import os

# configuration
app = Flask('__name__')
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)


# set session
@app.route('/')
def index():

	#設置session
	session['username'] = 'river'
	#如果设置了session的permanent属性为True，那么过期时间是31天
	session.permanent = True

	#讀取session
	session.get('username')

	#刪除session
	#session['username'] = False

	return 'Hellow Session World'

@app.route('/session')
def getsess():
	return 'Welcome , %s' % session.get('username')

@app.route('/set')
def setuname():
	#設置session
	session['username'] = 'Vicki'
	#如果设置了session的permanent属性为True，那么过期时间是31天
	session.permanent = True

	#讀取session
	#session.get('username')
	return 'setting OK'


if __name__ == "__main__":
	app.run(host='192.168.11.115', port=5000, debug=True)
