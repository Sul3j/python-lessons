# zadanie 1

text1 = """ Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. Praesent 
nunc odio, ornare a tellus nec, interdum 
varius lorem. Fusce aliquet velit ut ultricies 
cursus. Donec ut gravida sem. Vivamus mattis mattis viverra. 
Ut pharetra interdum dui, iaculis vehicula risus 
convallis eget. Donec ut dapibus massa."""

text2 = "Uczymy się programować w języku python"

text2 = text2.replace("python","Python")

text3 = "i dobrze się bawimy ;)"

text4 = text2 + " " + text3

text4 = text4.upper()

# zadanie 2

list1 = ["jabłko", "pomarańcza", "ananas", "truskawka", "mango"]

print(len(list1))

print(list1[2:4])

print(list1[-1])

list1.append("mandarynka")

list1.insert(2, "gruszka")

list1.pop(2)

list1.sort()

(fruit1, fruit2, *fruits) = list1

# zadanie 3

tuple1 = (1,7,8,3,5)

tupleLenght = len(tuple1)

tuple2 = tuple1 * 2

count = tuple2.count(tuple2[0])

# zadanie 4

car1 = {
    "marka": "Opel",
    "model": "Astra",
    "rok_produkcji": 2000,
    "przebieg": 220034
}

car2 = {
    "marka": "Skoda",
    "model": "0ctavia",
    "rok_produkcji": 2008,
    "przebieg": 140151
}

car3 = {
    "marka": "BMW",
    "model": "E36",
    "rok_produkcji": 1997,
    "przebieg": 320419
}

car2["rok_produkcji"] = 2012

carDealership = {
    "auto1": car1,
    "auto2": car2,
    "auto3": car3
}

del car1
del car2
del car3
