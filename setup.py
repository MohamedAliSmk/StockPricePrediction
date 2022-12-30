import yfm
fetcher = yfm.fetcher()
fetcher.getTicker("AAPL")  # read from the db
fetcher.update() # same as 'yfm update'
a=fetcher()
