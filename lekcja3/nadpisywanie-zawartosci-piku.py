# nadpisywanie zawartości pliku
# "w" - Write - plik otwarty do zapisu, przed zapisem zawartość pliku jest usuwana, tworzy plik, jeśli nie istnieje.

# nadpisywanie zawartości pliku
f = open("file3.txt", "w")
f.write("Opps! Usunięto istniejącą zawartość pliku")
f.close()

# otwarcie i czytanie pliku po nadpisaniu
f = open("demofile3.txt", "r")
print(f.read())