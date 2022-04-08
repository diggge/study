#!/usr/bin/env python
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

for gooditem in goods.items():
    costitem = 0
    quantityitem = 0
    itemname = gooditem[0]
    l =-1;
    for storeitem in store.items():
        l = l+1
        if storeitem[0]==gooditem[1]:
            s = storeitem[1].copy()
            # print(s);
            for asd in s:
                print(asd.values()[1])
            # print(storeitem[1])
            # s = {}.copy(storeitem[1])
            #     print(storeitem2)
            #     print(storeitem[0])

    print(itemname, quantityitem, 'шт, стоимость', costitem, 'руб')

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
stol_code = goods['Стол']
stol_item1 = store[stol_code][0]
stol_quantity1 = stol_item1['quantity']
stol_price1 = stol_item1['price']
stol_item2 = store[stol_code][1]
stol_quantity2 = stol_item2['quantity']
stol_price2 = stol_item2['price']
stol_cost = stol_quantity1 * stol_price1+stol_quantity2 * stol_price2
print('Стол -', (stol_quantity1+stol_quantity2), 'шт, стоимость', stol_cost, 'руб')
divan_code = goods['Диван']
divan_item1 = store[divan_code][0]
divan_quantity1 = divan_item1['quantity']
divan_price1 = divan_item1['price']
divan_item2 = store[divan_code][1]
divan_quantity2 = divan_item2['quantity']
divan_price2 = divan_item2['price']
divan_cost = divan_quantity1 * divan_price1+divan_quantity2 * divan_price2
print('Диван -', (divan_quantity1+divan_quantity2), 'шт, стоимость', divan_cost, 'руб')

divan_code = goods['Диван']
divan_item1 = store[divan_code][0]
divan_quantity1 = divan_item1['quantity']
divan_price1 = divan_item1['price']
divan_item2 = store[divan_code][1]
divan_quantity2 = divan_item2['quantity']
divan_price2 = divan_item2['price']
divan_cost = divan_quantity1 * divan_price1+divan_quantity2 * divan_price2
print('Диван -', (divan_quantity1+divan_quantity2), 'шт, стоимость', divan_cost, 'руб')


stul_code = goods['Стул']
stul_item1 = store[stul_code][0]
stul_quantity1 = stul_item1['quantity']
stul_price1 = stul_item1['price']
stul_item2 = store[stul_code][1]
stul_quantity2 = stul_item2['quantity']
stul_price2 = stul_item2['price']
stul_item3 = store[stul_code][2]
stul_quantity3 = stul_item3['quantity']
stul_price3 = stul_item3['price']
stul_cost = stul_quantity1 * stul_price1+stul_quantity2 * stul_price2+stul_quantity3 * stul_price3
print('Стул -', (stul_quantity1+stul_quantity2+stul_quantity3), 'шт, стоимость', stul_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код






##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






