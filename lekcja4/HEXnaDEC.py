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
