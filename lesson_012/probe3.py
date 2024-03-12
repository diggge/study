import os

import threading
from collections import defaultdict


class VolatilityCalc(threading.Thread):

    def __init__(self, SECID, sourse, lock, results, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sourse = sourse
        self.filename = SECID
        self.volatility, self.max_price, self.min_price = 0, 0, 0
        self.lock = lock
        self.results = results

    def _calculation_of_volatility(self, full_file_path):
        with open(full_file_path, 'r', encoding='cp1251') as data:
            file_content = data.read().split('\n')
            for line in file_content:
                if line != '':
                    price = line.split(',')[2]
                    if price != 'PRICE':
                        price = float(price)
                        if self.max_price != 0 and self.max_price != 0:
                            if price > self.max_price:
                                self.max_price = price
                            elif price < self.min_price:
                                self.min_price = price

                        else:
                            self.max_price, self.min_price = price, price

    def run(self):
        self.max_price, self.min_price = 0, 0
        full_file_path = os.path.join(self.sourse, self.filename)
        self._calculation_of_volatility(full_file_path=full_file_path)
        half_sum = (self.max_price + self.min_price) / 2
        self.volatility = round((self.max_price - self.min_price) * 100 / half_sum, 2)
        with self.lock:
            self.results[self.filename] = self.volatility


result_vol = defaultdict(int)
sourse = r'trades'
SECIDS = os.listdir(sourse)
lock = threading.Lock()
volatility_of_securities = [
    VolatilityCalc(SECID=SECID, sourse=sourse, lock=lock, results=result_vol) for SECID in SECIDS]
for security in volatility_of_securities:
    security.start()
for security in volatility_of_securities:
    security.join()

print('Максимальная волатильность:')
first_free_max = {}
counter = 0
number_of_max_and_min_volatility_numbers = 3
for max_num in sorted(result_vol.items(), key=lambda item: item[1], reverse=True):
    first_free_max[max_num[0]] = max_num[1]
    counter += 1
    if counter == number_of_max_and_min_volatility_numbers:
        break
for key, item in sorted(first_free_max.items(), key=lambda item: item[1]):
    print(' ' * 4, key.split('.')[0], '-', item, '%')

print('Минимальная волатильность:')
counter = 0
for min_num in sorted(result_vol.items(), key=lambda item: item[1]):
    if min_num[1] != 0:
        if counter == number_of_max_and_min_volatility_numbers:
            break
        print(' ' * 4, min_num[0].split('.')[0], '-', min_num[1], '%')
        counter += 1

print('Нулевая волатильность:')
list_of_zero_volatility_secids = []
for i in sorted(result_vol.items(), key=lambda item: item[0]):
    if i[1] == 0:
        list_of_zero_volatility_secids.append(i[0].split('.')[0])
print(' ' * 4, ', '.join(list_of_zero_volatility_secids))
# Зачет!