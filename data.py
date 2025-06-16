import requests

def getfundamentalData():
    url = f'https://eodhd.com/api/fundamentals/AAPL.US?api_token=demo&fmt=json'
    data = requests.get(url).json()

    return data

def getEodData():
    url = f'https://eodhd.com/api/eod/AAPL.US?from=2020-06-15&to=2025-06-15&period=d&api_token=demo&fmt=json'
    data = requests.get(url).json()
    return data


print('test2')