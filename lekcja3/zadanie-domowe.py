# zadanie 1
"""

f = open("file7.txt", "a")

i = 0
fruit = ""

while i < 5:
    fruit = input("podaj nazwę owocu: ")
    f.write(fruit + ";")
    i = i + 1

f.close()

"""

# zadanie 2
"""

f = open("file7.txt", "r")

text = f.readline()

fruitsList = text.split(";")

fruitsList.remove("")

f.close()
"""
# zadanie 3
"""

import os

if os.path.exists("file7.txt"):
  os.remove("file7.txt")
else:
  print("Ten plik nie istnieje")
"""
# zadanie 4

f = open("file8.txt", "a")

i = 0
fruit = ""

while i < 10:
    fruit = input("podaj cyfre od 1 do 10: ")
    f.write(fruit + "\n")
    i = i + 1

f.close()

# zadanie 5

f = open("file8.txt", "r")

x = 0
number = ""
numberList = []
count = 0

while x < 10:
    number = f.readline()
    numberList.append(int(number))
    x = x + 1

print(numberList)

for a in numberList:
    count = numberList.count(a)
    while count > 1:
        numberList.remove(a)
        count = count - 1
    count = 0

numberList.sort()

print(numberList)