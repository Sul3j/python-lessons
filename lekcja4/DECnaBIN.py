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
