from flask import Flask

app = Flask("__main__")

@app.route("/")
def home():
	return "Welcome to Flask"

@ap.route("/name")
def user(name)
	return "Welcome to Flask",name

if __name__ == "__main__":
	hosts = ["192.168.209.128"]
	app.run(hosts[0],debug=True)