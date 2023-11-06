# otwieramy plik w trybie do odczytu
plik = open('pi_przyklad.txt', 'r')
# wyciągamy wszystkie wiersze z pliku
wiersze = plik.readlines()

# przejście przez wiersze od 1 do przedostatniego
licznik = 0
for i in range(0, len(wiersze) - 1):
    # wyjmujemy element o index-ie 0 żeby nie wyjmować entera "/n"
    fragment = wiersze[i][0] + wiersze[i + 1][0]
    # zmieniamy fragment na int żeby usunąć 0 w fragmentach rozpoczynających sie od niego
    # "06" -> 6
    fragmentLiczba = int(fragment)
    # zwiększanie liczika gdy fragment jest większy od 90
    if fragmentLiczba > 90:
        licznik += 1

print(f"rozwiązanie 3.1: {licznik}")
