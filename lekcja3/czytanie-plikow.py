# "r" - Read - Otwiera plik do odczytu, błąd jeśli plik nie istnieje
# "a" - Append -  plik otwarty do zapisu, dodaje nową treść na końcu pliku, nie usuwa starej, tworzy plik jeśli nie istnieje
# "w" - Write - plik otwarty do zapisu, przed zapisem zawartość pliku jest usuwana, tworzy plik, jeśli nie istnieje.
# "x" - Create - Tworzy określony plik, zwraca błąd, jeśli plik istnieje

# "t" - Text - Domyślna wartość. Tryb tekstowy
# "b" - Binary - Tryb binarny

# czytanie pliku
f = open("file.txt")

file = open("file.txt", "r")
#print(file.read())

# czytanie pliku z dowolnej lokalizacji na dysku
#file1 = open("D:\\myfiles\welcome.txt", "r")
# print(file1.read())

# czytanie pierwszych 5 znaków z pliku tekstowego
print(file.read(5))

# czytanie pojedyńczej lini z pliku
print(file.readline())
print(file.readline())

# czytanie lini pliku w pętli
for x in file:
  print(x)

# zamknięcie połączenia z plikiem po zakończeniu jego używania
file.close()