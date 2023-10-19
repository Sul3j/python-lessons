def positional_representation(number, base):
    if number < 0 or base < 2:
        return "Nieprawidłowe dane wejściowe"

    result = ""

    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base

    return result


# Przykładowe użycie:
number = 3567
base = 8
result = positional_representation(number, base)
print(f"Reprezentacja pozycyjna liczby {number} w systemie o podstawie {base} to: {result}")