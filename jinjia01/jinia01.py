from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/page1/<name>")
def page1(name):
	return render_template("page1.html", name = name)

@app.route("/page2/<name>/<age>")
def page2(name,age):
	data = {"name":name, "age":age}
	return render_template("page2.html", data = data)

if __name__ == "__main__":
	host = ["192.168.209.128",]
	app.run(host[0], port=5000,debug=True)