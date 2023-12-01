from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

bs = Bootstrap4(app)
app.config['BOOTSTRAP_VERSION'] = 5

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/alert_demo")
def alertbox():
	return render_template("alertbox.html")

@app.route("/form_demo")
def formdemo():
	return render_template("formdemo.html")

if __name__ == "__main__":
	host = ["192.168.209.128",]
	app.run(host[0], port=5000,debug=True)