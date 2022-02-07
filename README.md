# 📈 Stock Market MBA

A simple library for accessing data from [stockmarketmba.com](https://stockmarketmba.com).

API queries currently return a JSON object, however future development will allow further options such as a Pandas DataFrame and CSV.

## Current Endpoints

* **Symbol lookup** - *returns stock identifiers*
* **Stocks on Exchange** - *returns list of stocks on a particular exchange*
* **Global Exchange Symbols** - *returns a list of exchange symbols for use with other endpoints*
* **Pending SPACS** - *returns a list of pending SPACs*

## Install

```shell
pip install stockmarketmba
```

### Usage

```python
>>> import StockMarketMBA as mba
>>> api = mba.api()

# Retrieve stock info
>>> sec_ids = test.symbol_lookup('aapl')
>>> print(sec_ids)

[{},
 {'Symbol': 'AAPL',
  'Description': 'Apple Inc',
  'Security Type': 'Common stocks',
  'Exchange Code': 'UW',
  'Exchange Country': 'USA',
  'Index Country': 'USA',
  'Sedol': '2046251',
  'Category1': 'US Equity',
  'Category2': 'Common stocks',
  'Category3': 'Large cap',
  'Avg Volume': '103,082,603',
  'Actions': 'Analyze'}]

# Retrieve exchange security list (e.g. London Stock Exchange)
>>> exch_secs = test.exch_secs('GB')
>>> print(exch_secs)

[{},
 {'Symbol': 'GB:3RB',
  'Description': 'RECKITT BENCK GRP',
  'Local Symbol': '3RB',
  'IPO Date': '01/04/2010',
  'Category1': 'Global Equity',
  'Category2': 'Common stocks',
  'Category3': 'Developed markets ex-US',
  'GICS Sector': 'Consumer Staples',
  'ISIN': 'GB00B24CGK77',
  'SEDOL': 'B28STJ1',
  'Market Cap': '51,608,408,503',
  'Currency': 'EUR',
  'Actions': 'Analyze'},
 {'Symbol': 'GB:HABA',
  'Description': 'Hamborner REIT AG',
  'Local Symbol': 'HABA',
  'IPO Date': '02/04/2021',
  'Category1': 'Global Equity',
  'Category2': 'Common stocks',
  'Category3': 'Developed markets ex-US',
  'GICS Sector': 'Unknown',
  'ISIN': 'DE000A3H2333',
  'SEDOL': 'BMH5DF7',
  'Market Cap': '0',
  'GICS Sector': '',
  'ISIN': '',
  'SEDOL': '',
  'Market Cap': '',
  'Currency': '',
  'Actions': ''}]
```

## Future Development

- [ ] Add more endpoints
- [ ] Add more output options (pandas, csv, etc.)
