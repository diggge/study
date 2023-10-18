import requests

from extractor import LinkExtractor
from utils import time_track

sites = [
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://work-zilla.com/',
    'https://soccer.ru',
    'https://sports.ru'
]


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