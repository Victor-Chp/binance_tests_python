import pydantic


class MarketRoutes(pydantic.BaseModel):
    name = "Delivery Futures - Market"

    ping: str = "dapi/v1/ping"
    time: str = "dapi/v1/time"
    exchangeInfo: str = "dapi/v1/exchangeInfo"
    depth: str = "dapi/v1/depth"
    trades: str = "dapi/v1/trades"
    historicalTrades: str = "dapi/v1/historicalTrades"
    aggTrades: str = "dapi/v1/aggTrades"
    premiumIndex: str = "dapi/v1/premiumIndex"
    fundingRate: str = "dapi/v1/fundingRate"
    klines: str = "dapi/v1/klines"
    continuousKlines: str = "dapi/v1/continuousKlines"
    indexPriceKlines: str = "dapi/v1/indexPriceKlines"
    markPriceKlines: str = "dapi/v1/markPriceKlines"
    _24hr: str = "dapi/v1/ticker/24hr"
    price: str = "dapi/v1/ticker/price"
    bookTicker: str = "dapi/v1/ticker/bookTicker"
    openInterest: str = "dapi/v1/openInterest"
    openInterestHist: str = "futures/data/openInterestHist"
    topLongShortAccountRatio: str = "futures/data/topLongShortAccountRatio"
    topLongShortPositionRatio: str = "futures/data/topLongShortPositionRatio"
    globalLongShortAccountRatio: str = "futures/data/globalLongShortAccountRatio"
    takerBuySellVol: str = "futures/data/takerBuySellVol"
    basis: str = "futures/data/basis"


class TradeRoutes(pydantic.BaseModel):
    name = "Delivery Futures - Trade"

    dual: str = "dapi/v1/positionSide/dual"
    order: str = "dapi/v1/order"
    batchOrders: str = "dapi/v1/batchOrders"
    orderAmendment: str = "dapi/v1/orderAmendment"
    allOpenOrders: str = "dapi/v1/allOpenOrders"
    countdownCancelAll: str = "dapi/v1/countdownCancelAll"
    openOrder: str = "dapi/v1/openOrder"
    openOrders: str = "dapi/v1/openOrders"
    allOrders: str = "dapi/v1/allOrders"
    account: str = "dapi/v1/account"
    leverage: str = "dapi/v1/leverage"
    marginType: str = "dapi/v1/marginType"
    positionMargin: str = "dapi/v1/positionMargin"
    history: str = "dapi/v1/positionMargin/history"
    positionRisk: str = "dapi/v1/positionRisk"
    userTrades: str = "dapi/v1/userTrades"
    income: str = "dapi/v1/income"
    leverageBracket: str = "dapi/v1/leverageBracket"
    forceOrders: str = "dapi/v1/forceOrders"
    adlQuantile: str = "dapi/v1/adlQuantile"


class DataStreamRoutes(pydantic.BaseModel):
    name = "Delivery Futures - DataStream"

    listenKey: str = "dapi/v1/listenKey"


class PortfolioMarginRoutes(pydantic.BaseModel):
    name = "Delivery Futures - PortfolioMargin"

    pmExchangeInfo: str = "dapi/v1/pmExchangeInfo"
    pmAccountInfo: str = "dapi/v1/pmAccountInfo"
