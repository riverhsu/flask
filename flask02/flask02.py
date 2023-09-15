from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def home():
	return "Welcome to Flask"

@app.route("/user/<name>/<age>", methods=["GET"])
def user(name,age):
	if request.method == "GET":
		return render_template("user.html",name = name,age = age)
	
@app.route("/user",methods=["POST"])
def userinfo():
	#username = request.args["name"]
	username = request.json.get("name")
	userage = request.json.get("age")
	return render_template("user.html",name = username, age = userage)

if __name__ == "__main__":
	hosts = ["192.168.209.128"]
	app.run(hosts[0],debug=True)