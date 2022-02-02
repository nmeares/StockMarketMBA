
import os
import sys

from StockMarketMBA import stockmarketmba as mba

api = mba.api()

print(api.exch_symbols())