import multiprocessing

import requests
from extractor import LinkExtractor
from lesson_012.utils import time_track

sites = [
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://work-zilla.com/',
    'https://soccer.ru',
    'https://sports.ru'
]
class PagerSizer(multiprocessing.Process):
    def __init__(self, url, collector, go_ahead=True,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.url = url
        self.total_bytes = 0
        self.go_ahead = go_ahead
        self.collector = collector
    def run(self):
        self.total_bytes = 0
        html_data = self.get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        if self.go_ahead:
            extractor = LinkExtractor(base_url=self.url)
            extractor.feed(html_data)
            collector = multiprocessing.Queue()
            sizers = [PagerSizer(url=link,go_ahead=False, collector=collector) for link in extractor.links]
            for sizer in sizers:
                sizer.start()
            for sizer in sizers:
                sizer.join()
            while not collector.empty():
                data = collector.get()
                self.total_bytes += data['total_bytes']
            for sizer in sizers:
                self.total_bytes += sizer.total_bytes
        self.collector.put(dict(url=self.url, total_bytes=self.total_bytes))


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
    collector = multiprocessing.Queue()
    sizers = [PagerSizer(url=url,collector=collector) for url in sites]
    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()

    while not collector.empty():
        data = collector.get()
        print(f"For url {data['url']} need download {data['total_bytes']//1024} Kb ")

    for sizer in sizers:
        print(f'For url {sizer.url} need download {round(sizer.total_bytes/1024,2)} Kbytes')

if __name__ == '__main__':
    main()