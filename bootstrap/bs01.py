from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

bs = Bootstrap4(app)

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == "__main__":
	host = ["192.168.209.128",]
	app.run(host[0], port=5000,debug=True)