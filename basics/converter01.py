from flask import Flask, request, render_template,current_app,jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/headers")
def headers():
	return list(request.headers)

@app.route("/forms")
def useforms():
	data1 = ["A","B","C"]
	data2 = [{"name": "A", "is_active": True},{"name": "B", "is_active": False},{"name": "C", "is_active": True}]

	data = {"data1":data1, "data2":data2}
	return render_template("form.html", items = data)

@app.route("/submitform1",methods=["POST","GET"])
def submitform1():
	data = json.dumps(dict(request.form),ensure_ascii=False)
	return data

@app.route("/argstodict1")
def args1():
	params = request.args.to_dict()
	stmt = jsonify({"your inputs": params})
	return stmt

if __name__ == "__main__":
	hosts = ["192.168.209.128"]
	app.run(hosts[0], port="5000",debug=True)