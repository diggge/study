from random import random,randint
x=[]
y=[]
massiv=[]
finish=[]
for i in range(10):
    x.append(randint(0,10))
    y.append(randint(10,20))
    massiv.append([i,x[i],y[i]])
print(massiv)
for i in range(10):
    if x[i]<4 or y[i]<4:
        finish.append(i)
print(finish)
finish.reverse()
print(finish)
for i in finish:
    print(i)
    for j in massiv:
        if i==j[0]:
            massiv.pop(i)
print(massiv)



