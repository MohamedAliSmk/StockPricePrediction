"""This is the main file called to run the flask application"""
from dotenv import load_dotenv
from root.factory import create_app
from flask import Blueprint
from flask import request, render_template, jsonify
import yfinance as yf

main = Blueprint("main", __name__)

@main.route("/quote")
def display_quote():
	# get a stock ticker symbol from the query string
	# default to AAPL
	symbol = request.args.get('symbol', default="AAPL")

	# pull the stock quote
	quote = yf.Ticker(symbol)

	#return the object via the HTTP Response
	return jsonify(quote.info)


# API route for pulling the stock history
@main.route("/history")
def display_history():
	#get the query string parameters
	symbol = request.args.get('symbol', default="AAPL")
	period = request.args.get('period', default="1y")
	interval = request.args.get('interval', default="1mo")

	#pull the quote
	quote = yf.Ticker(symbol)	
	#use the quote to pull the historical data from Yahoo finance
	hist = quote.history(period=period, interval=interval)
	#convert the historical data to JSON
	data = hist.to_json()
	#return the JSON in the HTTP response
	return data

@main.route("/financials")
def display_financials():
    symbol =request.args.get('symbol', default="AAPL")
    
    #pull the quote
    quote=yf.Ticker(symbol)

    #use the quote to pull income sheet
    yearly_inc_stmt=quote.income_stmt
    quarterly_inc_stmt=quote.quarterly_income_stmt

    #use the quote to pull balance sheet
    yearly_balance_sheet=quote.balance_sheet
    quarterly_balance_sheets=quote.quarterly_balance_sheet


    #use the quote to pull cash flow
    yearly_cash_stmt=quote.cashflow
    quarterly_cash_stmt=quote.quarterly_cashflow


    #show earnings
    earnings=quote.earnings
    quar_earnings=quote.earnings

    #show sustainability
    sustainability=quote.sustainability


@main.route("/AnalystsRecommendations")
def display_analysts():
    symbol =request.args.get('symbol', default="AAPL")
    
    #pull the quote
    quote=yf.Ticker(symbol)

    # show analysts recommendations
    recommeds=quote.recommendations
    summary=quote.recommendations_summary
    # show analysts other work
    target_price=quote.analyst_price_target
    rev_forcast=quote.revenue_forecasts
    earnings_forcast=quote.earnings_forecasts
    earnings_trend=quote.earnings_trend


@main.route("/news")
def get_news():

    symbol =request.args.get('symbol', default="AAPL")
    
    #pull the quote
    quote=yf.Ticker(symbol)
      

    #get_news
    news=quote.news

    

   


if __name__ == "__main__":
    load_dotenv()
    app = create_app()
    app.run()
