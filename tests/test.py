
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from StockMarketMBA import stockmarketmba as mba

api = mba.api()

print(api.exch_symbols())