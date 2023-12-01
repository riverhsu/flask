from flask import render_template, Blueprint


bpview = Blueprint("bpview", __name__)

@bpview.route("/auth")
def authhome():
	return render_template("auth/authhome.html")

@bpview.route("/auth/login")
def authlogin():
	return render_template("auth/login.html")