
from stringprep import c9_set


a = int(input("Adj meg egy számot:"))
b = int(input("Adj meg még egy számot: "))
c = int(input("Meg még egy utolsót: "))
lista = [a, b, c]

print(max(lista))
print(min(lista))

if a < b < c or c < b < a:
   print(b, "a középső")
elif b < a < c or c < a < b:
    print (a, "középső")
else: 
    print(c, "a középső")
# java kompatibilis megoldása a PYTHON feladatnak

maximum = max(a, b, c)
minimum = min(a, b, c)
if (a != maximum and a != minimum):
    medium = a
if (b != maximum and b != minimum):
    medium = b
else:
    medium = c
# még egy másik megoldás
lista =[a, b, c]
lista.sort()
print("legkisebb:", lista[0], "középső:", lista[1], "legnagyobb:", lista[2])