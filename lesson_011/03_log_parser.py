# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
# пример использования:
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
# на консоли должно появится что-то вроде
# [2018-05-17 01:57] 1234
# TODO здесь ваш код
# class Log_parser:
#     def __init__(self, file_name, parser_log):
#         self.file_name = file_name
#         self.parser_log = parser_log
#         self.final_log={}
#     def parser(self):
#         with open(self.file_name,'r', encoding='utf8') as file:
#             with open(self.parser_log,'w', encoding='utf8') as parser_file:
#                 for line in file:
#                     if line[-4:-1] == 'NOK':
#                         if line[:17]+']' in self.final_log:
#                             self.final_log[line[:17]+']'] += 1
#                         else:
#                             self.final_log[line[:17]+']'] = 1
#                 for date, quantity in self.final_log.items():
#                     print(date,quantity)
#                     parser_file.write(f'{date}:{quantity}\n'.format(date=date,quantity=quantity))
#
# log_parser = Log_parser(file_name='events.txt', parser_log='parser_log.txt')
# log_parser.parser()
# Решено через генератор
def grouped_events(file_name):
    final_log = {}
    with open(file_name,'r', encoding='utf8') as file:
        for line in file:
            if line[-4:-1] == 'NOK':
                if line[:17]+']' in final_log:
                       final_log[line[:17]+']'] += 1
                else:
                       final_log[line[:17]+']'] = 1
        for date, quantity in final_log.items():
            yield date, quantity

test = grouped_events(file_name='events.txt')
for group_time, event_count in test:
    print(f'{group_time} : {event_count}')


