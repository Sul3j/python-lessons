def DECtoHEX(decimal):
    if decimal == 0:
        return "0"

    result = ""
    hexChars = "0123456789ABCDEF"  # Cyfry szesnastkowe

    while decimal > 0:
        rest = decimal % 16
        print(rest)
        result = hexChars[rest] + result
        print(hexChars[rest])
        decimal = decimal // 16

    return result


# Pobierz liczbę od użytkownika
decimal = int(input("Podaj liczbę w systemie dziesiętnym: "))

result = DECtoHEX(decimal)
print(f"Liczba {decimal} w systemie szesnastkowym: {result}")
