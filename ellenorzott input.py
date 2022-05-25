

#addig kérünk egy páros számot, amíg 1 és 20 közötti számot nem ad meg 
import random

a = int(input("Adj meg egy 10 és 20 közötti páros számot"))

gondoltSzam = random.randint(10, 12, 14, 16, 18, 20)
tipp = int(input("tipp: "))

if a % 2 != 0 and (a >= 10 and  a <= 20):
    print("Nem talált")

while tipp != gondoltSzam:
    tipp = int(input("Nem talált, próbáldd mégegyszer: "))

if tipp == gondoltSzam:
    print("Nyertél")

