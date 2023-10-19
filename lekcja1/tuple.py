# tuple
fruits = ("truskawka", "jagoda", "banan", "kiwi", "melon", "mango")
numbers = (1, 5, 7, 9, 3, 9)
bools = (True, False, True)
mixedValues = ("abc", 56, False, 90, "male")
tupleExampleConstructor = tuple(("jabłko", "banan", "wiśnia"))

# aby utworzyła się tupla jedno wartościowa musimy wstawić w niej przecinek
thisTuple = ("Adam",)
# print(type(thisTuple))
thisNotTuple = ("Adam")
# print(type(thisNotTuple))

# wybieranie elemetu tupli

# tuple index-ujemy od 0 (0,1,2,3,4,5,...,n)

# print(fruits[1]) # element pierwszy
# print(fruits[-1]) # element pierwszy od końca
# print(fruits[2:4]) # elementy od 2 do 4
# print(fruits[:4]) # do 4 elementu
# print(fruits[2:]) # od 2 elementu
# print(fruits[-4:-1]) # od 2 elmentu licząc od końca do 4 elemntu licząc od końca

# sprawdzanie czy element istnieje w tupli

# if "banan" in fruits:
    # print("banan istnieje w tupli fruits")

# rozpakowywanie tupli (destrukturyzacja)

(apple, banana, cherry) = tupleExampleConstructor
#print(apple)
#print(banana)
#print(cherry)

(strawberry, banana, *x) = fruits
#print(strawberry)
#print(banana)
#print(x)

(abc, *y, male) = mixedValues
#print(abc)
#print(y)
#print(male)

# funcje wywoływane na tuplach

# ilość danego elementu w tupli
count = numbers.count(9)

# pozycja podanej wartości w tupli
index = numbers.index(1)

# ilość elementów tupli
lenght = len(numbers)

# łączenie tupli

joinTuple = fruits + numbers

# print(joinTuple)

doubleTuple = numbers * 2

# print(doubleTuple)