from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
	return "Welcome to Flask"

@app.route("/user/<name>", methods=["GET", "POST"])
def user(name):
	if request.method == "GET":
		return f"Welcome to Flask, {name}"
	elif request.method == "POST":
		# Handle POST request data here if needed
		return f"Hello, {name} (POST request received)"

	return "Welcome to Flask",name

if __name__ == "__main__":
	hosts = ["192.168.209.128"]
	app.run(hosts[0],debug=True)