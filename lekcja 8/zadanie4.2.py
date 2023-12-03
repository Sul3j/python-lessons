def czynniki_pierwsze(liczba):
    czynniki = []
    i = 2
    while i*i <= liczba:
        while liczba % i == 0:
            czynniki.append(i)
            liczba = liczba//i
        i += 1
    if liczba > 1:
        czynniki.append(liczba)
    return czynniki

plik = open('przyklad.txt')
wiersze = plik.readlines()

maxCzynnikow = -1
maxCzynnikowLiczba = -1
maxRoznychCzynnikow = -1
maxRoznychCzynnikowLiczba = -1

for wiersz in wiersze:
    liczba = int(wiersz)
    rozklad = czynniki_pierwsze(liczba)

    if len(rozklad) > maxCzynnikow:
        maxCzynnikow = len(rozklad)
        maxCzynnikowLiczba = liczba

    rozne = set(rozklad)
    if len(rozne) > maxRoznychCzynnikow:
        maxRoznychCzynnikow = len(rozne)
        maxRoznychCzynnikowLiczba = liczba

print('ZADANIE 4.2.')
print(maxCzynnikowLiczba, maxCzynnikow, maxRoznychCzynnikowLiczba, maxRoznychCzynnikow)