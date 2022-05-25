from telnetlib import X3PAD 
import random


mon= input("Ajd meg egy mondatot: ")
dat = input("Ajd meg még egy mondatot: ")

print(len(mon))
print(len(dat))

if len(mon) > len(dat):
    print("A ", mon, "hosszabb, mint a ", dat)
else:
     print("A ", dat, "hosszabb, mint a ", mon)

print(mon.endswith(".") and dat.endswith("."))

print(mon[0].isupper() and dat[0].isupper())


mondat = "A számítógép-programozás (vagy egyszerűen programozás) egy vagy több absztrakt algoritmus megvalósítását jelenti egy bizonyos programozási nyelven"

#1
print(mondat.find( "-"))
#2
print(mondat[0].isalpha())
#3
szavak = mondat.split(" ")
print(szavak)
#4
print(mondat.rstrip())
#5???
lista = [mondat]
lista.append("Wikipédia")
print(mondat)
#6 


#függvény, ami paraméterenként kap egy számot, majd random legenerál annyi számból álló listát és kiírja


def szam (a: int) -> int:
    lista = []
    for a in range():
        random.randint(5)
        lista.append()
        
print(lista)
        
    