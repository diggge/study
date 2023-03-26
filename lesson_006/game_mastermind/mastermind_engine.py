from random import randint
def think_a_number():
    a=randint(1,9)
    b=randint(0,9)
    for _ in range(1):
        if b!=a:
            break
        else:
            b=randint(0,9)
    c=randint(0,9)
    for _ in range(2):
        if (c!=a and c!=b):
            break
        else:
            c=randint(0,9)
    d = randint(0, 9)
    for _ in range(2):
        if (d != a and d != b and d != c):
            break
        else:
            d = randint(0, 9)
    return 1000*a+100*b+10*c+d
    #   загадать_число()
def chek_number(x,y):
    global bulls, cows
    spisok_1=[x // 1000, x // 100 % 10, x // 10 % 10, x % 10]
    spisok_2=[y // 1000, y // 100 % 10, y // 10 % 10, y % 10]
    bulls,cows=0,0
    g,h=0,0
    for g in range(4):
        if spisok_1[g] == spisok_2[g]:
            bulls +=1
            g+=1
        else:
            for h in range(4):
                if spisok_1[g]==spisok_2[h]:
                    cows +=1
                    h +=1
    dict_check = {'bulls': bulls, 'cows': cows}
    print('Количество быков =',dict_check['bulls'], 'Количество коров = ', dict_check['cows'])

# chek_number(7406,7459)
def is_gameover():
    return bulls == 4
print("жоп жоп")
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.

