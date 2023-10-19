# listy
names = ["Adam", "Tomasz", "Mateusz", "Kasia", "Ania", "Sylwia", "Marcin"]
numbers = [1, 5, 7, 9, 3, 9]
bools = [True, False, True]
mixedValues = ["abc", 56, False, 90, "male"]
tupleExampleConstructor = list(("apple", "banana", "cherry"))

# wyciąganie elementów tablicy
# listy index-ujemy od 0 (0,1,2,3,4,5,...,n)
x = names[0]

names[0] = "Klaudia"

# print(names[1]) # element pierwszy
print(names[-1]) # element pierwszy od końca
# print(names[2:4]) # elementy od 2 do 4
# print(names[:4]) # do 4 elementu
# print(names[2:]) # od 2 elementu
# print(names[-4:-1]) # od 2 elmentu licząc od końca do 4 elemntu licząc od końca

# sprawdzanie czy element istnieje w liście

# if "Tomasz" in names:
    # print("Tomasz istnieje w liście names")

# rozpakowywanie listy (destrukturyzacja)

(isHuman, isPet, isMale) = bools
# print(isHuman)
# print(isPet)
# print(isMale)

(klaudia, tomasz, *x) = names
# print(klaudia)
# print(tomasz)
# print(x)

(abc, *y, male) = mixedValues
# print(abc)
# print(y)
# print(male)

# sprawdzanie długości tablicy

lenght = len(names)

# dodawanie elementów do tablicy

names.append("Marta")

# dodanie elementu na specyficzną pozycję

names.insert(2, "Basia")

# usuwanie elementów z tablicy

names.pop(1)

# czyszczenie tablicy

cars = ["BMW", "Audi", "Seat", "Opel"]

cars.clear()

# zwaracanie kopii tablicy

names2 = names.copy()

# zwracanie ilości danych elementów w tablicy

count = names2.count("Klaudia")

# rozszerzanie tablicy o inną tablicę

names2.extend(names)

# sprawdzanie indexu danego elementu tablicy

index = names2.index("Mateusz")

# usunięcie elementu o podanej wartości - 1 element

names2.remove("Mateusz")

# odwracanie tablicy

names2.reverse()

# sortowanie tablicy

names2.sort()

