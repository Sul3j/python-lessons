# otwieramy plik w trybie do odczytu
plik = open('pi_przyklad.txt', 'r')
# wyciągamy wszystkie wiersze z pliku
wiersze = plik.readlines()

# Zmienna licznik przechowuje liczbę znalezionych ciągów
licznik = 0

# Lista ciagi przechowuje znalezione ciągi
ciagi = []

ciagTest = []

# Przeglądamy wszystkie możliwe ciągi o długości 6
for i in range(0, len(wiersze) - 5):

    # Czy aktualny ciąg jest rosnący?
    czyRosnacy = True
    # Czy aktualny ciąg jest malejący?
    czyMalejacy = True

    # Przechowuje poprzednią liczbę w ciągu
    poprzedniaLiczba = int(wiersze[i])

    print(ciagTest)
    ciagTest = []

    # Przeglądamy kolejne liczby w ciągu
    for j in range(1, 6):


        # Aktualna liczba w ciągu
        obecnaLiczba = int(wiersze[i + j])

        ciagTest.append(obecnaLiczba)

        # Jeśli aktualny ciąg jest rosnący i maleje lub liczba obecna jest taka sama jak poprzednia
        if czyRosnacy and obecnaLiczba <= poprzedniaLiczba:
            # Jeśli ciąg ma długość 1, to nie może być ani rosnący, ani malejący
            if i + 1 == i + j:
                print(obecnaLiczba)
                print(poprzedniaLiczba)
                czyRosnacy = False
                czyMalejacy = False
                break

            # Ciąg nie jest rosnący
            czyRosnacy = False

        # Jeśli aktualny ciąg jest malejacy i rośnie lub liczba jest taka sama jak poprzednia
        elif not czyRosnacy and czyMalejacy and obecnaLiczba >= poprzedniaLiczba:

            # Ciąg nie jest malejący
            czyMalejacy = False
            break

        # Aktualizuje poprzednią liczbę w ciągu
        poprzedniaLiczba = obecnaLiczba

    # Jeśli aktualny ciąg jest rosnący i malejący, to sprawdzamy, czy zawiera co najmniej jedną liczbę mniejszą niż poprzednia
    if czyRosnacy == False and czyMalejacy == True:

        # Czy ciąg zawiera co najmniej jedną liczbę mniejszą niż poprzednia?
        czyMalejeCoNajmniejRaz = False

        # Przeglądamy ciąg
        for k in range(0, len(wiersze[i:i+j+1]) - 1):

            # Jeśli obecna liczba jest mniejsza niż poprzednia, to ciąg zawiera co najmniej jedną liczbę mniejszą niż poprzednia
            if int(wiersze[i+k+1]) < int(wiersze[i+k]):
                czyMalejeCoNajmniejRaz = True
                break

        # Jeśli ciąg zawiera co najmniej jedną liczbę mniejszą niż poprzednia, to go dodajemy do listy znalezionych ciągów
        if czyMalejeCoNajmniejRaz:
            licznik += 1
            ciagi.append(wiersze[i:i+j+1])

# Przekształcamy listę ciągów na listę ciągów bez znaków nowej linii
listaCiagow = [''.join(sublista).replace('\n', '') for sublista in ciagi]

# Wypisujemy liczbę znalezionych ciągów i listę znalezionych ciągów
print("zadanie 3.3: ")
print(licznik, listaCiagow)