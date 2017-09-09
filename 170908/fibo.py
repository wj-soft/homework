def fibo(n):
    if n==1 or n==0:
        return 1
    return fibo(n-2) + fibo(n-1)

for i in range(10):
    print(fibo(i), end= ' ')

