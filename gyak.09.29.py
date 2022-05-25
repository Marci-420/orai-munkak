import math

a = int(input("adj meg egy egész számot: "))
b = int(input("adj meg egy egész számot: "))
print("A megadott két szám:", a, "és", b)

c = math.sqrt (pow (a, 2) + pow (b, 2))
print("Az átfogó hossza: ", c)

if c < 0:
    print("nincs megoldás")