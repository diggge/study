n = int(input("Введите число:"))
t=i=len(str(n))
r=j=i//2
summa_left = 0
summa_right = 0
for k in range(1,j+1):
    summa_left += (n % 10**i) // 10**(i-1)
    summa_right += (n % 10**j) // 10**(j-1)
    i -= 1
    j -= 1
print(t,r,k)
if summa_left==summa_right:
    print(f'{n}: Счастливое число')
else:
    print(f'{n}: Несчатсливое число')