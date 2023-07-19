from helper import custom_session
from projectcfg import BaseUrls, CreateSignature
from binance_apps.model.api.routes.spot import traderoutes
from binance_apps.creds.api_creds import ApiCreds

base_url = BaseUrls()
creds = ApiCreds()


headers = {
    'X-MBX-APIKEY': creds.spot_key
}


def test_get_account_information():
    params = {'recvWindow': 5000}
    params['signature'] = CreateSignature(creds.spot_key, creds.spot_secret, params).signature
    response = custom_session.get(f'{base_url.spot}/{traderoutes.account}', headers=headers, params=params)
    assert response.status_code == 200
    print('\n', params, '\n')
    # print(test.params)
    print(response.json())