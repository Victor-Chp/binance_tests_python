import hashlib
import hmac
from urllib.parse import urlencode

import pydantic
import os
import time
root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class BaseUrls(pydantic.BaseModel):
    perpetual_futures: str = 'https://fapi.binance.com'
    futures_testnet: str = 'https://testnet.binancefuture.com'

    spot: str = 'https://api.binance.com'
    spot_testnet: str = 'https://testnet.binance.vision'


class CreateSignature():
    def __init__(self, api_key, api_secret, params: dict):
        self.api_key = api_key
        self.api_secret = api_secret
        self.params = params
        self.timestamp = int(time.time() * 1000)
        self.params['timestamp'] = self.timestamp
        self.query_string = urlencode(self.params)
        self.signature = hmac.new(self.api_secret.encode('utf-8'), self.query_string.encode('utf-8'), hashlib.sha256).hexdigest()


# test = CreateSignature()
# print(test.params)