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

def chek_number():
    a,b,c,d=1,2,3,4
    i,j,k,l=1,4,6,5
    spisok_1=[a,b,c,d]
    spisok_2=[i,j,k,l]
    bulls,cows=0,0
    for g in spisok_1:
        for h in spisok_2:
            if g==h:
                bulls=bulls+1

        # if spisok_1[g]==spisok_2[g]:
        #     bulls+=bulls
    #     for h in spisok_2:
    #         if spisok_2[h]=spisok_1[g]:
    #             cows+=cows
    print(spisok_1,spisok_2)
    print(bulls,cows)
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
chek_number()

