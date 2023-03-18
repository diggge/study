while True:
    try:
        y = int(input('Напишите вариант четырехзначного числа c неповторяющимися цифрами :  '))
        if (1023< y < 10000 and y // 1000!= y // 100 % 10|| y // 10 % 10, y % 10):
            break
        else:
            raise ValueError()
    except ValueError:
        print("Ошибка! введенное число не отвечает требованиям")















# y // 1000, y // 100 % 10, y // 10 % 10, y % 10
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")