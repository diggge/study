# -*- coding: utf-8 -*-
# Есть словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
# Есть словарь списков количества товаров на складе.
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
# Рассчитать на какую сумму лежит каждого товара на складе.
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
# Алгоритм должен получиться приблизительно такой:
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе
# TODO здесь ваш код
# print(goods['Лампа'])                               12345
# print(store['12345'])                               [{'quantity': 27, 'price': 42}]
# print(store[goods['Лампа']])                        [{'quantity': 27, 'price': 42}]
# print(store[goods['Лампа']][0]['quantity'])         27
# print(store[goods['Лампа']][0]['price'])            42
for tovar in goods:
    total_sum=0
    total_quantity = 0
    for i in store[goods[tovar]]:
        quantity=i['quantity']
        price=i['price']
        total_quantity=total_quantity+quantity
        total_sum = total_sum + price*quantity
    print('Товара',tovar,'Количество товаров =',total_quantity,'На общую сумму =',total_sum,'рублей')
    #     quantity+=store[goods[tovar]]['quantity']
    #     print(quantity)
    #     print(len(store[goods[tovar]]))g





