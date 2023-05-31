def get_multiplier_v2(n):

    def multiplier(x):
        return x * n

    return multiplier

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_5 = get_multiplier_v2(5)
print(by_5(my_numbers))

result = map(by_5, my_numbers)
print(list(result))

by_100 = get_multiplier_v2(100)
result = map(by_100, my_numbers)
print(list(result))