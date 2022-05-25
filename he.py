lista =[]

for i in range(5):
    szam = int(input("Add meg a lista", i,". elemét"))
    i += 1
    a = int(input("Hányadik helyre szeretnéd tenni?"))

lista.append(szam, a)

print(lista)