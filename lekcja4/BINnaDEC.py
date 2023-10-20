def BINtoDEC(binary):
    result = 0
    base = 1  # Inicjalizacja podstawy systemu (2^0)

    # Przetwarzanie od ostatniej cyfry (od prawej do lewej)
    for number in reversed(binary):
        if number == '1':
            result += base
        base *= 2  # Zwiększamy podstawę systemu o 2

    return result

# Pobierz liczbę binarną od użytkownika
binary = input("Podaj liczbę w systemie binarnym: ")

result = BINtoDEC(binary)
print(f"Liczba {binary} w systemie dziesiętnym: {result}")

"""
- Pobieramy liczbę w systemie dziesiętnym od użytkownika.
- Jeśli liczba wynosi 0, zwracamy "0", ponieważ 0 w systemie binarnym to również "0".
- W pętli while, obliczamy resztę z dzielenia liczby przez 2 (która jest cyfrą w systemie binarnym) i dodajemy ją do początku wyniku jako łańcuch znaków.
- Następnie dzielimy liczbę przez 2, aby uzyskać kolejną cyfrę w systemie binarnym, i kontynuujemy pętlę.
- Proces ten powtarza się, aż liczba spadnie do zera.
- Na koniec zwracamy wynik jako reprezentację liczby w systemie binarnym.
"""
