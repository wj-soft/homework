def fib2(n) :
    b= True
    f1 = 1
    f2 = 1

    while n > 2:
        if b:
            f1 = f1 + f2
        else :
            f2 = f1 + f2

        b = not b
        n -= 1

    if b:
        return f2
    else:
        return f1

for i in range(10):
    print(fib2(i), end= ' ')
