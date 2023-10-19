# sety

fruits = {"jabłko", "banan", "wiśnia"}
set1 = {"apple", "banana", "cherry", True, 1, 2}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
setConstructor = set(("apple", "banana", "cherry"))

# wyciąganie danych z setu i sprawdzanie czy set je posiada

# for x in fruits:
  # print(x)

# print("banan" in fruits)

#dodawanie wartości do setu

fruits.add("pomarańcza")

tropical = {"mango", "ananas"}

myList = ["kiwi", "jagoda"]

fruits.update(tropical)
fruits.update(myList)

# usuwanie elementów setu

fruits.remove("banan")

fruits.discard("jabłko")

# usuwanie randomowego elementu setu

fruits.pop()

# czyszczenie setu

# fruits.clear()

# usuwanie setu

del fruits

# łączenie setów

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)

# tworzenie setu z pokrywających się wartości

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)


# tworzenie setu z pominięciem powtarzających się
a = {"apple", "banana", "cherry", 1}
b = {"google", "microsoft", "apple", True}

a.symmetric_difference_update(y)

#dodatkowe metody do wywoływania na setach

# https://www.w3schools.com/python/python_sets_methods.asp
