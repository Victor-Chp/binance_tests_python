from selene import browser, have, command
from projectcfg import BaseUrls

base_url = BaseUrls.perpetual_futures_testnet

class GeneralPageTestnet():
    def open(self):
        browser.open(base_url)