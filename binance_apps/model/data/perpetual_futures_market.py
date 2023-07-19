from typing import Union
import pydantic
from pydantic.error_wrappers import ValidationError
from binance_apps.model.data.exchangeinfo import exchangeinfo
from projectcfg import BaseUrls
from binance_apps.model.api.routes.perpetual_futures import marketroutes

# Создать фикстуру и передавать результат (массив) из нее
print(exchangeinfo(
    base_url=BaseUrls().perpetual_futures, exchange_url=marketroutes.exchangeInfo
).get_onboard_date_perpetual_futures())


class OrderBookModel(pydantic.BaseModel):
    lastUpdateId: int
    E: int
    T: int
    bids: list[list[str]]
    asks: list[list[str]]


class KlineModel(pydantic.BaseModel):
    __root__: list[list[Union[int, str]]]

    @pydantic.validator('__root__')
    def check_open_close_time_difference(cls, array):
        # # print(array[-1])
        # assert not isinstance(array[-1][0], int), f'Value {array[-1][0]} (open time) not integer'
        if not isinstance(array[-1][0], int):
            raise TypeError(f'Value {array[-1][0]} (open time) not integer')

        values = [
            59999,
            179999,
            299999,
            899999,
            1799999,
            3599999,
            7199999,
            14399999,
            21599999,
            28799999,
            43199999,
            86399999,
            259199999,
            604799999,
            2678399999
        ]
        # Написать условие при котором  if onboard +
        difference = array[-1][6] - array[-1][0]
        if difference not in values:
            raise ValueError(
                'The difference between the opening and closing times does not correspond to the permissible values'
            )
        return array


class RecentTradesModel(pydantic.BaseModel):
    id: int
    price: str
    qty: str
    quoteQty: str
    time: int
    isBuyerMaker: bool


class RecentTradesListModel(pydantic.BaseModel):
    array: list[RecentTradesModel]
