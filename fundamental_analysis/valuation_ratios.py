aapl = {'stock_price': 199.20, 'outstanding_shares': 14940000000, "dividend_share_amount": 0.26, 'curr_earnings_per_yr': 6.11}

stockPrice = aapl['stock_price']
outstandingShares = aapl['outstanding_shares']
dividendShareAmt = aapl['dividend_share_amount']
currEarningsPerYr = aapl['curr_earnings_per_yr']

def getMarketCap():
    return stockPrice * outstandingShares

def getDividendYield():
    return (dividendShareAmt/stockPrice)*100