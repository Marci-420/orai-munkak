from pickle import TRUE
import random
from xmlrpc.client import boolean

#töltsön fel egy listát kétjegyű természetes számokkal
lista = []
for i in range(10):
   lista.append(random.randint(10, 99))
print(lista)


#döntsük el, hogy prím szám-e?
def prime(szam: int) -> boolean:
    osztok = 0
    for i in range(szam):
      if szam% (i+1) == 0:
          osztok=osztok + 1
    return osztok == 2

# eldöntöm, hogy a listában van-e prím szám
vaneprim = False
for i in range(10):
  if(prime(lista[i])):
    vaneprim = True
    
if vaneprim == True:
   print("Van benne prím szám")
else:
   print("Nincs benne prím szám")
    
# eldöntöm, hogy a listában van-e prím szám No.2

primdb = 0
for i in range(10):
  if(prime(lista[i])):
    primdb = primdb + 1
if primdb > 0:
  print("Van benne prím tuti")
else:
  print("Nincs benne tuti")
  
  
  

  
  
      
