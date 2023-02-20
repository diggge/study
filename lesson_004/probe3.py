import simple_draw as sd
sd.resolution = (1200, 600)
x=[]
for i in range(7):
    if i == 0:
        x.append(sd.random_number(0,100))
    else:
        x.append(x[i-1]+sd.random_number(0,100))
    print(x[i],i)