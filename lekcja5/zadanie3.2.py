# otwieramy plik w trybie do odczytu
plik = open('pi.txt', 'r')
# wyciągamy wszystkie wiersze z pliku
wiersze = plik.readlines()

minWartosc = 999999999999
minWartoscLiczba = 999999999999
maxWartosc = 0
maxWartoscLiczba = 0
wystapieniaFragmentow = {}

# tworzenie słownika do zliczania  fragmentów kluczami są kolejno wszystkie fragmenty a ilość ich początkowo jest ustawiona na 0
for i in range(0, 10):
    for j in range(0, 10):
        wystapieniaFragmentow[str(i) + str(j)] = 0

# zliczanie wszystkich wystąpień fragmentów i zapisywanie ich ilości do słownika
for i in range(0, len(wiersze) - 1):
    # wyjmujemy element o index-ie 0 żeby nie wyjmować entera "/n"
    fragment = wiersze[i][0] + wiersze[i + 1][0]
    wystapieniaFragmentow[fragment] = wystapieniaFragmentow[fragment] + 1


# sprawdzanie których fragmentów jest najwięcej a ktrych najmniej
for klucz in wystapieniaFragmentow: # zmienna klucz przyjmuje kolejne klucze słownika
    liczbaWystapien = wystapieniaFragmentow[klucz] # liczba wystąpień przyjmuje kolejno ilość wystąpień danego fragmentu
    if liczbaWystapien <= minWartosc:
        if liczbaWystapien < minWartosc:
            minWartosc = liczbaWystapien
            minWartoscLiczba = int(klucz)
        if int(klucz) < minWartoscLiczba:
            minWartosc = liczbaWystapien
            minWartoscLiczba = int(klucz)
    if liczbaWystapien >= maxWartosc:
        if liczbaWystapien > maxWartosc:
            maxWartosc = liczbaWystapien
            maxWartoscLiczba = int(klucz)
        if int(klucz) < maxWartoscLiczba:
            maxWartosc = liczbaWystapien
            maxWartoscLiczba = int(klucz)

print("zadanie 3.2: ")
print("Najmniejsza liczba wystąpień:", minWartosc)
print("Liczba o najmniejszych wystąpieniach:", minWartoscLiczba)
print("Największa liczba wystąpień:", maxWartosc)
print("Liczba o największych wystąpieniach:", maxWartoscLiczba)