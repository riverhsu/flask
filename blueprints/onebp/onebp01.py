from flask import Flask
from views.bpview import bpview

app = Flask(__name__)

app.register_blueprint(bpview)

if __name__ == "__main__":
	host = ["192.168.209.128",]
	app.run(host[0], port=5000,debug=True)