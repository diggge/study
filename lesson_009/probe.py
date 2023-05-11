# форматирование вывода строк - минимальная ширина поля {xxx:10}
phones = {'Bill': 4127, 'Jameson': 4098, 'Abraham': 7678}
for name, phone in phones.items():
    print('{name:10} ==> {phone:10d}'.format(name=name, phone=phone))