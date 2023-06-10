# n = int(input("Введите число:"))
n=3291566
i=len(str(n))
print("Количество цифр равно:", i)
j=i//2
summa_left = 0
summa_right = 0
for k in range(1,j+1):
    summa_left += (n % 10**i) // 10**(i-1)
    summa_right += (n % 10**(j)) // 10**(j-1)
    i -= 1
    j -= 1
print(n,j,summa_left,summa_right)