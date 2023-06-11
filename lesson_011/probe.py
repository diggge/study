n = int(input("Введите число:"))
i = len(str(n))
j = i//2
summa_left = 0
summa_right = 0
y = 1
for _ in range(0,j):
    summa_left += (n % 10**i) // 10**(i-1)
    summa_right += (n % 10**y) // 10**(y-1)
    i -= 1
    y += 1
if summa_left == summa_right:
    print(f'{n}: Счастливое число')
else:
    print(f'{n}: Несчатсливое число')