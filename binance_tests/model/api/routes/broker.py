import pydantic


class BrokerRoutes(pydantic.BaseModel):
    name = "Broker"

    subAccount: str = "sapi/v1/broker/subAccount"
    margin: str = "sapi/v1/broker/subAccount/margin"
    futures: str = "sapi/v1/broker/subAccountApi/commission/futures"
    subAccountApi: str = "sapi/v1/broker/subAccountApi"
    commission: str = "sapi/v1/broker/subAccountApi/commission"
    info: str = "sapi/v1/broker/info"
    transfer: str = "sapi/v1/broker/transfer"
    recentRecord: str = "sapi/v1/broker/rebate/recentRecord"
    historicalRecord: str = "sapi/v1/broker/rebate/historicalRecord"
    spot: str = "sapi/v1/broker/subAccount/bnbBurn/spot"
    marginInterest: str = "sapi/v1/broker/subAccount/bnbBurn/marginInterest"
    status: str = "sapi/v1/broker/subAccount/bnbBurn/status"
    depositHist: str = "sapi/v1/broker/subAccount/depositHist"
    spotSummary: str = "sapi/v1/broker/subAccount/spotSummary"
    marginSummary: str = "sapi/v1/broker/subAccount/marginSummary"
    futuresSummary: str = "sapi/v1/broker/subAccount/futuresSummary"
