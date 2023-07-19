import math
import requests

# Задача: передавать массив доступных интервалов в параметриз фикстуры pytest
kline_intervals = [
    '1m',
    '3m',
    '5m',
    '15m',
    '30m',
    '1h',
    '2h',
    '4h',
    '6h',
    '8h',
    '12h',
    '1d',
    '3d',
    '1w',
    '1M',
]


class PriceTicker:
    def __init__(self, base_url, market_url):
        self.base_url = base_url
        self.market_url = market_url

    def get_ticker_price_for_all_symbols(self):
        response = requests.get(f'{self.base_url}/{self.market_url}')
        raw_prices_data = response.json()
        assert (
            response.status_code == 200
        ), f'Expected status code 200, not {response.status_code}'
        assert 'symbol' in raw_prices_data[0], 'No Price/Ticker data from binance'
        prices_data = {}
        for symbol in raw_prices_data:
            prices_data[symbol['symbol']] = symbol['price']
        print(prices_data)
        return prices_data


# Задача: перед тестами получить данные ExchangeInfo один раз и в дальнейшем вызывать методы из полученных данных
# Т.е. не выполнять запрос при каждом вызове метода
class ExchangeInfo:
    def __init__(self, base_url, exchange_url):
        self.base_url = base_url
        self.exchange_url = exchange_url

    def get_exchangeinfo(self):
        response = requests.get(f'{self.base_url}/{self.exchange_url}')
        exchange_data = response.json()
        assert (
            response.status_code == 200
        ), f'Expected status code 200, not {response.status_code}'
        assert 'assets' in exchange_data, 'No data from binance'
        return exchange_data

    def get_symbols_perpetual_futures(self):
        exchange_data = self.get_exchangeinfo()
        symbols_list = []
        for symbol in exchange_data['symbols']:
            match symbol['contractType']:
                case 'PERPETUAL':
                    match symbol['status']:
                        case 'TRADING':
                            symbols_list.append(symbol['symbol'])
        return symbols_list

    def get_onboard_date_perpetual_futures(self):
        exchange_data = self.get_exchangeinfo()
        onboard_symbols_list = {}
        for symbol in exchange_data['symbols']:
            match symbol['contractType']:
                case 'PERPETUAL':
                    match symbol['status']:
                        case 'TRADING':
                            onboard_symbols_list[symbol['symbol']] = symbol['onboardDate']
        return onboard_symbols_list

    def get_minqty_dict_for_market_lot_size(self, market_url):
        exchange_data = self.get_exchangeinfo()
        prices_data = PriceTicker(base_url=self.base_url, market_url=market_url).get_ticker_price_for_all_symbols()
        minqty_symbols_dict = {}
        for symbol in exchange_data['symbols']:
            if symbol['contractType'] == 'PERPETUAL':
                if symbol['status'] == 'TRADING':
                    if symbol['filters'][2]['filterType'] == 'MARKET_LOT_SIZE':
                        if symbol['filters'][5]['filterType'] == 'MIN_NOTIONAL':
                            notional_for_minqty = float(prices_data[symbol['symbol']]) * float(symbol['filters'][2]['minQty'])
                            if notional_for_minqty < float(symbol['filters'][5]['notional']):
                                min_notional = math.ceil(float(symbol['filters'][5]['notional']) / notional_for_minqty)
                                minqty = float(symbol['filters'][2]['minQty']) * min_notional
                                minqty_symbols_dict[symbol['symbol']] = minqty
                            else:
                                minqty_symbols_dict[symbol['symbol']] = symbol['filters'][2]['minQty']
                # match symbol['contractType']:
            #     case 'PERPETUAL':
            #         match symbol['filters'][2]['filterType']:
            #             case 'MARKET_LOT_SIZE':
            #                 match symbol['filters'][5]['filterType']:
            #                     case 'MIN_NOTIONAL':
            #                         minqty_symbols_dict[symbol['symbol']] = symbol[
            #                             'filters'
            #                         ][2]['minQty']
        return minqty_symbols_dict


exchangeinfo = ExchangeInfo
