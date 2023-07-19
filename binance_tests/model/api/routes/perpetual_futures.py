import pydantic


class MarketRoutes(pydantic.BaseModel):
    name = "Perpetual Futures - Market"

    ping: str = "fapi/v1/ping"
    time: str = "fapi/v1/time"
    exchangeInfo: str = "fapi/v1/exchangeInfo"
    depth: str = "fapi/v1/depth"
    trades: str = "fapi/v1/trades"
    historicalTrades: str = "fapi/v1/historicalTrades"
    aggTrades: str = "fapi/v1/aggTrades"
    klines: str = "fapi/v1/klines"
    continuousKlines: str = "fapi/v1/continuousKlines"
    indexPriceKlines: str = "fapi/v1/indexPriceKlines"
    markPriceKlines: str = "fapi/v1/markPriceKlines"
    premiumIndex: str = "fapi/v1/premiumIndex"
    fundingRate: str = "fapi/v1/fundingRate"
    _24hr: str = "fapi/v1/ticker/24hr"
    price: str = "fapi/v1/ticker/price"
    bookTicker: str = "fapi/v1/ticker/bookTicker"
    openInterest: str = "fapi/v1/openInterest"
    openInterestHist: str = "futures/data/openInterestHist"
    topLongShortAccountRatio: str = "futures/data/topLongShortAccountRatio"
    topLongShortPositionRatio: str = "futures/data/topLongShortPositionRatio"
    globalLongShortAccountRatio: str = "futures/data/globalLongShortAccountRatio"
    takerlongshortRatio: str = "futures/data/takerlongshortRatio"
    lvtKlines: str = "fapi/v1/lvtKlines"
    indexInfo: str = "fapi/v1/indexInfo"
    assetIndex: str = "fapi/v1/assetIndex"


marketroutes = MarketRoutes()


class AccountRoutes(pydantic.BaseModel):
    name = "Perpetual Futures - Account"

    account: str = "fapi/v2/account"
    income: str = "fapi/v1/income"
    positionRisk: str = "fapi/v2/positionRisk"
    userTrades: str = "fapi/v1/userTrades"
    balance: str = "fapi/v2/balance"
    leverageBracket: str = "fapi/v1/leverageBracket"
    adlQuantile: str = "fapi/v1/adlQuantile"
    commissionRate: str = "fapi/v1/commissionRate"
    multiAssetsMargin: str = "fapi/v1/multiAssetsMargin"


accountroutes = AccountRoutes()


class OrderRoutes(pydantic.BaseModel):
    name = "Perpetual Futures - Order"

    order: str = "fapi/v1/order"
    batchOrders: str = "fapi/v1/batchOrders"
    allOpenOrders: str = "fapi/v1/allOpenOrders"
    countdownCancelAll: str = "fapi/v1/countdownCancelAll"
    openOrders: str = "fapi/v1/openOrders"
    openOrder: str = "fapi/v1/openOrder"
    allOrders: str = "fapi/v1/allOrders"
    forceOrders: str = "fapi/v1/forceOrders"


orderroutes = OrderRoutes()


class TradeRoutes(pydantic.BaseModel):
    name = "Perpetual Futures - Trade"

    marginType: str = "fapi/v1/marginType"
    leverage: str = "fapi/v1/leverage"
    positionMargin: str = "fapi/v1/positionMargin"
    history: str = "fapi/v1/positionMargin/history"
    dual: str = "fapi/v1/positionSide/dual"
    multiAssetsMargin: str = "fapi/v1/multiAssetsMargin"
    apiTradingStatus: str = "fapi/v1/apiTradingStatus"


traderoutes = TradeRoutes()


class DataStreamRoutes(pydantic.BaseModel):
    name = "Perpetual Futures - DataStream"

    listenKey: str = "fapi/v1/listenKey"


class PortfolioMarginRoutes(pydantic.BaseModel):
    name = "Perpetual Futures - PortfolioMargin"

    pmExchangeInfo: str = "fapi/v1/pmExchangeInfo"
    pmAccountInfo: str = "fapi/v1/pmAccountInfo"
