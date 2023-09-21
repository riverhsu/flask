from flask import render_template, Blueprint


bpview = Blueprint("bpview", __name__)

@bpview.route("/")
def dphome():
	return "Welcome to Blueprint Demo"

@bpview.route("/login")
def dploing():
	return render_template("auth/login.html")