#bekérjük a pontszámot, aztán értékelünk, 
#ha 0-39, akkor karó
#ha 40-54, akkor kettes
#ha 55-69, akkor közepes
#ha 70-84, akkor jó
#ha 85-100, akkor jeles
#majd kiírjuk az eredményt


a = int(input("Add meg a pontszámodat: "))

if a < 40:
    print("Elégtelen")
elif a < 55:
    print("elégséges")        
elif a < 70:
    print("közepes")
elif a < 85:
     print("Jó")
elif a <= 100:
    print("jeles")

# egészítsük ki: addig kérjen be pontszámokat a program, amíg mínusz egyet ír be a tanár
a = int(input("Add meg a pontszámodat: "))

while a != -1 :
 if a <= 40:
    print("Elégtelen")
 elif a <= 55:
    print("elégséges")        
 elif a <= 70:
    print("közepes")
 elif a <= 85:
     print("Jó")
 elif a <= 100:
    print("jeles")
 a = int(input("Adj meg egy másik számot: "))

 #számoljuk meg, hány ötös lett

a = int(input("Add meg a pontszámodat: "))

db = 0
if a <= 40:
    print("Elégtelen")
elif a <= 55:
    print("elégséges")        
elif a <= 70:
    print("közepes")
elif a <= 85:
    print("Jó")
elif a <= 100:
    print("jeles")
    db = db + 1
    
    
print(db, "jeles dolgozat van.")



