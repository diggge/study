user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
if type(month) == int or float:
    print(type(month))
    print('целое число')
else:
    print('не целое число')