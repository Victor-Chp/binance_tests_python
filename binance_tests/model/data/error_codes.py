import pydantic


class ErrorCodes(pydantic.BaseModel):
    code_1022: dict = {'code': -1022, 'msg': 'Signature for this request is not valid.'}
    code_2014: dict = {"code": -2014, "msg": "API-key format invalid."}


