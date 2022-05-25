beSzam= int(input("Adj meg egy számot"))
db = 0                           # számolja meg, hányszor kellett megszorozni, meg írja ki az eredményt
while beSzam < 100:
     beSzam*=2
     if beSzam%3 == 0:
         db + 1
print(db)