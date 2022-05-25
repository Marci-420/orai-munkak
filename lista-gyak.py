#létrehozunk egy szamok nevű listát
#legyen benne 3 tetszőleges szám

szamok = [13, 21, 52]
print(szamok)
szamok.append(9)
szamok.append(4)
print(szamok)
db = 0    
for i in szamok:                 
    if i %2  == 0:
        db += 1
print("A listában", db, "páros szám van a kurvaanyáddalmatekozzálcsütörtökdélután")
for i in range(len(szamok)):
    if szamok[i] < 5:
        szamok[i] = szamok[i] * 2
    else:
        szamok[i] = szamok[i] / 3
print(szamok)
        

       



   
