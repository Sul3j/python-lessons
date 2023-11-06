def BINtoDEC(binary):
    result = 0
    base = 1  # Inicjalizacja podstawy systemu (2^0)

    # Przetwarzanie od ostatniej cyfry (od prawej do lewej)
    for number in reversed(binary):
        if number == '1':
            result = result + base
        base = base * 2  # Zwiększamy podstawę systemu o 2

    return result

# Pobierz liczbę binarną od użytkownika
binary = input("Podaj liczbę w systemie binarnym: ")

result = BINtoDEC(binary)
print(f"Liczba {binary} w systemie dziesiętnym: {result}")
