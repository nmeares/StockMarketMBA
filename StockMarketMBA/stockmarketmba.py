import StockMarketMBA.lib as lib
from requests.sessions import session
import json

HEADERS_PATH = './headers.json'

class api():
    
    def __init__(self):
        
        # Initiate
        self.s = session()
        with open(HEADERS_PATH) as f:
            self.HEADERS = json.load(f)


    def symbol_lookup(self, ticker):
        url = "https://stockmarketmba.com/symbollookup.php"
        # Retrieve version ID from web form
        forms = lib.get_forms(url, s)[1]
        details = lib.form_details(forms)
        version = lib.get_version(details)

        # Add ticker and version ID to search payload
        payload = 'action=Go&search={}&version={}'.format(ticker, version)

        # Request and find table
        r = self.s.post(url, headers=self.HEADERS, data=payload)
        return lib.get_table(r.text, 'searchtable')


    def exch_secs(self,exchange_code):
        url = "https://stockmarketmba.com/listofstocksforanexchange.php"
        payload = 'action=Go&exchangecode={}'.format(exchange_code)

        # Request and find table
        r = self.s.post(url, headers=self.HEADERS, data=payload)
        return lib.get_table(r.text, 'ETFs')


    def exch_symbols(self):
        url = 'https://stockmarketmba.com/globalstockexchanges.php'

        r = self.s.get(url)
        return lib.get_table(r.text, 'ETFs')


    def pending_SPACs(self):
        url = 'https://stockmarketmba.com/pendingspacmergers.php'

        r = self.s.get(url)
        return lib.get_table(r.text, 'ETFs')
