def DECtoBIN(decimal):
    if decimal == 0:
        return "0"

    result = ""

    while decimal > 0:
        rest = decimal % 2
        result = str(rest) + result
        decimal = decimal // 2

    return result


# Pobierz liczbę od użytkownika
decimal = int(input("Podaj liczbę w systemie dziesiętnym: "))

result = DECtoBIN(decimal)
print(f"Liczba {decimal} w systemie binarnym: {result}")

"""
- Pobieramy liczbę w systemie dziesiętnym od użytkownika.
- Jeśli liczba wynosi 0, zwracamy "0", ponieważ 0 w systemie binarnym to również "0".
- W pętli while, obliczamy resztę z dzielenia liczby przez 2 (która jest cyfrą w systemie binarnym) i dodajemy ją do początku wyniku jako łańcuch znaków.
- Następnie dzielimy liczbę przez 2, aby uzyskać kolejną cyfrę w systemie binarnym, i kontynuujemy pętlę.
- Proces ten powtarza się, aż liczba spadnie do zera.
- Na koniec zwracamy wynik jako reprezentację liczby w systemie binarnym.
"""

