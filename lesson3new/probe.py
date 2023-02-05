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

f1, f2, count = 0, 1, 0
while f2 < 10000:
    count += 1
    if count > 27:
        print('Число итераций больше 27, выхожу')
        break
    f1, f2 = f2, f1 + f2
    if f2 < 10:
        continue
    print(f2)
else:
    print('было', count, 'итераций')
