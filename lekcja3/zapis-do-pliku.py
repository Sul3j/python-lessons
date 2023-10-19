# dopisywanie do istniejącego pliku
# "a" - Append -  plik otwarty do zapisu, dodaje nową treść na końcu pliku, nie usuwa starej, tworzy plik jeśli nie istnieje
f = open("file2.txt", "a")
f.write("dodano nowy tekst!")
f.close()

# czytanie pliku po dodaniu nowego tekstu
f = open("file2.txt", "r")
print(f.read())
f.close()








