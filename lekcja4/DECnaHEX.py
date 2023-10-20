def DECtoHEX(decimal):
    if decimal == 0:
        return "0"

    result = ""
    hexChars = "0123456789ABCDEF"  # Cyfry szesnastkowe

    while decimal > 0:
        rest = decimal % 16
        result = hexChars[rest] + result
        decimal = decimal // 16

    return result


# Pobierz liczbę od użytkownika
decimal = int(input("Podaj liczbę w systemie dziesiętnym: "))

result = DECtoHEX(decimal)
print(f"Liczba {decimal} w systemie szesnastkowym: {result}")

"""
- Pobieramy liczbę w systemie dziesiętnym od użytkownika.
- Jeśli liczba wynosi 0, zwracamy "0", ponieważ 0 w systemie szesnastkowym to również "0".
- W pętli while, obliczamy resztę z dzielenia liczby przez 16 (podstawa systemu szesnastkowego) i dodajemy ją do początku wyniku jako odpowiednią cyfrę szesnastkową (zdefiniowaną w hexChars).
- Następnie dzielimy liczbę przez 16, aby uzyskać kolejną cyfrę szesnastkową, i kontynuujemy pętlę.
- Proces ten powtarza się, aż liczba spadnie do zera.
- Na koniec zwracamy wynik jako reprezentację liczby w systemie szesnastkowym.
"""