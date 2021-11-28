from fmp_python.fmp import FMP
from config import fmp_key, fmp_url
from ratelimit import limits, sleep_and_retry
import requests
import pandas as pd


# 300 calls per minute
calls = 300
rate_limit = 60


@sleep_and_retry
@limits(calls=calls, period=rate_limit)
def check_limit():
    # Empty function to throttle calls to API
    return None


fmp = FMP(api_key=fmp_key)


def full_history(ticker):
    url = fmp_url + "historical-price-full/" + ticker +  "?apikey=" + fmp_key
    response = requests.get(url)
    j = response.json()
    data = pd.DataFrame.from_dict(j['historical'])
    return data

