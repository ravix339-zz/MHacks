from flask import Flask, render_template, send_from_directory, request
import os
import json
app = Flask(__name__, static_folder='public')
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

@app.route('/data',  methods=["GET"])
def indexs():
	return json.dumps({"weeks": json.dumps(["2015-04-06","2015-03-29", "2015-03-21","2015-02-25" "2015-03-04", "2015-03-05"]),
			"Prices": json.dumps(["3.4","4.6","-3", "1.5", ".3", ".1"]),
			"Sentiments": json.dumps(["9","12", "-2","16", "1", ".25"])
			})
def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

@app.route('/stop')
def stop():
	if(not(proc is None)):
	 	proc.sendcontrol('c')
	# shutdown_server()
	return 'stopped'

@app.route('/static/<path:filename>')
def send_static(filename):
	return send_from_directory(app.static_folder, 'static/'+filename)
@app.route('/favicon.ico')
def favicon():
	return ''
@app.route('/',  methods=["GET"])
def index():
	return send_from_directory(app.static_folder, 'index.html')
@app.route('/<path:path>',  methods=["GET"])
def catchall(path):
	return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False, threaded=True, port=4000)
