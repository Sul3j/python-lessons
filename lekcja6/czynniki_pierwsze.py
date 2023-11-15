# Rozłożenie liczby na czynniki pierwsze polega na przedstawieniu jej w postaci iloczynu liczb pierwszych.
def czynniki_pierwsze(liczba):
    czynnik = 2 # (*)
    while czynnik*czynnik <= liczba:
        while liczba % czynnik == 0: # (****)
            print(czynnik, end=' ')
            liczba = liczba//czynnik # (***)
        czynnik += 1 # (**)
    if liczba > 1:
        print(liczba) # (*****)


liczba = int(input("Podaj liczbe: "))
czynniki_pierwsze(liczba)