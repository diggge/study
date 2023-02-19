import simple_draw as sd
spisok_sneshinok=[]
# print(spisok_sneshinok)
# spisok_sneshinok.append((sd.random_number(350,700),43))
# print(spisok_sneshinok)
for i in range(1,21):
    spisok_sneshinok.append((sd.random_number(350,700), 600))
    print(i,spisok_sneshinok[i-1])
print(spisok_sneshinok[4])
print(spisok_sneshinok[4][1])