def Fib(n):
    a = 1
    b = 1
    for i in range(n):
        print(a, end=' ')
        b = b + a
        a = b - a


# głowna część programu

n = int(input("Podaj długość ciągu: "))
Fib(n)