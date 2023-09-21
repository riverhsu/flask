from flask import Flask,render_template
from views.bpview import bpview
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

bp4 = Bootstrap4(app)

app.register_blueprint(bpview)

@app.route("/")
def bphome():
	return render_template("index.html")

if __name__ == "__main__":
	host = ["192.168.209.128",]
	app.run(host[0], port=5000,debug=True)