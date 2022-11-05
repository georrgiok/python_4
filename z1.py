#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input("Type N: "))

ans = str(n) + " =>"
while n > 1:
    for i in xrange(2, n+1):
        if n%i == 0:
            n /= i
            ans += " "+str(i)
            break
print(ans)
