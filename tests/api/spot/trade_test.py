from binance_tests.utils.requests_extensions import requests
from project_cfg import BaseUrls, CreateSignature
from binance_tests.model.api.routes.spot import traderoutes
from binance_tests.creds.api_creds import ApiCreds

base_url = BaseUrls()
creds = ApiCreds()


headers = {
    'X-MBX-APIKEY': creds.spot_key
}


def test_get_account_information():
    params = {'recvWindow': 5000}
    params['signature'] = CreateSignature(creds.spot_key, creds.spot_secret, params).signature
    response = requests.get(f'{base_url.spot}/{traderoutes.account}', headers=headers, params=params)
    assert response.status_code == 200
    print('\n', params, '\n')
    # print(test.params)
    print(response.json())
