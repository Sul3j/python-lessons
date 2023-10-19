# a == b  # a równa się b
# a > b # a jest większe od b
# a < b # a jest mniejsze od b
# a <= b # a jest mniejsze lub równe b
# a >= b # a jest wieksze lub równe b
# a != b # a nie jest równe b

# operatory do łączenia warunków
# | - lub
# & - i

# instrukcja wrunkowa if
a = 43
b = 340

if b > a:
    print("b jest większe od a")

# instrukcja warunkowa która jest sprawdzana gdy warunek if nie został spełniony
x = 22
y = 22

if b > a:
    print("y jest większe od x")
elif a == b:
    print("y i x są równe")

# else - jest wykonywany kiedy if i elif nie spełniają warunków

z = 230
q = 31

if q > z:
    print("q jest większe od z")
elif z == b:
    print("q i z są równe")
else:
    print("z jest większe od q")

print("a") if a > b else print("b")

# warunek jednoliniowy

if b > a: print("b jest większe od a")

# warunek jednoliniowy z else

print("a") if a > b else print("b")

# warunek jednoliniowy z 3 wyrażeniami

print("a") if a > b else print("=") if a == b else print("b")

# słowo kluczowe and
# warunek jest prawdziwy gdy obydwa warunki które łączymy są prawdziwe

i = 340
o = 89
p = 670

if i > o and p > i:
    print("wyrażenie jest prawdziwe")

# słowo kluczowe or
# warunek jest prawdziwy gdy jeden z warunków jest prawdziwy

j = 220
k = 90
l = 890

if j > k or j > l:
    print("wyrażenie jest prawdziwe, gdy jeden z warunków jest prawdziwy")

# słowo kluczowe not
# słowo kluczowe not neguje warunek

n = 78
m = 239

if not n > m:
    print("n nie jest większe od m")

# zagnieżdżenie instrukcji warunkowych

d = 40

if d > 10:
    print("powyżej 10")
    if d > 20:
        print("także powyżej 20")
    else:
        print("ale nie powyżej 20")

# słowo kluczowe pass
# pomija warunek

e = 34
r = 340

if e > r:
    pass
