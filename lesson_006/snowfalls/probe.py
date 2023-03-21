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
    if x[i]<5 or y[i]<5:
        finish.append(i)
print(finish)
# massiv_dict=dict(massiv)
# print(massiv_dict)
# for i in finish:
#     print(i)
#     massiv.pop(i)
massiv.pop(1)
print(massiv)
