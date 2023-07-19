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
from binance_apps.model.data.error_codes import ErrorCodes


base_url = BaseUrls().futures_testnet
api_key = ApiCreds().futures_testnet_key
api_secret = ApiCreds().futures_testnet_secret
headers = {'X-MBX-APIKEY': api_key}


def test_get_account_information():
    params = {}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.get(
        f'{base_url}/{accountroutes.account}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()
    # НЕ ВАЛИДИРУЕТ вложенные массивы
    account_information = AccountInformationModel(**response.json())
    account_assets = AccountAssetsModel(**response.json().get('assets')[0])
    # print('\n', params, '\n')
    # print(response.json())


def test_get_account_information_wrong_api_key():
    params = {}
    wrong_api_key = ''
    # print(len(api_key), '\n')
    # print(api_key)
    # print(wrong_api_key)
    params['signature'] = CreateSignature(wrong_api_key,api_secret, params).signature
    response = custom_session.get(f'{base_url}/{accountroutes.account}', headers=headers, params=params)
    assert  response.status_code == 401, response.json()
    # print(response.json())


def test_get_account_information_wrong_api_secret():
    params = {}
    wrong_api_secret = api_secret[:63]
    params['signature'] = CreateSignature(api_key,wrong_api_secret, params).signature
    response = custom_session.get(f'{base_url}/{accountroutes.account}', headers=headers, params=params)
    assert response.status_code == 400, response.json()
    assert response.json() == ErrorCodes().code_1022


def test_get_income_history():
    params = {}
    params['signature'] = CreateSignature(api_key, api_secret, params).signature
    response = custom_session.get(f'{base_url}/{accountroutes.income}', headers=headers, params=params)
    assert response.status_code == 200, response.json()
    # print(response.json())