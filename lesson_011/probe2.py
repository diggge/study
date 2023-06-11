# n = int(input("Введите число:"))
n=123191321
t = i = len(str(n))
r = j = i//2
y = 1
ravno = 0
summa_left = 0
summa_right = 0
for _ in range(0,j):
    summa_left = (n % 10**i) // 10**(i-1)
    summa_right = (n % 10**y) // 10**(y-1)
    if summa_left == summa_right:
        ravno += 1
    y += 1
    i -= 1
print(t,r)
if ravno == j:
    print(f'{n}: Палиндромное число')
else:
    print(f'{n}: Непалиндромное число')