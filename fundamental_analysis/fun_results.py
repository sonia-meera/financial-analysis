from valuation_ratios import getMarketCap, getDividendYield

marketCapResults = {'micro': "Micro Cap (Less than $250M): You should avoid this company. Micro Caps have very high volatility, liquididty problems, and are highly susceptible to pump and dump schemes.", "small": "Small Cap (Between $250M and $1B): You should avoid this company unless you have insider knowledge on them. This could be attractive, however, if you intend to buy and sell stocks within short time periods as they are more volatile.", "mid": "Mid Cap (Between $1B and $5B): Some mid cap companies can be worth your investment, but beware! They are still more volatile than large and mega cap companies. However, you may find success in options trading.", "large": "Large Cap (Between $5B and $200B): These are typically your safest bet as they are very stable, well-covered companies. You can use options on these companies to maximize your results.", "mega": "Mega Cap (Greater than $200B): These are the most stable companies that exist. Due to such a low volatility, you should use options trading to maximize your result."}

divYieldRes = {'no_yld': "No Yield: If you're an income investor, you should avoid tihs. However, if you are a growth investor, you may prefer investing in a no-dividend company", 'low': "Low Yield (0.1-2%): Since this is below the current inflation rate, dividend yield should not be the main reason to invest in this", 'medium': 'Medium Yield (2-5%): ', 'high': 'High Yield', 'very_high': 'Very High Yield'}

marketCap = getMarketCap()
dividendYield = getDividendYield()
inflationRate = 2.4

def getMarketResults():
    print(marketCap)
    if(marketCap <= 250000000):
        print(marketCapResults['micro'])
    elif(marketCap > 250000000 and marketCap < 1000000000):
        print(marketCapResults['small'])
    elif(marketCap > 1000000000 and marketCap < 5000000000):
        print(marketCapResults['mid'])
    elif(marketCap > 5000000000 and marketCap < 200000000000):
        print(marketCapResults['large'])
    else:
        print(marketCapResults['mega'])
    
getMarketResults()

