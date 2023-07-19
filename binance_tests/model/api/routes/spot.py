import pydantic


class BLVTRoutes(pydantic.BaseModel):
    name = "Spot - BLVT"

    tokenInfo: str = "sapi/v1/blvt/tokenInfo"
    subscribe: str = "sapi/v1/blvt/subscribe"
    record: str = "sapi/v1/blvt/redeem/record"
    redeem: str = "sapi/v1/blvt/redeem"
    userLimit: str = "sapi/v1/blvt/userLimit"


class BSwapRoutes(pydantic.BaseModel):
    name = "Spot - BSwap"

    pools: str = "sapi/v1/bswap/pools"
    liquidity: str = "sapi/v1/bswap/liquidity"
    liquidityAdd: str = "sapi/v1/bswap/liquidityAdd"
    liquidityRemove: str = "sapi/v1/bswap/liquidityRemove"
    liquidityOps: str = "sapi/v1/bswap/liquidityOps"
    quote: str = "sapi/v1/bswap/quote"
    swap: str = "sapi/v1/bswap/swap"
    poolConfigure: str = "sapi/v1/bswap/poolConfigure"
    addLiquidityPreview: str = "sapi/v1/bswap/addLiquidityPreview"
    removeLiquidityPreview: str = "sapi/v1/bswap/removeLiquidityPreview"
    unclaimedRewards: str = "sapi/v1/bswap/unclaimedRewards"
    claimRewards: str = "sapi/v1/bswap/claimRewards"
    claimedHistory: str = "sapi/v1/bswap/claimedHistory"


class C2CRoutes(pydantic.BaseModel):
    name = "Spot - C2C"

    listUserOrderHistory: str = "sapi/v1/c2c/orderMatch/listUserOrderHistory"


class ConvertRoutes(pydantic.BaseModel):
    name = "Spot - Convert"

    exchangeInfo: str = "sapi/v1/convert/exchangeInfo"
    assetInfo: str = "sapi/v1/convert/assetInfo"
    getQuote: str = "sapi/v1/convert/getQuote"
    acceptQuote: str = "sapi/v1/convert/acceptQuote"
    orderStatus: str = "sapi/v1/convert/orderStatus"
    tradeFlow: str = "sapi/v1/convert/tradeFlow"


class CryptoLoansRoutes(pydantic.BaseModel):
    name = "Spot - CryptoLoans"

    income: str = "sapi/v1/loan/income"
    borrow: str = "sapi/v1/loan/borrow"
    history: str = "sapi/v1/loan/ltv/adjustment/history"
    orders: str = "sapi/v1/loan/ongoing/orders"
    repay: str = "sapi/v1/loan/repay"
    ltv: str = "sapi/v1/loan/adjust/ltv"
    data: str = "sapi/v1/loan/collateral/data"
    rate: str = "sapi/v1/loan/repay/collateral/rate"
    margin_call: str = "sapi/v1/loan/customize/margin_call"


class FiatRoutes(pydantic.BaseModel):
    name = "Spot - Fiat"

    orders: str = "sapi/v1/fiat/orders"
    payments: str = "sapi/v1/fiat/payments"


class FuturesRoutes(pydantic.BaseModel):
    name = "Spot - Futures"

    transfer: str = "sapi/v1/futures/transfer"
    history: str = "sapi/v1/futures/loan/adjustCollateral/history"
    wallet: str = "sapi/v2/futures/loan/wallet"
    liquidationHistory: str = "sapi/v1/futures/loan/liquidationHistory"
    interestHistory: str = "sapi/v1/futures/loan/interestHistory"


class FuturesAlgoRoutes(pydantic.BaseModel):
    name = "Spot - FuturesAlgo"

    newOrderVp: str = "sapi/v1/algo/futures/newOrderVp"
    newOrderTwap: str = "sapi/v1/algo/futures/newOrderTwap"
    order: str = "sapi/v1/algo/futures/order"
    openOrders: str = "sapi/v1/algo/futures/openOrders"
    historicalOrders: str = "sapi/v1/algo/futures/historicalOrders"
    subOrders: str = "sapi/v1/algo/futures/subOrders"


class GiftCardRoutes(pydantic.BaseModel):
    name = "Spot - GiftCard"

    createCode: str = "sapi/v1/giftcard/createCode"
    redeemCode: str = "sapi/v1/giftcard/redeemCode"
    buyCode: str = "sapi/v1/giftcard/buyCode"
    verify: str = "sapi/v1/giftcard/verify"
    token_limit: str = "sapi/v1/giftcard/buyCode/token-limit"
    rsa_public_key: str = "sapi/v1/giftcard/cryptography/rsa-public-key"


class MarginRoutes(pydantic.BaseModel):
    name = "Spot - Margin"

    transfer: str = "sapi/v1/margin/isolated/transfer"
    loan: str = "sapi/v1/margin/loan"
    repay: str = "sapi/v1/margin/repay"
    asset: str = "sapi/v1/margin/asset"
    pair: str = "sapi/v1/margin/isolated/pair"
    allAssets: str = "sapi/v1/margin/allAssets"
    allPairs: str = "sapi/v1/margin/isolated/allPairs"
    priceIndex: str = "sapi/v1/margin/priceIndex"
    order: str = "sapi/v1/margin/rateLimit/order"
    interestHistory: str = "sapi/v1/margin/interestHistory"
    forceLiquidationRec: str = "sapi/v1/margin/forceLiquidationRec"
    account: str = "sapi/v1/margin/isolated/account"
    openOrders: str = "sapi/v1/margin/openOrders"
    allOrders: str = "sapi/v1/margin/allOrders"
    oco: str = "sapi/v1/margin/order/oco"
    orderList: str = "sapi/v1/margin/orderList"
    allOrderList: str = "sapi/v1/margin/allOrderList"
    openOrderList: str = "sapi/v1/margin/openOrderList"
    myTrades: str = "sapi/v1/margin/myTrades"
    maxBorrowable: str = "sapi/v1/margin/maxBorrowable"
    maxTransferable: str = "sapi/v1/margin/maxTransferable"
    tradeCoeff: str = "sapi/v1/margin/tradeCoeff"
    accountLimit: str = "sapi/v1/margin/isolated/accountLimit"
    bnbBurn: str = "sapi/v1/bnbBurn"
    interestRateHistory: str = "sapi/v1/margin/interestRateHistory"
    crossMarginData: str = "sapi/v1/margin/crossMarginData"
    isolatedMarginData: str = "sapi/v1/margin/isolatedMarginData"
    isolatedMarginTier: str = "sapi/v1/margin/isolatedMarginTier"
    dribblet: str = "sapi/v1/margin/dribblet"


class MarketRoutes(pydantic.BaseModel):
    name = "Spot - Market"

    ping: str = "api/v3/ping"
    time: str = "api/v3/time"
    exchangeInfo: str = "api/v3/exchangeInfo"
    depth: str = "api/v3/depth"
    trades: str = "api/v3/trades"
    historicalTrades: str = "api/v3/historicalTrades"
    aggTrades: str = "api/v3/aggTrades"
    klines: str = "api/v3/klines"
    uiKlines: str = "api/v3/uiKlines"
    avgPrice: str = "api/v3/avgPrice"
    _24hr: str = "api/v3/ticker/24hr"
    price: str = "api/v3/ticker/price"
    bookTicker: str = "api/v3/ticker/bookTicker"
    ticker: str = "api/v3/ticker"


class MiningRoutes(pydantic.BaseModel):
    name = "Spot - Mining"

    algoList: str = "sapi/v1/mining/pub/algoList"
    coinList: str = "sapi/v1/mining/pub/coinList"
    detail: str = "sapi/v1/mining/worker/detail"
    list: str = "sapi/v1/mining/statistics/user/list"
    other: str = "sapi/v1/mining/payment/other"
    details: str = "sapi/v1/mining/hash-transfer/profit/details"
    config: str = "sapi/v1/mining/hash-transfer/config"
    cancel: str = "sapi/v1/mining/hash-transfer/config/cancel"
    status: str = "sapi/v1/mining/statistics/user/status"
    uid: str = "sapi/v1/mining/payment/uid"


class NFTRoutes(pydantic.BaseModel):
    name = "Spot - NFT"

    transactions: str = "sapi/v1/nft/history/transactions"
    deposit: str = "sapi/v1/nft/history/deposit"
    withdraw: str = "sapi/v1/nft/history/withdraw"
    getAsset: str = "sapi/v1/nft/user/getAsset"


class PayRoutes(pydantic.BaseModel):
    name = "Spot - Pay"

    transactions: str = "sapi/v1/pay/transactions"


class PortfolioMarginRoutes(pydantic.BaseModel):
    name = "Spot - PortfolioMargin"

    account: str = "sapi/v1/portfolio/account"
    collateralRate: str = "sapi/v1/portfolio/collateralRate"
    pmLoan: str = "sapi/v1/portfolio/pmLoan"
    repay: str = "sapi/v1/portfolio/repay"


class RebateRoutes(pydantic.BaseModel):
    name = "Spot - Rebate"

    taxQuery: str = "sapi/v1/rebate/taxQuery"


class SavingsRoutes(pydantic.BaseModel):
    name = "Spot - Savings"

    list: str = "sapi/v1/lending/project/position/list"
    userLeftQuota: str = "sapi/v1/lending/daily/userLeftQuota"
    purchase: str = "sapi/v1/lending/customizedFixed/purchase"
    userRedemptionQuota: str = "sapi/v1/lending/daily/userRedemptionQuota"
    redeem: str = "sapi/v1/lending/daily/redeem"
    position: str = "sapi/v1/lending/daily/token/position"
    account: str = "sapi/v1/lending/union/account"
    purchaseRecord: str = "sapi/v1/lending/union/purchaseRecord"
    redemptionRecord: str = "sapi/v1/lending/union/redemptionRecord"
    interestHistory: str = "sapi/v1/lending/union/interestHistory"
    positionChanged: str = "sapi/v1/lending/positionChanged"


class StakingRoutes(pydantic.BaseModel):
    name = "Spot - Staking"

    productList: str = "sapi/v1/staking/productList"
    purchase: str = "sapi/v1/staking/purchase"
    redeem: str = "sapi/v1/staking/redeem"
    position: str = "sapi/v1/staking/position"
    stakingRecord: str = "sapi/v1/staking/stakingRecord"
    setAutoStaking: str = "sapi/v1/staking/setAutoStaking"
    personalLeftQuota: str = "sapi/v1/staking/personalLeftQuota"


class SubAccountRoutes(pydantic.BaseModel):
    name = "Spot - SubAccount"

    virtualSubAccount: str = "sapi/v1/sub-account/virtualSubAccount"
    list: str = "sapi/v1/sub-account/list"
    history: str = "sapi/v1/sub-account/sub/transfer/history"
    internalTransfer: str = "sapi/v1/sub-account/futures/internalTransfer"
    assets: str = "sapi/v3/sub-account/assets"
    spotSummary: str = "sapi/v1/sub-account/spotSummary"
    subAddress: str = "sapi/v1/capital/deposit/subAddress"
    subHisrec: str = "sapi/v1/capital/deposit/subHisrec"
    status: str = "sapi/v1/sub-account/status"
    enable: str = "sapi/v1/sub-account/blvt/enable"
    account: str = "sapi/v2/sub-account/futures/account"
    accountSummary: str = "sapi/v2/sub-account/futures/accountSummary"
    positionRisk: str = "sapi/v2/sub-account/futures/positionRisk"
    transfer: str = "sapi/v1/sub-account/margin/transfer"
    subToSub: str = "sapi/v1/sub-account/transfer/subToSub"
    subToMaster: str = "sapi/v1/sub-account/transfer/subToMaster"
    subUserHistory: str = "sapi/v1/sub-account/transfer/subUserHistory"
    universalTransfer: str = "sapi/v1/sub-account/universalTransfer"
    deposit: str = "sapi/v1/managed-subaccount/deposit"
    asset: str = "sapi/v1/managed-subaccount/asset"
    withdraw: str = "sapi/v1/managed-subaccount/withdraw"
    accountSnapshot: str = "sapi/v1/managed-subaccount/accountSnapshot"
    ipRestriction: str = "sapi/v2/sub-account/subAccountApi/ipRestriction"
    ipList: str = "sapi/v1/sub-account/subAccountApi/ipRestriction/ipList"
    thirdPartyList: str = "sapi/v1/sub-account/apiRestrictions/ipRestriction/thirdPartyList"


class TradeRoutes(pydantic.BaseModel):
    name = "Spot - Trade"

    test: str = "api/v3/order/test"
    order: str = "api/v3/rateLimit/order"
    cancelReplace: str = "api/v3/order/cancelReplace"
    openOrders: str = "api/v3/openOrders"
    allOrders: str = "api/v3/allOrders"
    oco: str = "api/v3/order/oco"
    orderList: str = "api/v3/orderList"
    allOrderList: str = "api/v3/allOrderList"
    openOrderList: str = "api/v3/openOrderList"
    account: str = "api/v3/account"
    myTrades: str = "api/v3/myTrades"


traderoutes = TradeRoutes()


class UserDataStreamRoutes(pydantic.BaseModel):
    name = "Spot - UserDataStream"

    userDataStream: str = "sapi/v1/userDataStream"
    isolated: str = "sapi/v1/userDataStream/isolated"


class WalletRoutes(pydantic.BaseModel):
    name = "Spot - Wallet"

    status: str = "sapi/v1/account/status"
    getall: str = "sapi/v1/capital/config/getall"
    accountSnapshot: str = "sapi/v1/accountSnapshot"
    disableFastWithdrawSwitch: str = "sapi/v1/account/disableFastWithdrawSwitch"
    enableFastWithdrawSwitch: str = "sapi/v1/account/enableFastWithdrawSwitch"
    apply: str = "sapi/v1/capital/withdraw/apply"
    hisrec: str = "sapi/v1/capital/deposit/hisrec"
    history: str = "sapi/v1/capital/withdraw/history"
    address: str = "sapi/v1/capital/deposit/address"
    apiTradingStatus: str = "sapi/v1/account/apiTradingStatus"
    dribblet: str = "sapi/v1/asset/dribblet"
    dust_btc: str = "sapi/v1/asset/dust-btc"
    dust: str = "sapi/v1/asset/dust"
    assetDividend: str = "sapi/v1/asset/assetDividend"
    assetDetail: str = "sapi/v1/asset/assetDetail"
    tradeFee: str = "sapi/v1/asset/tradeFee"
    transfer: str = "sapi/v1/asset/transfer"
    get_funding_asset: str = "sapi/v1/asset/get-funding-asset"
    getUserAsset: str = "sapi/v3/asset/getUserAsset"
    apiRestrictions: str = "sapi/v1/account/apiRestrictions"
    convert_transfer: str = "sapi/v1/asset/convert-transfer"
    queryByPage: str = "sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage"


class VIPLoansRoutes(pydantic.BaseModel):
    name = "Spot - VIPLoans"

    orders: str = "sapi/v1/loan/vip/ongoing/orders"
    repay: str = "sapi/v1/loan/vip/repay"
    history: str = "sapi/v1/loan/vip/repay/history"
    account: str = "sapi/v1/loan/vip/collateral/account"
