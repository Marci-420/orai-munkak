import math 
print(" Starting f.a.s.z.")
# feladat: 3 adott számról döntsük el, hogy 3szög-e
a = int(input(" Derékszögű 3szög a oldala"))
b = int(input(" Derékszögű 3szög b oldala"))
c = int(input(" Derékszögű 3szög c oldala"))

if (a < b + c and b < a + c > b) and a + b > c:
    print("kijött")
    print("A 3szög kerülete:", a + b + c, "méter")
    s = (a+b+c) / 2
    print(s)
    T = math.sqrt (s* (s-a) * (s-b) * (s-c))
    print("A 3szög területe:", "{} cm\u00b2".format(T))
else: 
    print("hehehehehehe")

