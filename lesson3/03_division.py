# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 17456456459, 34567

# TODO здесь ваш код
print(a//b)
c=0
while c<a:
    c=c+1
    if c*b > a:
        print(c-1)
        break
