#lista létrehozása
mylist = ["Audi", "Peugeot", "Volkswagen"]

#ellenőrzés
print(mylist)

#listaelem elérése
print(mylist[1])

#listaelemek száma
print(len(mylist))

#a mindenkori utolsó kiiratása
print(mylist[-1])
print(mylist[len(mylist)-1])

#elem hozzáfűzése (a végéhez)
mylist.append("bázsi")
print(mylist)

#elem beszúrása megadott helyre
mylist.insert(2, "Suzuki")
print(mylist)

#beszúrás a mindenkori utolsó helyre
mylist.insert(len(mylist), "Renault")
print(mylist)

#listaelem eltávolítása indexszel
mylist.pop(2)
print(mylist)

#listaelem eltávolítása tartalom alapján
mylist.remove("Dacia")
print(mylist)

#lista bejárása
for i in range(len(mylist)):
    print(mylist)

#feladat: járjuk be a listát, vizsgáljuk meg minden elemnél, hogy Audi-e. Ha igen, írjuk ki: "ez Audi"
for i in range(len(mylist)):
    if mylist[i] == "Audi":
        print("Ez Audi")
