#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['papa', 'mama', 'dochka', 'cat']
print(my_family)

# список списков приблизителного роста членов вашей семьи
my_family_height = [['papa', 170],['mama',160],['dochka',120],['cat', 10]]
print(my_family_height)
    # ['имя', рост],


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('Рост отца -' , my_family_height[0][1], 'см')


# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
#my_test=[1,3,4]
#rint(sum(my_test))
print ('Общий рост семьи -',(my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]+my_family_height[3][1]) ,'см')