# aktualizacja tupli

fruits = ("jabłko", "banan", "wiśnia")
y = list(fruits)
y.append("pomarańcza")
fruits = tuple(y)

print(fruits)