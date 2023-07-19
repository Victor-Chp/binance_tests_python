import pytest
from helper import custom_session
from projectcfg import BaseUrls, CreateSignature
from binance_apps.model.api.routes.perpetual_futures import (
    marketroutes,
    accountroutes,
    orderroutes,
    traderoutes
)
from binance_apps.model.data.perpetual_futures_trade import (
    AccountInformationModel,
    AccountAssetsModel,
    OrderModel,
)
from binance_apps.creds.api_creds import ApiCreds
from binance_apps.model.data.exchangeinfo import exchangeinfo
from binance_apps.model.data.error_codes import ErrorCodes


base_url = BaseUrls().futures_testnet
api_key = ApiCreds().futures_testnet_key
api_secret = ApiCreds().futures_testnet_secret
headers = {'X-MBX-APIKEY': api_key}

perpetual_futures_symbols = exchangeinfo(
    base_url=BaseUrls().perpetual_futures, exchange_url=marketroutes.exchangeInfo
).get_symbols_perpetual_futures()


@pytest.mark.parametrize('symbol', perpetual_futures_symbols)
def test_change_margin_type_isolated(symbol):
    params = {'symbol': symbol, 'marginType': 'ISOLATED'}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.post(
        f'{base_url}/{traderoutes.marginType}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()


@pytest.mark.parametrize('symbol', perpetual_futures_symbols)
def test_change_margin_type_crossed(symbol):
    params = {'symbol': symbol, 'marginType': 'CROSSED'}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.post(
        f'{base_url}/{traderoutes.marginType}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()


def test_get_current_multi_assets_margin():
    params = {}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.get(
        f'{base_url}/{traderoutes.multiAssetsMargin}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()
    print(response.json())