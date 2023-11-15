# to taka liczba naturalna, której suma naturalnych dzielników mniejszych od niej jest równa tej liczbie.
# 6 = 1 + 2 + 3
# 28 = 14 + 7 + 4 + 2 + 1

# zmienna suma będzie przechowywać sumę
def czy_doskonala(liczba):
    suma = 1 # każda liczba dzieli się przez jeden
    k = 2 # k przyjmuje kolejne wartości z przedziału [2..sqrt(liczba))
    while k*k < liczba:
        if liczba % k == 0: # jeśli k jest dzielnikiem liczby liczba
            suma += k + liczba/k # to zwiększ wartość zmiennej suma o dwa dzielniki
        k += 1
    if k*k == liczba: # jeśli liczba jest kwadratowa
        suma += k   # to zwiększ wartość suma o dzielnik k
    return suma == liczba


liczba = int(input("Podaj liczbę: "))
if czy_doskonala(liczba):
    print(f"Liczba {liczba} jest doskonała")
else:
    print(f"Liczba {liczba} nie jest doskonała")