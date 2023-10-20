def HEXtoDEC(hex):
    hex = hex.upper()  # Zamień litery na duże, aby obsługiwać zarówno małe, jak i duże litery
    hexChars = "0123456789ABCDEF"
    result = 0

    for number in hex:
        if number in hexChars:
            charToDEC = hexChars.index(number)  # Indeks cyfry w zestawie cyfr szesnastkowych
            print(charToDEC)
            result = result * 16 + charToDEC  # Przekształć na dziesiętny, uwzględniając pozycję cyfry

    return result

# Pobierz liczbę szesnastkową od użytkownika
hex = input("Podaj liczbę w systemie szesnastkowym: ")

result = HEXtoDEC(hex)
print(f"Liczba {hex} w systemie dziesiętnym: {result}")

"""
- Pobieramy liczbę w systemie szesnastkowym od użytkownika.
- Zamieniamy wszystkie litery na duże litery, aby obsługiwać zarówno małe, jak i duże litery w zapisie szesnastkowym.
- Inicjalizujemy zmienną wynik na 0, która będzie przechowywać wartość liczby w systemie dziesiętnym.
- Tworzymy zestaw cyfr szesnastkowych w zmiennej hexChars.
- Przetwarzamy liczbę szesnastkową od lewej do prawej (od pierwszej do ostatniej cyfry) za pomocą pętli for.
- Dla każdej cyfry szesnastkowej, sprawdzamy, czy znajduje się w zestawie hexChars. Jeśli tak, obliczamy jej indeks w zestawie.
- Następnie przekształcamy tę cyfrę szesnastkową na cyfrę dziesiętną, uwzględniając jej pozycję w liczbie (mnożymy przez 16 i dodajemy wartość).
- Proces ten powtarza się dla wszystkich cyfr.
- Na koniec zwracamy wynik jako liczbę w systemie dziesiętnym.
"""
