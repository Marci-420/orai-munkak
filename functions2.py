#függvény: névvel ellátott, adott feladatot elvégző utasítások sorozata
#a függvényt használat előtt definiálni kell
#formája: 1. függvény fej:

#def függvény_neve(formális paraméterlista) -> függvény_visszatérési_értékének_a_típusa:
#2: Függvény törzs leítása:

#tetszőleg számú utasítás



from xmlrpc.client import boolean


def összead(a: int, b: int) -> int:          #a függvény feje
    #def => a függvény definíciót bevezető kulcsszó
    #összead => a függvény azonosítója (neve)
    #() => operátorok a paraméterek megadására
    #a: int, b: int => a függvény formális paraméterei azonosítóval és típussal (típus opcionális)
    # -> => a függvény visszatérési értékét ezután az "operátor" után adhatjuk meg (opcionális)
    # int => a függvény visszatérési értékének a típusa
    
    return a + b # a függvény törzse


# a függvény hívása
# a hívás szintaxisa(szabályai):
# függvény_azonosítója/neve(aktuális paraméterlista)
összead(3, 4)   # a függvény visszatérési értéke így elveszik
print(összead(3, 4)) # a függvény visszatérési értékét így a képernyőre írjuk
osszeg: int= összead(3, 4) #a függvény visszatérési értékét így eltároljuk
print(osszeg)

# feladat:két szám legnagyobb közös osztóját adja vissza a függvény

def lnko(a, b):
    if(b == 0):
        return a
    else:
        return lnko(b, a % b)
  
a = 12
b = 18
  
print("A két szám legnagyobb közös osztója: ", end="")
print(lnko(12, 18))

def lnko(a, b):
  
  
    if (a == 0):
        return b
    if (b == 0):
        return a
  
    if (a == b):
        return a

    if (a > b):
        return lnko(a-b, b)
    return lnko(a, b-a)
  

a = 12
b = 18
if(lnko(a, b)):
    print('A legnagyobb közös osztója', a, 'és', b, ':', lnko(a, b))
else:
    print('Nincs közös osztója')
    


a = int(input("Add meg az a-t: "))
b = int(input("Add meg a b-t: "))
def lnko(a: int, b:int) -> int:
    while a!=b:
        if a > b:
            a = a - b
        else: 
            b = b - a
    return a
print(lnko(a, b))

#feladat: írj egy logikai értékkel visszatérő python függvényt, amely
#paraméterenként kap egy egész számot, és eldönti a számról, hogy osztható-e 2-vel és 3-mal is egyszerre


a = int(input("Adj meg egy számot: "))
def osztas(a: int) -> boolean:
    if (a % 2 ==0 and a % 3 ==0):
        return True
        print("Ez a szám osztható kettővel és hárommal")
    else:
        return False
        print(" Nem osztható kettővel és hárommal is.")
          
print(osztas(12))

        




