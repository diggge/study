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

def some_func():
    print('Привет! Я функция')


# some_func()
#
my_list = [3, 14, 15, 92, 6]
for element in my_list:
    some_func()
