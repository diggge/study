# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
# Сделано
# class PrimeNumbers:
#     def __init__(self,n):
#         self.i, self.j,  self.n = 1, 1, n
#     def __iter__(self):
#         self.i, self.j = 1, 1
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > 1:
#             if self.i > self.n:
#                 raise StopIteration()
#             for self.j in range(2, self.i):
#                 if self.i % self.j == 0:
#                     break
#                 else:
#                     return self.i
#     # TODO здесь ваш код
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     if number is not None:
#         print(number)



# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик
# Вторую часть сделал
# def prime_numbers_generator(n):
#     # TODO здесь ваш код
#     # i=2
#     for number in range(2,n+1):
#         for i in range(2,number):
#             if number % i == 0:
#                 break
#         else:
#             yield number
#
# for number in prime_numbers_generator(n=10000):
#     print(number)
#
#
# # Часть 3
# # Написать несколько функций-фильтров, которые выдает True, если число:
# # 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
# #       Если число имеет нечетное число цифр (например 727 или 92083),
# #       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
# #           727 -> 7(2)7 -> 7 == 7 -> True
# #           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# # 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# # 3) придумать свою (https://clck.ru/GB5Fc в помощь)
# #
# # Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# # для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# # простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
# #
# # Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
# Через итератор
# n = int(input("Введите число:"))
# i=len(str(n))
# j=i//2
# summa_left = 0
# summa_right = 0
# for k in range(1,j+1):
#     summa_left += (n % 10**i) // 10**(i-1)
#     summa_right += (n % 10**j) // 10**(j-1)
#     i -= 1
#     j -= 1
# if summa_left==summa_right:
#     print(f'{n}: Счастливое число')
# else:
#     print(f'{n}: Несчатсливое число')

class Lucky_numbers:
    def __init__(self, N):
        self.i, self.N = 121, N
        summa_left = summa_right = 0
    def __iter__(self):
        self.i = 121
        summa_left = summa_right = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.N:
            raise StopIteration()
        self.k = len(str(self.i))
        self.j = self.k // 2
        for _ in range(1,self.j+1):
            summa_left += (self.N % 10**self.k) // 10**(self.k-1)
            summa_right += (self.N % 10**self.j) // 10**(self.j-1)
            self.k -= 1
            self.j -= 1

        if summa_left == summa_left:
            return self.i


test=Lucky_numbers(N=1235)
for number in test:
    print(number)




