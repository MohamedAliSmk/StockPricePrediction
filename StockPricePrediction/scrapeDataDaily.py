import schedule
import time
from datetime import datetime, timedelta
import requests
import json
import pymongo


# Connect to the MongoDB server
client=pymongo.MongoClient()
db = client.stock_data
collection = db.stock_data

def scrape_data(Stock_symbol):
    # Get the current date
    today = datetime.now()
    # Get the date range (30 days ago)
    start_date = (today - timedelta(days=30)).strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    
    # Construct the API URL
    url = 'https://finance.yahoo.com/quote/'+ Stock_symbol +'/history?period1=1546300800&period2=1609439200&interval=1d&filter=history&frequency=1d'

    # Send the GET request to the API
    response = requests.get(url)
    data = json.loads(response.text)
    
    # Append the data to the MongoDB collection
    collection.insert_many(data)
    print("Data has been scraped and updated at", datetime.now())

schedule.every(24).hours.do(scrape_data('AAPL'))

while True:
    schedule.run_pending()
    time.sleep(1)

