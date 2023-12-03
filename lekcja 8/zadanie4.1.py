plik = open('przyklad.txt')
wiersze = plik.readlines()

ile = 0
pierwsza = -1

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz[0] == wiersz[len(wiersz) - 1]:
        ile += 1
        if pierwsza == -1:
            pierwsza = wiersz

print('ZADANIE 4.1')
print(ile, pierwsza)