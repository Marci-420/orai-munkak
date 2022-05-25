import math

#első feladat
a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg még egy számot: "))

if a > b:
    print(" A(z)",  a, "a nagyobb szám!")
elif b > a:
    print("A(z)", b, "a nagyobb szám!")
else:
    print("A két szám egyenlő!")
    
#második feladat
c = int(input("Add meg a háromszög a oldalát: "))
d = int(input("Add meg a háromszög b oldalát: "))
e = int(input("Add meg a háromszög c oldalát: "))

if c + d > e and d + e > c and c + e > d:
    print("A háromszög megszerkeszthető!!")
else: 
    print("A háromszög nem szerkeszthető meg!")
    
#harmadik feladat
f = int(input("Add meg a háromszög a oldalát: "))
g = int(input("Add meg a háromszög b oldalát: "))
h = int(input("Add meg a háromszög c oldalát: "))
K= f+ g+ h
print(" A 3szög kerülete:", K, "méter")
s = K / 2
T = math.sqrt (s* (s-f) * (s-g) * (s-h))
print(" A 3szög területe:" , T, "négyzetméter" )

#negyedik feladat
Aoldal = float(input("Add meg a téglalap a oldalát: "))
Boldal = float(input("Add meg a téglalap b oldalát"))
kerulet = 2 * (Aoldal + Boldal)
terulet = Aoldal * Boldal
print("A téglalap kerülete:", kerulet)
print("A téglalap területe:", terulet)

#első feladat újragondolása max és min függvénnyel

a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg még egy számot: "))
lista = [a,b]
kisebb = min(lista)
print = ("A kisebb szám: ",kisebb)