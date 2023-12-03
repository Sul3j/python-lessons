def Fib(n):
   if n < 3:
       return 1
   return Fib(n-1) + Fib(n-2)

n = int(input("Podaj nr liczby z ciągu Fibonacciego: "))

print(Fib(n))