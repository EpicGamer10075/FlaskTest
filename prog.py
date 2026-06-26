#/usr/bin/env python
from flask import Flask, render_template, request, json, jsonify
import sqlite3

app = Flask(__name__)

mydb = sqlite3.connect("data.db") #opens database in this thread
cur = mydb.cursor() #creates cursor in database to execute commands
cur.execute("CREATE TABLE IF NOT EXISTS block(name VARCHAR[32] NOT NULL)")
res = cur.execute(f"SELECT name FROM block")
print(f"{res.fetchone()!r}")
if f"{res.fetchone()!r}" == "None": #if current is empty (should only happen on first startup)
    cur.execute(f"INSERT INTO block(name) VALUES ('dummy')") #insert 'dummy' into block's name
mydb.commit() #commits the database so it persists between sessions
mydb.close() #closes the database thread

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.json['text']
    print("data:", data)
    
    mydb = sqlite3.connect("data.db")
    cur = mydb.cursor()
    res = cur.execute(f"SELECT name FROM block")
    cur.execute(f"UPDATE block SET name = '{data}'")
    
    result = cur.execute(f"SELECT name FROM block").fetchone()[0]

    mydb.commit() #commits the database so it persists between sessions
    mydb.close() #closes the database thread
    return result #returns name retrieved from database

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15271, debug=True) #Branch from Evan
#new comment
