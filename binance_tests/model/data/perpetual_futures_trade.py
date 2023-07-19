from binance_tests.utils.extensions import pydantic


class AccountAssetsModel(pydantic.BaseModel):
    asset: str
    walletBalance: str
    unrealizedProfit: str
    marginBalance: str
    maintMargin: str
    initialMargin: str
    positionInitialMargin: str
    openOrderInitialMargin: str
    maxWithdrawAmount: str
    crossWalletBalance: str
    crossUnPnl: str
    availableBalance: str
    marginAvailable: bool
    updateTime: int


class AccountPositionsModel(pydantic.BaseModel):
    symbol: str
    initialMargin: str
    maintMargin: str
    unrealizedProfit: str
    positionInitialMargin: str
    openOrderInitialMargin: str
    leverage: str
    isolated: bool
    entryPrice: str
    maxNotional: str
    positionSide: str
    positionAmt: str
    notional: str
    isolatedWallet: str
    updateTime: int
    bidNotional: str
    askNotional: str


class AccountInformationModel(pydantic.BaseModel):
    feeTier: int
    canTrade: str
    canDeposit: str
    canWithdraw: str
    updateTime: int
    multiAssetsMargin: bool
    totalInitialMargin: str
    totalMaintMargin: str
    totalWalletBalance: str
    totalUnrealizedProfit: str
    totalMarginBalance: str
    totalPositionInitialMargin: str
    totalOpenOrderInitialMargin: str
    totalCrossWalletBalance: str
    totalCrossUnPnl: str
    availableBalance: str
    maxWithdrawAmount: str
    assets: list[AccountAssetsModel]
    positions: list[AccountPositionsModel]


class OrderModel(pydantic.BaseModel):
    orderId: int
    symbol: str
    status: str
    clientOrderId: str
    price: str
    avgPrice: str
    origQty: str
    executedQty: str
    cumQty: str
    cumQuote: str
    timeInForce: str
    type: str
    reduceOnly: bool
    closePosition: bool
    side: str
    positionSide: str
    stopPrice: str
    workingType: str
    priceProtect: bool
    origType: str
    updateTime: int
