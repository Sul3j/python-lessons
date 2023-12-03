def Fib(n):
    a , b = 1, 1
    for i in range(n - 1):
        b = b + a
        a = b - a
    return a

n = int(input("Podaj nr liczby z ciągu Fibonacciego: "))

print(Fib(n))