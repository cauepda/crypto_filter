# https://api.poloniex.com/markets/{symbol}/candles
import json
import requests
import pandas as pd
import numpy as np
import datetime

def get_data(symbol, period, start, end):
    url = f'https://api.poloniex.com/public?command=returnChartData&currencyPair={symbol}&start={start}&end={end}&period={period}'
    response = requests.get(url)
    data = response.json()
    return data

get_data('USDT_BTC', 300, 1617244800, 1617331200)