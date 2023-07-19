import os.path
import json
from projectcfg import root_path
import jsonschema


def load_postman_collection(name: str):
    collection_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)

    with open(collection_path) as collection:
        return json.load(collection)


def create_class_name(name, api_name):
    name = name.replace(' ', '').replace('-', '').replace('/', '')
    code = (
        f'\n\n\nclass {name}Routes(pydantic.BaseModel):\n'
        f'    '
        f'name = "{api_name} - {name}"\n'
    )
    return code


def create_route_name(values):
    # print(values)
    url_list = {}
    for item in values:
        string = item['request']['url']['path'][-1]
        if string[0].isnumeric():
            string = '_' + string
        string = string.replace('-', '_')
        url_list[string] = '/'.join(item['request']['url']['path'])

    code = ''
    for key, value in url_list.items():
        code = code + f'\n    {key}: str = "{value}"'
    return code


def make_classes_code(collection, api_name):
    code = 'import pydantic'

    if api_name in ('Perpetual Futures', 'Delivery Futures', 'European Options'):
        for route in collection['item']:
            code = code + create_class_name(name=route['name'], api_name=api_name)
            code = code + create_route_name(route['item'])

    if api_name == 'Spot':
        for route in collection['item']:
            code = code + create_class_name(name=route['name'], api_name=api_name)
            if 'request' in route['item'][0]:
                code = code + create_route_name(route['item'])
            else:
                items_list = []
                for item in route['item']:
                    items_list.append(item['item'][0])
                    # print(item)
                code = code + create_route_name(items_list)

    if api_name == 'Broker':
        code = (
            code + '\n\n\nclass BrokerRoutes(pydantic.BaseModel):'
            '\n    name = "Broker"\n'
        )
        items_list = []
        for route in collection['item']:
            items_list.append(route)

        code = code + create_route_name(items_list)

    code = code + '\n'
    return code


def make_routes_file(content, file_name):
    path = os.path.join(root_path, 'binance_apps', 'model', 'api', 'routes', file_name)
    with open(path, mode='w', encoding="utf-8") as file:
        file.write(content)


perpetual_futures = make_classes_code(
    load_postman_collection('Binance_USDs_M_Futures_API.postman_collection.json'),
    'Perpetual Futures',
)
make_routes_file(perpetual_futures, 'perpetual_futures.py')

delivery_futures = make_classes_code(
    load_postman_collection('Binance_Coin_M_Futures_API.postman_collection.json'),
    'Delivery Futures',
)
make_routes_file(delivery_futures, 'delivery_futures.py')

spot = make_classes_code(
    load_postman_collection('Binance_Spot_API.postman_collection.json'), 'Spot'
)
make_routes_file(spot, 'spot.py')

broker = make_classes_code(
    load_postman_collection('Binance_Broker_API.postman_collection.json'), 'Broker'
)
make_routes_file(broker, 'broker.py')

european_options = make_classes_code(
    load_postman_collection('Binance_European_Options_API.postman_collection.json'),
    'European Options',
)
make_routes_file(european_options, 'european_options.py')