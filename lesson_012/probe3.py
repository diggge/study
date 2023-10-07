from urllib.request import Request,urlopen
from html.parser import HTMLParser
from html.entities import name2codepoint

import requests

sites = [
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://work-zilla.com/',
    'https://soccer.ru',
    'https://sports.ru'
]
class LinkExtractor(HTMLParser):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag not in ('link','script',):
            return
        attrs = dict(attrs)
        # print("Start tag", tag)
        if tag == 'link':
            if 'rel' in attrs and attrs['rel'] == 'stylesheet' and 'href' in attrs:
                self.links.append(attrs['href'])
            elif 'rel' in attrs and attrs['rel'] == 'stylesheet' and 'data-href' in attrs:
                self.links.append(attrs['data-href'])
        elif tag == 'script':
            if 'src' in attrs:
                self.links.append(attrs['src'])

class PagerSizer:
    def __init__(self,url):
        self.url = url
        self.total_bytes = 0
    def run(self):
        self.total_bytes = 0
        html_data = self.get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        extractor = LinkExtractor()
        extractor.feed(html_data)
        for link in extractor.links:
            exctra_data = self.get_html(url=link)
            if exctra_data is None:
                return
            self.total_bytes = + len(exctra_data)
    def get_html(self,url):
        try:
            res = requests.get(url)
        except Exception as exc:
            print(exc)
        else:
            return res.text

for url in sites:
    print(f'Go {url} ...')
    # res = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    sizer = PagerSizer(url=url)
    # res = requests.get(url)
    # html_data = res.text
    # html_data = html_data.decode('utf8')
    # total_bytes = len(html_data)
    # extractor = LinkExtractor()
    # extractor.feed(html_data)
    # print(html_data)
    # print(extractor.links)
    # for link in extractor.links:
    #     print(f'\t Go {link} ...')
    #     try:
    #         res = requests.get(link)
    #         # res = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    #
    #     except Exception as exc:
    #         print(exc)
    #     exctra_data = res.text
    #     total_bytes =+ len(exctra_data)
    sizer.run()
    print(f'For url {url} need download {sizer.total_bytes/1024} Kbytes')
