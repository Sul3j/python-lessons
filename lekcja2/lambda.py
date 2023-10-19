# funkcja lambda
# lambda argumenty : wyrażenie

lambda1 = lambda a : a + 10

# print(lambda1(5))

lambda2 = lambda a, b : a * b

# print(lambda2(5,6))

lambda3 = lambda a, b, c : a + b + c
# print(lambda3(5, 6, 2))

# użycie funkcji lambda

def myFunc(n):
  return lambda a : a * n

myDoubler = myFunc(2)
myTripler = myFunc(3)

# print(myDoubler(11))
# print(myTripler(11))

