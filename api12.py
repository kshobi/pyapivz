#!/usr/bin/python3

import requests
from pprint import pprint

def main():
    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=ENB5Z31R9P07VDJL"
    fullstockdata=requests.get(mylookup)
    #print(stockdata.json())
    customizedstockdata=fullstockdata.json()["Meta Data"]["3. Last Refreshed"]
    print(customizedstockdata)
    #print(customizedstockdata["Time Series (5min)"]["2019-08-20 10:05:00"])
    #   print(customizedstockdata)

main()





















