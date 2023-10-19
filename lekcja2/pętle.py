# pętla iterująca po elementach listy

fruits = ["jabłko", "banan", "wiśnia"]
for x in fruits:
  print(x)

# pętla iterująca po ciągu znaków

for x in "banan":
  print(x)

# przerwanie pętli iterującej po tablicy

for x in fruits:
  print(x)
  if x == "banan":
    break

# słowo kluczowe continue
# słowo kluczowe continue pomija dalsze instrukcje w pętli i idzie do nastepnego wykonania

for x in fruits:
    if x == "banan":
        continue
    print(x)

# funkcja range
# funkcja range pozwala nam na stworzenie pętli o określonej ilości przejść

# iteracja od 0 do 5
for x in range(6):
    print(x)

# iteracja od 2 do 5
for x in range(2, 6):
    print(x)

# iteracja od 2 do 29 co 3
for x in range(2, 30, 3):
    print(x)

# else w pętlach
# iteracja od 0 do 5 i po zakończeniu iterowania pętli wykonanie else
for x in range(6):
    print(x)
else:
    print("Wywołanie pętli zakończone!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Wywołanie pętli zakończone!")

# zagnieżdżone pętle
adj = ["czerwone", "wielkie", "smaczne"]

for x in adj:
    for y in fruits:
        print(x, y)


# słowo kluczowe pass pomija wykonanie pętli

for x in [0, 1, 2]:
    pass