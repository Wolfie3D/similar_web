from .browser import Browser
from .pages import Pages


class DataModule:
    def __init__(self):
        self.browser = Browser()
        self.pages = Pages()

    def get_data(self, url):
        fields = {}
        self.browser.make_domain(url)
        response = self.browser.get_data_from_api()
        return self.pages.parse_data(response, fields)
