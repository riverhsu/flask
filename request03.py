#coding: utf-8

from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():
	lan = request.args.get('language')
	return '<H1> your language is %s </H1>' % lan

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
	lan = request.form.get('language')
	fw = request.form.get('framework')

	if request.method == 'POST':  # judge passing method
		if (lan, fw) == (None, None):
		    return '''<form method="POST">
		                  Language: <input type="text" name="language"><br>
		                  Framework: <input type="text" name="framework"><br>
		                  <input type="submit" value="Submit"><br>
		              </form>'''
		else:
		 	return '<H1> your language is %s, your framework is %s </H1>' % (lan, fw)

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

@app.route('/show-attribute')
def showinfo():
	path = request.path
	url = request.url
	url_root = request.url_root

	return '''
		The path is : %s ;
		The URL is : %s ;
		The URL_root is : %s ;''' % (path, url, url_root)

if __name__ == ('__main__'):
	app.run(host='192.168.209.156', port=8050, debug=True)