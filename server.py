from flask import Flask, render_template, send_from_directory, request
import pyodbc
import os
import json
app = Flask(__name__, static_folder='public')
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

@app.route('/data',  methods=["GET"])
def indexs():
    connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mhacks.database.windows.net,1433;Database=mhacks;Uid=ajaykumar@mhacks;Pwd=ILoveAjay!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = connection.cursor()
    cursor.execute("SELECT [startdate], [FinalPrice], [Delta], [Score] FROM AnalyzedData WHERE [Delta] != [FinalPrice]")
    weeks = []
    prices =[]
    delta=[]
    sentiments=[]
    row = cursor.fetchone()
    while row:
        weeks.append('-'.join([row[0][:4],row[0][4:6],row[0][6:]]))
        prices.append(row[1])
        delta.append(row[2])
        sentiments.append(row[3])
        row = cursor.fetchone()
    zipall = list(zip(weeks, prices, delta, sentiments))
    print(zipall)
    zip2 = sorted(list(zip(weeks, prices, delta, sentiments)), key=lambda t: t[0])
    print(zip2)
    weeks, prices, delta, sentiments = [list(t) for t in zip(*zip2)]
    return json.dumps({"weeks": json.dumps(weeks),
    		"Prices": json.dumps(prices),
    		"Sentiments": json.dumps(sentiments),
    		"Delta": json.dumps(delta)
    		})

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

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
