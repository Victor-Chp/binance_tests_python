import pydantic as original
from pydantic import *  # noqa


class BaseModel(original.BaseModel):
    @classmethod
    def assert_(cls, json):
        obj = cls(**json)
        # TODO: support validation of nested models that are list[NestedModel]
        #       use for loop over __annotations__
        #       from https://github.com/yashaka/selene/blob/6e4dc073c2ca74425ca4f6e25afdbcd315bba1d3/examples/run_remote_in_ios_safari_with_options_for_browserstack/test_todomvc.py#L33
