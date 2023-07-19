import pytest
from helper import custom_session
from projectcfg import BaseUrls, CreateSignature
from binance_apps.model.api.routes.perpetual_futures import (
    marketroutes,
    accountroutes,
    orderroutes,
)
from binance_apps.model.data.perpetual_futures_trade import (
    AccountInformationModel,
    AccountAssetsModel,
    OrderModel,
)
from binance_apps.creds.api_creds import ApiCreds
from binance_apps.model.data.exchangeinfo import exchangeinfo


base_url = BaseUrls().futures_testnet
api_key = ApiCreds().futures_testnet_key
api_secret = ApiCreds().futures_testnet_secret
headers = {'X-MBX-APIKEY': api_key}

perpetual_futures_symbols = exchangeinfo(
    base_url=BaseUrls().perpetual_futures, exchange_url=marketroutes.exchangeInfo
).get_symbols_perpetual_futures()
minqty_for_market_order = exchangeinfo(
    base_url=BaseUrls().perpetual_futures, exchange_url=marketroutes.exchangeInfo
).get_minqty_dict_for_market_lot_size(marketroutes.price)


def test_get_account_information():
    params = {}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.get(
        f'{base_url}/{accountroutes.account}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()
    # НЕ ВАЛИДИРУЕТ вложенные массивы
    account_information = AccountInformationModel(**response.json())
    account_assets = AccountAssetsModel(**response.json()['assets'][0])
    print('\n', params, '\n')
    print(response.json())


def test_post_new_order_market_buy_btcusdt():
    params = {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.post(
        f'{base_url}/{orderroutes.order}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()
    new_order = OrderModel(**response.json())
    # print(response.json())


def test_post_new_order_market_sell_btcusdt():
    params = {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.post(
        f'{base_url}/{orderroutes.order}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()

    params = {'symbol': 'BTCUSDT', 'side': 'SELL', 'type': 'MARKET', 'quantity': 0.001}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.post(
        f'{base_url}/{orderroutes.order}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()


@pytest.mark.parametrize('symbol', perpetual_futures_symbols)
def test_post_new_order_market_buy_minqty(symbol):
    quantity = minqty_for_market_order[symbol]
    # print(quantity)
    params = {'symbol': symbol, 'side': 'BUY', 'type': 'MARKET', 'quantity': quantity}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.post(f'{base_url}/{orderroutes.order}', headers=headers, params=params)
    # print('\n', params, '\n')
    # print(response.json())
    assert response.status_code == 200, response.json()