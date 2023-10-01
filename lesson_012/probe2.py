from urllib.request import Request,urlopen
from html.parser import HTMLParser
from html.entities import name2codepoint

import requests

sites = [
    'https://www.fl.ru',
    # 'https://www.weblancer.net/',
    # 'https://www.freelancejob.ru/',
    # 'https://kwork.ru',
    # 'https://work-zilla.com/',
    # 'https://soccer.ru',
    # 'https://sports.ru'
]
class Link_extractor(HTMLParser):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.links = []
    def handle_starttag(self, tag,attrs):
        if tag != 'link':
            return
        attrs = dict(attrs)
        if 'rel' in attrs and attrs['rel'] == 'stylesheet':
            self.links.append('href')


for url in sites:
    res = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    # res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    # res = requests.get()
    html_data = urlopen(res).read()
    html_data = html_data.decode('utf8')
    total_bytes = len(html_data)
    extractor = Link_extractor()
    extractor.feed(html_data)
    print(extractor.links)
