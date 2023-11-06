def swap(decimal, base):

    result = ""

    if decimal == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"  # Cyfry szesnastkowe

    while decimal > 0:
        rest = decimal % base
        decimal = decimal // base
        result = result + hex_chars[rest] # użycie cyfr szesnastkowych

    return result[::-1]

decimal = int(input("podaj liczbe: "))
base = int(input("podaj podstawe systemu: "))
result = swap(decimal, base)

print(f"Liczba {decimal} w systemie {base}: {result}")
