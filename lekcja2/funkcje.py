#funkcje

# definicja funkcji
def myFunction1():
  print("Witam w funkcji")

# wywołanie funkcji
# myFunction1()

# argumenty funkcji
# argumenty pozwalają nam na przekazanie danych do funkcji
def myFunction2(firstName):
  print(firstName + " Kowalski")

# myFunction2("Adam")
# myFunction2("Marcin")
# myFunction2("Tomasz")

def myFunction3(firstName, lastName):
  print(firstName + " " + lastName)

# myFunction3("Tomasz", "Kowalski")

# przekazywanie argumentów za pomocą kluczy
def myFunction4(child3, child2, child1):
  print("Najmłodszym dzieckiem jest: " + child3)

# myFunction4(child1 = "Adam", child2 = "Marcin", child3 = "Tomasz")

# przekazywanie jako argument słownika danych
def myFunction5(**kid):
  print("Jego nazwisko to: " + kid["lastName"])

# myFunction5(firstName = "Marcin", lastName = "Kowalski")

# domyślna wartość argumentu
def myFunction6(country = "Norwegi"):
  print("Jestem z " + country)

# myFunction6("Szwecji")
# myFunction6("Indi")
# myFunction6()
# myFunction6("Brazyli")

# podawanie listy jako argument

def myFunction7(food):
  for x in food:
    print(x)

fruits = ["jabłko", "banan", "wiśnia"]

# myFunction7(fruits)

# zwracanie wartości z funkcji

def myFunction8(x):
  return 5 * x

# print(myFunction8(3))
# print(myFunction8(5))
# print(myFunction8(9))

# definiowanie funkcji bez żadnej zawratości

def myFunction9():
    pass

