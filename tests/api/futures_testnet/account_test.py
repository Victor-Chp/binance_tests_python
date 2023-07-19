from binance_tests.utils.requests_extensions import requests
from project_cfg import BaseUrls, CreateSignature
from binance_tests.model.api.routes.perpetual_futures import (
    accountroutes,
)
from binance_tests.model.data.perpetual_futures_trade import (
    AccountInformationModel,
    AccountAssetsModel,
)
from binance_tests.creds.api_creds import ApiCreds
from binance_tests.model.data.error_codes import ErrorCodes


base_url = BaseUrls().futures_testnet
api_key = ApiCreds().futures_testnet_key
api_secret = ApiCreds().futures_testnet_secret
headers = {'X-MBX-APIKEY': api_key}


def test_get_account_information():
    params = {}
    params['signature'] = CreateSignature(
        ApiCreds().futures_testnet_key,
        ApiCreds().futures_testnet_secret,
        params
        # TODO: refactor to something shorter like: creds.api.key, creds.api.secret, params
    ).signature

    response = requests.get(
        f'{base_url}/{accountroutes.account}', headers=headers, params=params
    )

    assert (
        response.status_code == 200
    ), response.json()  # todo: refactor response.json() out, hide it
    '''
    # some versions of refactoring
    expect(response).have_code_ok()
    assert_(response).have_code_ok()
    response.should(have.code_ok)
    '''

    AccountInformationModel.assert_(response.json())
    account_assets = AccountAssetsModel(
        **response.json().get('assets')[0]
    )  # TODO: refactor


def test_get_account_information_wrong_api_key():
    params = {}
    wrong_api_key = ''
    # print(len(api_key), '\n')
    # print(api_key)
    # print(wrong_api_key)
    params['signature'] = CreateSignature(wrong_api_key, api_secret, params).signature
    response = requests.get(
        f'{base_url}/{accountroutes.account}', headers=headers, params=params
    )
    assert response.status_code == 401, response.json()
    # print(response.json())


def test_get_account_information_wrong_api_secret():
    params = {}
    wrong_api_secret = api_secret[:63]
    params['signature'] = CreateSignature(
        ApiCreds().futures_testnet_key, wrong_api_secret, params
    ).signature
    response = requests.get(
        f'{base_url}/{accountroutes.account}', headers=headers, params=params
    )
    assert response.status_code == 400, response.json()
    assert response.json() == ErrorCodes().code_1022


def test_get_income_history():
    params = {}
    params['signature'] = CreateSignature(
        ApiCreds().futures_testnet_key, api_secret, params
    ).signature
    response = requests.get(
        f'{base_url}/{accountroutes.income}', headers=headers, params=params
    )
    assert response.status_code == 200, response.json()
    # print(response.json())
