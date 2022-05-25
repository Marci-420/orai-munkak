#lista létrehozása
import random

szamok = [1, 2, 3]

#FOR ciklus, amely tízszer fut le
for szam in range(10):
    print(szam)

    #FOR ciklusban random generáljon 10 számot
    #a számokat adjuk a listához
    bruh = random.randint(1, 10)
    szamok.append(bruh)
print(szamok)
 
 #kérjünk be egy számot
a = int(input("Adjál meg egy számot: "))

# ha nincs a listában, akkor adjuk hozzá
if a in szamok:
    print("Szerepel a listában")
else: 
    szamok.insert(0, a)

print(szamok)

#az első elemet szorozzuk kettővel
#másodiki elemet, távolítsuk el
szamok[0] = szamok[0] * 2
szamok.pop(1)

 
#rendezzük csökkenőbe a listát

print(szamok.sort(reverse=True))
print(szamok)
#adjuk össze a lista elemeit

bruh = 0
for i in szamok:
    bruh += i
print(bruh)

