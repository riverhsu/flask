from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def vuejs():
	return render_template("index.html")


if __name__ == "__main__":
	host = ["192.168.209.128",]
	app.run(host[0], port=5000,debug=True)
