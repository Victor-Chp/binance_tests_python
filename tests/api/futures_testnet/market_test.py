import pytest
from datetime import datetime
from helper import custom_session
from projectcfg import BaseUrls
from binance_apps.model.data.exchangeinfo import exchangeinfo, kline_intervals
from binance_apps.model.api.routes.perpetual_futures import marketroutes
from binance_apps.model.data.perpetual_futures_market import OrderBookModel, RecentTradesListModel, KlineModel

base_url = BaseUrls().futures_testnet

perpetual_futures = exchangeinfo(
    base_url=BaseUrls().perpetual_futures, exchange_url=marketroutes.exchangeInfo
).get_symbols_perpetual_futures()


@pytest.mark.parametrize('symbol', perpetual_futures[:5])
def test_get_order_book(symbol):
    params = {'symbol': symbol}
    time_before_response = int(int(datetime.now().timestamp() * 1000))
    response = custom_session.get(f'{base_url}/{marketroutes.depth}', params=params)
    assert response.status_code == 200, f'Status code {response.status_code}, not 200'
    orderbook_data = OrderBookModel(**response.json())
    # assert orderbook_data.T > time_before_response


@pytest.mark.parametrize('symbol', perpetual_futures[:5])
def test_get_recent_trades_list(symbol):
    params = {'symbol': symbol, 'limit': 1}
    response = custom_session.get(f'{base_url}/{marketroutes.trades}', params=params)
    assert response.status_code == 200, f'Status code {response.status_code}, not 200'
    tradeslistdata = {'array': response.json()}
    tradeslist_data = RecentTradesListModel(**tradeslistdata)
    assert len(tradeslist_data.array) == params['limit'], f'Limit {len(response.json())}, not {params["limit"]}'


@pytest.mark.parametrize('interval', kline_intervals)
@pytest.mark.parametrize('symbol', perpetual_futures)
def test_get_one_kline_perpetual_futures(symbol, interval):
    params = {'symbol': symbol, 'interval': interval, 'limit': 2}
    response = custom_session.get(f'{base_url}/{marketroutes.klines}', params=params)
    assert response.status_code == 200, f'Status code {response.status_code}, not 200'
    klinedata = {'__root__': response.json()}
    kline_data = KlineModel(**klinedata)
    assert len(kline_data.__root__) == params['limit'], f'Limit {len(response.json())}, not {params["limit"]}'
    KlineModel.check_open_close_time_difference(response.json())
    # with pytest.raises(TypeError):
    #     KlineModel.check_open_close_time_difference(response.json())
