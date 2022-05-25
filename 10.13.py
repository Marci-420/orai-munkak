#feladat: bekérni egy számot
#a program véletlenszerűen generáljon egy számot a megadott tartományban
#addig kérje a felhasználó tippjeit, amíg AZ el nem találja
import random

elso = int(input("Add meg a tartomány alsó határát: " ))
utolso = int(input("Add meg a tartomány felső határát: " ))

gondoltSzam = random.randint(elso, utolso)
tipp = int(input("tipp: "))


if tipp > utolso or tipp < elso:
    print("Te kajak ekkora nyomorék vagy?")

while tipp != gondoltSzam:
    tipp = int(input("Nem talált, próbáldd mégegyszer: "))

if tipp == gondoltSzam:
    print("Nyertél")