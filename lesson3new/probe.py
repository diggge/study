# print('дратути!')
# i=1
# while i<1000:
#     i=i*2
#     print(i)
# # print('Доствидания, i=',i)
# f1,f2=1,1
# print(f1)
# print(f2)
# while f2<1000:
#     next_f2=f1+f2
#     next_f1=f2
#     f1=next_f1
#     f2=next_f2
#     print(f2)
# print('дотвидания')

# my_pets = ['cat', 'dog', 'hamster']
# i = 0
# while i < len(my_pets):
#     pet = my_pets[i]
#     print('Проверяем ', pet)
#     if pet == 'cat':
#         print('Ура, кот найден!')
#         break
#     i += 1
# print('дотвиданя!')

# zoo_pets = [
#     'lion', 'monkey', 'skunk',
#     'elephant', 'horse',
# ]
# for i, animal in enumerate(zoo_pets):
#     print(i, animal)
# генерация целочисленных последовательностей
# for i in range(100, 600, 50):
#     print(i)
# вложенные циклы
# zoo_pets = [
#     'lion', 'skunk',
#     'elephant', 'horse',
# ]
# for animal in zoo_pets:
#     for char in animal:
#         print(char)
#     print(animal)
# цикл по словарям

# zoo_pet_mass = {
#     'lion': 300,
#     'skunk': 5,
#     'elephant': 5000,
#     'horse': 400,
# }
# print(zoo_pet_mass['lion'])
# total_mass = 0
# for animal in zoo_pet_mass:
#     print(animal, zoo_pet_mass[animal])
#     total_mass += zoo_pet_mass[animal]
# print('Общая масса животных', total_mass)
#
# total_mass = 0
# print(zoo_pet_mass.items())
# print(zoo_pet_mass.values())
# for animal, mass in zoo_pet_mass.items():
#     print(zoo_pet_mass.items())
#     print(animal, mass)
#     total_mass += mass
# print('Общая масса животных', total_mass)
# total_mass = 0
# for mass in zoo_pet_mass.values():
#     print(mass)
#     total_mass += mass
# print('Общая масса животных', total_mass)

# def some_func():
#     print('Привет! Я функция')
#
#
# # some_func()
# #
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     print(element)
#     some_func()
# def func_with_params(param):
#     print('Функцию вызвали с параметром=', param)
#
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     print('Начало цикла')
#     func_with_params(param=element)
#     print('Конец цикла')

# # возврат значения из функции
#
# def power(number, pow):
#     print('Функцию вызвали с параметрами', number, pow)
#     power_value = number ** pow
#     return power_value
#
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     result = power(element, 10)
#     print(result)
#
# for element in my_list:
#     result = power(number=element, pow=element)
#     print(result)
# def some_func():
#     print("я ничего не верну")
#
# result = some_func()
# print(result)

# можно возвращать несколько значений
# def create_default_user():
#     name = "Василий"
#     age = 27
#     return name, age
# user_name, use_age=create_default_user()
# print(user_name, use_age)
# print(create_default_user())
# динамическая типизация
# def multiplay(number_1, number_2):
#     print('Функцию вызвали с параметрами', number_1, number_2)
#     value = number_1 * number_2
#     return value
# print(multiplay(number_1=42, number_2=27))
# print(multiplay(number_1='привет! ', number_2=34))

# Параметры передаются как ссылка

def elephant_to_free(some_list):
    elephant_found = 'elephant' in some_list
    if elephant_found:
        some_list.remove('elephant')
        print('Слон на свободе!!!')
    return elephant_found


zoo = ['lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant']

elephant_to_free(some_list=tuple(zoo))
print(zoo)

elephant_to_free(zoo)
print(zoo)

elephant_to_free(zoo)
print(zoo)

# это т.н. функции с побочными эффектами, они меняют контекст выполнения.
# можно заблокировать изменение параметров - передать тьюпл
zoo = ('lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant')
elephant_to_free(zoo)
print(zoo)

