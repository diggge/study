# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
class Log_parser:
    def __init__(self, file_name, parser_log):
        self.file_name = file_name
        self.parser_log = parser_log
        self.final_log={}
    def parser(self):
        with open(self.file_name,'r', encoding='utf8') as file:
            with open(self.parser_log,'w', encoding='utf8') as parser_file:
                for line in file:
                    if line[-4:-1] == 'NOK':
                        if line[:14]+']' in self.final_log:
                            self.final_log[line[:14]+']'] += 1
                        else:
                            self.final_log[line[:14]+']'] = 1
                for date,quantity in self.final_log.items():
                    print(date,quantity)
                    parser_file.write(f'{date}:{quantity}\n'.format(date=date,quantity=quantity))

log_parser=Log_parser(file_name='events.txt', parser_log='parser_log.txt')
log_parser.parser()
