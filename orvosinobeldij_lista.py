#fájl megnyitása
file = open ("orvosi_nobeldijak.txt", "r", encoding = "utf-8")

#lista létrehozása a soroknak
lista = []

#első sor beolvasása
file.readline()

for sor in file:
    #listához hozzáfűzöm a listából feldarabolt sort
    lista.append(sor.strip().split(";"))
    
print(lista)
print(lista[1][3])

#az összes angol Nobel-díjas

mennyi = 0
for sor in lista:
    if sor[3] == "GB" :
     mennyi += 1

print(mennyi)

#az összes Nobel-díjas, aki 1920 előtt lpota a díjat

for sor in lista:
    if int(sor[0]) < 1905:
        print(sor[1])
        
print("           ")
        
# az összes "a" betűvel kezdődő név kiíratása

for sor in lista:
    if sor[1].startswith("A"):
        print(sor[1])
        
print("        ")
        
#akik élnek még, és hány évesek

for sor in lista:
    if len(sor[2]) == 5:
        szulev = int(sor[2][0:4])
        print(sor[1], 2022 - szulev)
