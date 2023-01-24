import yfm


fetcher = yfm.fetcher()
fetcher.getTicker("goog")  # read from the db
fetcher.update() # same as 'yfm update's
