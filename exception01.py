from flask import Flask, abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    return 'Error: ' , 404

if __name__ == '__main__':
	host=['0.0.0.0', '192.168.11.144',]
	app.run(host[1], port='8000', debug=False)	
