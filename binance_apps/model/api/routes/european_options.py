import pydantic


class MarketRoutes(pydantic.BaseModel):
    name = "European Options - Market"

    ping: str = "eapi/v1/ping"
    time: str = "eapi/v1/time"
    exchangeInfo: str = "eapi/v1/exchangeInfo"
    depth: str = "eapi/v1/depth"
    trades: str = "eapi/v1/trades"
    historicalTrades: str = "eapi/v1/historicalTrades"
    klines: str = "eapi/v1/klines"
    mark: str = "eapi/v1/mark"
    ticker: str = "eapi/v1/ticker"
    index: str = "eapi/v1/index"
    exerciseHistory: str = "eapi/v1/exerciseHistory"


class AccountTradesRoutes(pydantic.BaseModel):
    name = "European Options - AccountTrades"

    account: str = "eapi/v1/account"
    transfer: str = "eapi/v1/transfer"
    order: str = "eapi/v1/order"
    batchOrders: str = "eapi/v1/batchOrders"
    allOpenOrders: str = "eapi/v1/allOpenOrders"
    allOpenOrdersByUnderlying: str = "eapi/v1/allOpenOrdersByUnderlying"
    openOrders: str = "eapi/v1/openOrders"
    historyOrders: str = "eapi/v1/historyOrders"
    position: str = "eapi/v1/position"
    userTrades: str = "eapi/v1/userTrades"
    exerciseRecord: str = "eapi/v1/exerciseRecord"
    bill: str = "eapi/v1/bill"


class DataStreamRoutes(pydantic.BaseModel):
    name = "European Options - DataStream"

    userDataStream: str = "eapi/v1/userDataStream"


class MarketMakerRoutes(pydantic.BaseModel):
    name = "European Options - MarketMaker"

    marginAccount: str = "eapi/v1/marginAccount"
