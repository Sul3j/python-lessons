# słowniki

car = {
  "brand": "Opel",
  "model": "Astra",
  "year": 1997,
  "colors": ["czerwony", "biały", "niebieski"]
}

dictionaryConstructor = dict(name = "Jan", age = 26, country = "Polska")

# dostęp do danych

brand = car["brand"]
model = car.get("model")

# pobieranie kluczy słownika
keys = car.keys()

# pobieranie wartości słownika
values = car.values()

# pobieranie watrości słownika
items = car.items()

# sprawdzanie czy klucz istnieje w słowniku
# if "model" in car:
  # print("Tak, 'model' jest jednym z kluczy słownika")

# aktualizacja wartości

car["year"] = 2000

car.update({"year": 2001})

# dodanie wartości

car["postAccident"] = True

car.update({"course": 141000})

# usuwanie określonego elementu

# car.pop("course")

# del car["course"]

# usuwanie ostatniego dodanego elementu

# car.popitem()

# czyszczenie słownika

# car.clear()

# kopiowanie słowników

newDict1 = car.copy()
newDict2 = dict(car)

# rozszerzone słowniki

myFamily1 = {
  "child1" : {
    "name" : "Adam",
    "year" : 2000
  },
  "child2" : {
    "name" : "Tomek",
    "year" : 1997
  },
  "child3" : {
    "name" : "Marcin",
    "year" : 2001
  }
}

child1 = {
  "name" : "Adam",
  "year" : 2000
}
child2 = {
  "name" : "Tomek",
  "year" : 1997
}
child3 = {
  "name" : "Marcin",
  "year" : 2001
}

myFamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# dodatkowe metody wywoływane na słownikach
# https://www.w3schools.com/python/python_dictionaries_methods.asp
