def swap(decimal, base):

    result = ""

    if decimal == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"  # Cyfry szesnastkowe

    while decimal > 0:
        rest = decimal % base
        decimal //= base
        result += hex_chars[rest] # użycie cyfr szesnastkowych

    return result[::-1]

decimal = int(input("podaj liczbe: "))
base = int(input("podaj podstawe systemu: "))
result = swap(decimal, base)

print(f"Liczba {decimal} w systemie {base}: {result}")

"""
- Algorytm przyjmuje dwie zmienne: liczba, która jest liczbą, którą chcemy przekształcić, oraz podstawa, która określa docelową podstawę systemu liczbowego.
- Jeśli liczba wynosi 0, algorytm od razu zwraca "0", ponieważ liczba 0 w dowolnym systemie pozycyjnym jest zawsze "0".
- Tworzona jest zmienna cyfry, która zawiera zestaw dostępnych cyfr w systemie liczbowym. W przykładzie użyłem cyfr od 0 do 9 oraz literek A do Z, co pozwala na konwersję do systemów o podstawie do 36.
- Następnie, w pętli while, algorytm oblicza resztę z dzielenia liczby przez podstawę systemu, a następnie przypisuje odpowiednią cyfrę z cyfry na początek wyniku. Następnie liczba jest dzielona przez podstawę (używamy operatora //, aby otrzymać liczbę całkowitą).
- Powyższe kroki są powtarzane, aż liczba spadnie do zera, co oznacza, że przekształcenie zostało zakończone.
- Na końcu wynik jest zwracany jako reprezentacja liczby w wybranym systemie pozycyjnym.
"""