sorok = []
file = open('forras.txt', 'r', encoding='utf-8')

nev1 =  file.readline().strip()
nev2 =  file.readline().strip()
nev3 =  file.readline().strip()
 
print(nev1, nev2, nev3)

lizsda = []
files = open('szamok.txt', 'r',)

for e in files:
    lizsda.append(int(e.strip()))
print(lizsda)

