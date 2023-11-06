# otwieramy plik w trybie do odczytu
plik = open('pi.txt', 'r')
# wyciągamy wszystkie wiersze z pliku
wiersze = plik.readlines()

# Zmienna maxDlugosc przechowuje długość najdłuższego znalezionego ciągu.
# Zmienna maxPozycja przechowuje pozycję początkową najdłuższego znalezionego ciągu.
# Zmienna lokalnaDlugosc przechowuje bieżącą długość ciągu.
# Zmienna lokalnaPozycja przechowuje bieżącą pozycję ciągu.

maxDlugosc = 0
maxPozycja = 0
lokalnaDlugosc = 0
lokalnaPozycja = 0

for i in range(0, len(wiersze) - 5):
    czyRosnacy = True
    czyMalejacy = True
    poprzedniaLiczba = int(wiersze[i])
    j = i + 1

    # Przeglądamy kolejne liczby w ciągu.
    while j < len(wiersze) and (czyRosnacy == True or czyMalejacy == True):

        # Aktualizuje bieżącą długość ciągu.
        lokalnaDlugosc = lokalnaDlugosc + 1

        # Aktualna liczba w ciągu.
        obecnaLiczba = int(wiersze[j])

        # Jeśli aktualny ciąg jest rosnący i obecna liczba jest mniejsza lub równa poprzedniej, to ciąg nie jest rosnący.
        if czyRosnacy and obecnaLiczba <= poprzedniaLiczba:
            # Jeśli ciąg ma długość 1, to nie może być ani rosnący, ani malejący.
            if lokalnaDlugosc == 1:
                lokalnaDlugosc = 0
                break
            # Ciąg nie jest rosnący
            czyRosnacy = False
        # Jeśli aktualny ciąg nie jest rosnący i obecna liczba jest większa lub równa poprzedniej, to ciąg nie jest malejący.
        elif not czyRosnacy and czyMalejacy and obecnaLiczba >= poprzedniaLiczba:
            # Ciąg nie jest malejący
            czyMalejacy = False
            # Jeśli bieżąca długość ciągu jest większa od maksymalnej długości znalezionego ciągu, to aktualizujemy maksymalną długość i pozycję początkową.
            if lokalnaDlugosc > maxDlugosc:
                maxDlugosc = lokalnaDlugosc
                maxPozycja = i
            lokalnaDlugosc = 0
        # Aktualizuje poprzednią liczbę w ciągu.
        poprzedniaLiczba = obecnaLiczba
        # Przechodzi do następnej liczby w ciągu.
        j = j + 1

# Tworzymy listę zawierającą znaleziony ciąg.
ciag = [''.join(sublista).replace('\n', '') for sublista in wiersze[maxPozycja:maxPozycja + maxDlugosc]]

# Wypisujemy pozycję początkową i znaleziony ciąg.
print("zadanie 3.4: ")
print(maxPozycja + 1, ciag)


