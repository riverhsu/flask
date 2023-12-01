from flask import Flask,render_template

#目的
#	測試使用 3rd web templates 檔案

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("base.html")


if __name__ == ('__main__'):
	hosts = ["192.168.209.128"]
	app.run(hosts[0], port = 5000,debug=True)