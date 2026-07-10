import pytest #type:ignore
import prog
import requests #type:ignore
import sqlite3

def func1() -> str:
	requests.post("http://127.0.0.1:15271/process-data", json = {"text":"1"})
	mydb = sqlite3.connect("data.db")
	cur = mydb.cursor()
	result = cur.execute(f"SELECT name FROM block").fetchone()[0]
	mydb.close()
	return result

def func2() -> str:
	requests.post("http://127.0.0.1:15271/process-data", json = {"text":"2"})
	mydb = sqlite3.connect("data.db")
	cur = mydb.cursor()
	result = cur.execute(f"SELECT name FROM block").fetchone()[0]
	mydb.close()
	return result

def test_prog():
	assert func1() == "1"
	assert func2() == "2"