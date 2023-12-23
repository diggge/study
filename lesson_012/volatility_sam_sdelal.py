import os
import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate

path = 'C:/Users/user/study/lesson_012/trades'


class VolatilitySixxer:
    def __init__(self,path):
        self.path = path
        self.new_list, self.null_volatity = [], []

    def run(self):
        path_normalized = os.path.normpath(path=self.path)
        for dirpath, dirnames, filenames in os.walk(path_normalized):

            for file in filenames:
                with open(dirpath + "/" + file, 'r', encoding='utf8') as f:
                    my_list = []
                    for line in f:
                        key, value1, value2, value3 = line.split(',')
                        if key != 'SECID':
                            value2 = float(value2)
                            value3 = int(value3[:-1])
                            my_list.append([value2, value3])
                    min_list = min(my_list, key=lambda x: x[0])
                    max_list = max(my_list, key=lambda x: x[0])
                    average_price = round(((min_list[0] + max_list[0]) / 2), 2)
                    volatility = round(((max_list[0] - min_list[0]) / average_price) * 100, 2)
                    self.new_list.append([key, average_price, volatility])
        return self.new_list

    def sorted(self):
        self.new_list = sorted(self.new_list, key=lambda x: x[2])
        min_volatility = self.new_list[:3]
        max_volatility = self.new_list[-3:]
        print('минималная волатильность в бумагах: ', min_volatility)
        print('максимальная волатильность в бумагах: ', max_volatility)
        for i in self.new_list:
            if i[2] == 0:
                self.null_volatity.append(i)
        print('Нулевая волатильность  в бумагах:', self.null_volatity)


@time_track
def main():
    readers = [VolatilitySixxer(path=path)]
    for reader in readers:
        reader.run()
    for reader in readers:
        reader.sorted()

if __name__ == '__main__':
    main()
