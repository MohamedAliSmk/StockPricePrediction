#from dotenv import load_dotenv
import os
import pymongo     
from flask import Flask, jsonify


def get_db():
	DATABASE_URL='mongodb+srv://Fintech:qANVTzWevwD9UZz6@stockpriceprediction.9srtpdu.mongodb.net/?retryWrites=true&w=majority'         
	client=pymongo.MongoClient(DATABASE_URL) # establish connection with database
	mongo_db=client.db
	return mongo_db
 
app=Flask(__name__)

@app.route('/')
def ping_server(): 
  	return "welcome to the world"

@app.route('/data')
def fetch_data():
	mongo_db=get_db()
	_data = mongo_db.stock_data.find()
	data =[{"date": dataa["date"], 'o': dataa['o'],'h':dataa['h'],'l':dataa['l'],'c':dataa['c'],'adjc':dataa['adjc'],'v': dataa['v'],'ticker':dataa['ticker']} for dataa in _data]
    
	return jsonify({"data":data})

if __name__ == '__main__':
	app.run()