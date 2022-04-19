user_input = input("Введите, пожалуйста, номер месяца: ")
try:
    month = int(user_input)
    print('Вы ввели', month)
except ValueError:
    print('Ошибка, Вы вели не целое число')



