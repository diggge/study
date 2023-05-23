# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# TODO здесь ваш код
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import zipfile
from pprint import pprint


class Statistika:
    def __init__(self,file_name):
        self.file_name = file_name
        self.stat = {}
    def unzip(self):
        zfile=zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename
    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        # self.sequence = ' ' * self.analize_count
        with open(self.file_name,'r', encoding='cp1251') as file:
            for line in file:
                # print(line, end='')
                for char in line:
                    if char in line:
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            if (char.isalpha() is True and ord(char)>128):
                                self.stat[char] = 1
            print('{line0:^22} '.format(line0='+-----------+-----------+'))
            print('|{first_line1:^10} | {first_line2:^10}|'.format(first_line1='Буква',first_line2='Частота'))
            print('{line2:^22} '.format(line2='+-----------+-----------+'))
            # print(dict(sorted(self.stat.items(), key=lambda x: x[1])))
            # sorted(self.stat.items()):
            stat_sort= dict(sorted(self.stat.items(), reverse=False , key=lambda x: x[0]))
            # для сортировки по алфавиту или по значениям, меняем x[0] или x[1], убывание или возрастание меняем reverse=false or true
            for alphabet,quantity in stat_sort.items():
                print('|{alphabet:^10} | {quantity:^10}|'.format(alphabet=alphabet,quantity=quantity))
            print('{line999:^22} '.format(line999='+-----------+-----------+'))
            print('|{line1000:^10} | {summa:^10}|'.format(line1000='Итого', summa=sum(self.stat.values())))
            print('{linefinal:^22} '.format(linefinal='+-----------+-----------+'))

# print('|{txt:^30}|'.format(txt='centered'))
# # '           centered
statistika=Statistika(file_name='python_snippets/voyna-i-mir.txt.zip')
statistika.collect()




