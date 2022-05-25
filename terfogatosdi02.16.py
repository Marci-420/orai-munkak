#térfogat: r sugárból és m magasságból kiszámolja a kúp térfogatát
#V=r2 * Pi * M/3

r = int(input("Add meg a kúp sugarát: "))
m = int(input("Add meg a kúp masgasságát: "))


def ker(r, m):
   return (r * r * 3.14 * m / 3)

print(ker(r, m))

#meh = r * r * 3.14 * m/3
#print(meh)

def tref(r: int, m: int) -> float:
    return r * r * 3.14 * m / 3
print(tref(r, m))

ev = int(input("Adj meg egy évet, csak úgy random: "))

def szokik(ev):
   return ev % 400 == 0 or (ev % 4== 0 and ev %100 != 0)

print(szokik(ev))

ev1 = int(input("Adj meg egy évszámot: "))
ev2 = int(input("Adj meg még egyet: "))

fff = []
for i in range(ev1, ev2):
    if szokik(i):
       fff.append(i)
       
print(fff)
if (len(fff)) == 0:
 print ("Nincs szökőév az adott időtartományban.")
    
        

