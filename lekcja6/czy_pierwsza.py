# liczba naturalna większa od 1, która ma dokładnie dwa dzielniki naturalne: jedynkę i siebie samą

def czy_pierwsza(n):
    if n < 2: # liczba mnniejsza niż 2 nie jest pierwsza
        return False
    i = 2
    while i * i <= n:
        if n % i == 0: # jeśli znajdę dzielnik, to liczba n nie jest pierwsza
            return False
        i += 1
    return True # jeśli do pierwiastka z n nie znajdę dzielnika, to znaczy, że nie jest ona pierwsza

p = int(input("Podaj liczbę naturalną, aby sprawdzić, czy jest pierwsza: ")) # wczytuję liczbę zestawów danych

if czy_pierwsza(p):
    print("TAK")
else:
    print("NIE")