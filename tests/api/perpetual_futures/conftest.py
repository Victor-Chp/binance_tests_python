import pydantic
import pytest


class Config(pydantic.BaseSettings):
    base_url: str = 'https://testnet.binancefuture.com'


config = Config()


@pytest.fixture(scope='function', autouse=True)
def requests_management():
    base_url = config.base_url

    yield

    ...
