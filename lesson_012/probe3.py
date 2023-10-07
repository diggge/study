import time
from urllib.parse import urlsplit, urljoin
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

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate

class LinkExtractor(HTMLParser):
    def __init__(self, base_url,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.base_url = base_url
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag not in ('link','script',):
            return
        attrs = dict(attrs)
        # print("Start tag", tag)
        if tag == 'link':
            if 'rel' in attrs and attrs['rel'] == 'stylesheet' and 'href' in attrs:
                link = self._refine(attrs['href'])
                self.links.append(link)
            elif 'rel' in attrs and attrs['rel'] == 'stylesheet' and 'data-href' in attrs:
                link = self._refine(attrs['data-href'])
                self.links.append(link)
        elif tag == 'script':
            if 'src' in attrs:
                link = self._refine(attrs['src'])
                self.links.append(link)

    def _refine(self,link):
        # scheme, netloc, path, query, fragment = urlsplit(link)
        return urljoin(self.base_url, link)

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
        extractor = LinkExtractor(base_url=self.url)
        extractor.feed(html_data)
        for link in extractor.links:
            exctra_data = self.get_html(url=link)
            if exctra_data is None:
                return
            self.total_bytes = + len(exctra_data)
    def get_html(self,url):
        try:
            print(f'Go {url} ...')
            res = requests.get(url)
        except Exception as exc:
            print(exc)
        else:
            return res.text
@time_track
def main():
    sizers = [PagerSizer(url=url) for url in sites]
    for sizer in sizers:
        sizer.run()
    for sizer in sizers:
        print(f'For url {sizer.url} need download {round(sizer.total_bytes/1024,2)} Kbytes')

if __name__ == '__main__':
    main()