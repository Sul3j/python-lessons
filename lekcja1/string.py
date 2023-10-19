#zapis wieloliniowy

multiLine = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# wyciąganie znaku z ciągu

exampleText = "Ala ma kota a kot ma Ale"

letter = exampleText[0]

# długość ciągu znaków

lenght = len(exampleText)

# wycinanie części ciągu znaków

slice1 = exampleText[2:7]
slice2 = exampleText[:5]
slice3 = exampleText[2:]
slice4 = exampleText[-5:-2]

# zamiana ciągu znaków na małe / duże litery

upper = exampleText.upper()

lower = exampleText.lower()

# usuwanie białych znaków

exampleText1 = "  text 123   "

removeWhitespace = exampleText1.strip()

# zamiana znaków

replace = exampleText.replace("A", "E")

# dzielenie ciągu znaków

exampleText2 = "jeden, dwa, trzy"
exampleText3 = "jeden; dwa; trzy"

split = exampleText2.split(",")
split2 = exampleText3.split(";")

# łączenie ciągów znaków

a = "Cześć"
b = "Adam"
c = a + b
d = a + " " + b

# string format

age = 24

text = "Tomek ma {} lata"

text2 = "Tomek ma {1} lata i {0} psy"

# print(text.format(age))
# print(text2.format(2, age))

# dodatkowe metody do wywoływania na ciągach znaków
# https://www.w3schools.com/python/python_strings_methods.asp
