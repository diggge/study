import os


from utils import time_track


class VolatilityCalc:

    def __init__(self, filename, source):
        self.source = source
        self.filename = filename
        self.volatility, self.max_price, self.min_price = 0, 0, 0

    def _calculation_of_volatility(self, full_file_path):
        with open(full_file_path, 'r', encoding='utf8') as data:
            file_content = data.read().split('\n')
            # print(file_content)
            for line in file_content:
                if line != '':
                    price = line.split(',')[2]
                    if price != 'PRICE':
                        price = float(price)
                        if self.max_price != 0 and self.min_price != 0:
                            if price > self.max_price:
                                self.max_price = price
                            elif price < self.min_price:
                                self.min_price = price

                        else:
                            self.max_price, self.min_price = price, price

    def run(self):
        self.max_price, self.min_price = 0, 0
        full_file_path = os.path.join(self.source, self.filename)
        self._calculation_of_volatility(full_file_path=full_file_path)
        half_sum = (self.max_price + self.min_price) / 2
        self.volatility = round((self.max_price - self.min_price) * 100 / half_sum, 2)


@time_track
def main():
    # source = r'..\..\..\trades'
    source = r'trades'
    list_filenames = os.listdir(source)
    volatility_of_securities = [VolatilityCalc(filename=filename, source=source) for filename in list_filenames]
    result_vol = {}
    for security in volatility_of_securities:
        security.run()
        result_vol[security.filename] = security.volatility
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
    list_of_zero_volatility_list_filenames = []
    for i in sorted(result_vol.items(), key=lambda item: item[0]):
        if i[1] == 0:
            list_of_zero_volatility_list_filenames.append(i[0].split('.')[0])
    print(' ' * 4, ', '.join(list_of_zero_volatility_list_filenames))


if __name__ == '__main__':
    main()
# Зачет!