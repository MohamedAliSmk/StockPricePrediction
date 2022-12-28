db=db.getSibling("StockPricePrediction");
db.stock_data.drop()

db.stock_data.insertMany[{'date': '2018-01-04', 
'o': 91.199997, 
'h': 91.739998,
'l': 90.839996,
'c': 91.139999,
'adjc': 80.725845,
'v': 363629,
'ticker': 'HO.PA'
},
{'date': '2018-01-05',
'o': 91.360001,
'h': 91.779999,
'l': 90.800003,
'c': 91.300003,
'adjc': 80.867569,
'v': 274216, 
'ticker': 'HO.PA'
}]