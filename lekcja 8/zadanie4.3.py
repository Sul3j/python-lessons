plik = open('liczby.txt')
wiersze = plik.readlines()

def ile3(wiersze):
    trojki = []

    for i in range(0, len(wiersze)):
        liczba1 = int(wiersze[i])
        for j in range(0, len(wiersze)):
            if i == j:
                continue

            liczba2 = int(wiersze[j])
            if liczba2 % liczba1 == 0:
                for k in range(0, len(wiersze)):
                    if i == k or j == k:
                        continue

                    liczba3 = int(wiersze[k])
                    if liczba3 % liczba2 == 0:
                        trojki.append([liczba1, liczba2, liczba3])

    return trojki

def ile5(wiersze):
    piatki = []

    for i in range(0, len(wiersze)):
        liczba1 = int(wiersze[i])
        for j in range(0, len(wiersze)):
            if i == j:
                continue

            liczba2 = int(wiersze[j])
            if liczba2 % liczba1 == 0:
                for k in range(0, len(wiersze)):
                    if i == k or j == k:
                        continue

                    liczba3 = int(wiersze[k])
                    if liczba3 % liczba2 == 0:
                        for m in range(0, len(wiersze)):
                            if i == m or j == m or k == m:
                                continue

                            liczba4 = int(wiersze[m])
                            if liczba4 % liczba3 == 0:
                                for n in range(0, len(wiersze)):
                                    if i == n or j == n or k == n or m == n:
                                        continue

                                    liczba5 = int(wiersze[n])
                                    if liczba5 % liczba4 == 0:
                                        piatki.append([liczba1, liczba2, liczba3, liczba4, liczba5])

    return piatki

dobreTrojki = ile3(wiersze)
dobrePiatki = ile5(wiersze)

print('ZADANIE 4.3a.')
print(len(dobreTrojki))
for trojka in dobreTrojki:
    print(trojka)

print('ZADANIE 4.3b.')
print(len(dobrePiatki))
for piatka in dobrePiatki:
    print(piatka)