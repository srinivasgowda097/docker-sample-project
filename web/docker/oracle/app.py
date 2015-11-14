from flask import Flask
from redis import Redis
import cx_Oracle

app = Flask(__name__)
app.debug = True
redis = Redis(host='redis', port=6379)

@app.route('/hello')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

@app.route('/hellodb')
def helloDb():
	db = cx_Oracle.connect('system/oracle@db:1521/XE')
	data = db.version
	cursor = db.cursor()
	cursor.execute("UPDATE hits set count = count + 1")
	db.commit()
	cursor.execute("SELECT count FROM hits")
	row = cursor.fetchone()
	return 'Hello World Oracle DB! I have been seen {} times. Database version : {} '.format(row[0], data);
	cursor.close
	db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
	
