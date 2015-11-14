from flask import Flask
from redis import Redis
import MySQLdb

app = Flask(__name__)
app.debug = True
redis = Redis(host='redis', port=6379)

@app.route('/hello')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

@app.route('/hellodb')
def helloDb():
	db = MySQLdb.connect("db","testuser","test123","TESTDB")
	db.autocommit(True)
	cursor = db.cursor()
	cursor.execute("SELECT VERSION()")
	data = cursor.fetchone()
	cursor.execute("UPDATE hits set count = count + 1")
	cursor.execute("SELECT count FROM hits")
	row = cursor.fetchone()
	return 'Hello World DB! I have been seen {} times. Database version : {} '.format(row[0], data);
	db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
	
