# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from district.central_street.house1.room1 import folks as folks_CS_h1_r1
from district.central_street.house1.room2 import folks as folks_CS_h1_r2
from district.central_street.house2.room1 import folks as folks_CS_h2_r1
from district.central_street.house2.room2 import folks as folks_CS_h2_r2
from district.soviet_street.house1.room1 import folks as folks_SS_h1_r1
from district.soviet_street.house1.room1 import folks as folks_SS_h1_r2
from district.soviet_street.house2.room1 import folks as folks_SS_h2_r1
from district.soviet_street.house2.room1 import folks as folks_SS_h2_r2
folks=folks_CS_h1_r1+folks_CS_h1_r2+folks_CS_h2_r1+folks_CS_h2_r2+folks_SS_h1_r1+folks_SS_h1_r2+folks_SS_h2_r1+folks_SS_h2_r2
print('На районе живут (1 вариант)',folks)
folks_str=",".join(folks)
print('На районе живут (2 вариант)',folks_str)




