for ch in 'hello@.':
    k1=0
    k2=0
    print(ord(ch))
    if ord(ch) == 64:
        k1 += 1
    if ord(ch) == 46:
        k2 += 1
if (k1 == 1 and k2 == 1):
    print(k1,k2,'почта написано корректно')
else:
    print(k1,k2,'почта написано некорректно')


    # print(ord(ch))