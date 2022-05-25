lista = ["egyes", "kettes", "hármas", "négyes", "Kizsgugya"]

#lista elemek kiíratása egymás alá
for i in range (len(lista)):
    print(lista[i])
    
#lista elemeinek HOSSZÁNAK kiíratása
for i in range (len(lista)):
    print(len(lista[i]))
    
    

#vesszővel elválasztva írasd ki az összes k betűvel kezdődő szavat
for i in range(0, len(lista)):
    if lista[i][0] == "k" or "K":
        print(lista[i], end=" ") #szóközzel tagolva egymás mellé kiíratva
        
#a kis- és nagybetűket ne különböztesse meg

for i in range(0, len(lista)):
    if lista[i][0].lower ==  "k":
        print(lista[i], end=" ")
        
#szerepel-e a rétes szó a mondatban?
mondat = "Ki szereti a rétest?"
print("rétes" in mondat)
 
#a lista mindenkori utolsó elemében van-e y betű?
print("y" in lista[len(lista)-1])
