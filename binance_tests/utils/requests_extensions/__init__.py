from binance_tests.utils.requests_extensions.session_with_allure import CustomSession

# TODO: should we create a separate session for each request?
#       like it is done inside original requests library
requests = CustomSession()
