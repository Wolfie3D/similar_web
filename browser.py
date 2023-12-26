import requests
from urllib.parse import urlparse
import datetime
import json


class Browser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'authority': 'data.similarweb.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'none',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'X-Extension-Version': '6.9.0'
        })
        self.countries = {}
        self.domain = None
        self.url = None

    def make_domain(self, url):
        self.url = url
        parsed = urlparse(url)
        self.domain = parsed.netloc
        print("Running for:", self.domain)

    def get_data_from_api(self):
        response = self.session.get(
            'https://data.similarweb.com/api/v1/data', params={'domain': self.domain})
        return response

    def country_name(self, country_code):
        if not self.countries:
            with open('countries.json') as file:
                self.countries = json.load(file)
        return self.countries.get(country_code, country_code)

    def strip_category(self, category):
        if category:
            return category.replace('_', ' ').replace('/', ' > ')

    def get_perc(self, numb):
        if numb:
            return str(round(float(numb) * 100, 2))
        return '0'

    def get_duration(self, seconds):
        if seconds:
            return datetime.timedelta(seconds=float(seconds))
