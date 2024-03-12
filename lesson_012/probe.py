from html.parser import HTMLParser
from urllib.request import urlopen, Request

import requests

# from extractor import LinkExtractor
# from utils import time_track

sites = [
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://work-zilla.com/',
    # 'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
]
class LinkExtractor(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.links = []
    def handle_starttag(self,tag,attrs):
        if tag != 'link':
            return
        print("Start tag:",tag)
        if 'rel' in attrs and attrs['rel'] == 'stylesheet':
            self.links.append(attrs['href'])
        for attr in attrs:
            print("    attr:", attr)
for url in sites:
    req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    html_data = urlopen(req).read()
    html_data = html_data.decode('utf8', errors='ignore')
    total_bytes = len(html_data)
    extractor = LinkExtractor()
    extractor.feed(html_data)
    print(extractor.links)



