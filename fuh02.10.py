#készítsünk egy függvényt, ami egy paramméterként megkapott szóban meghatározza a magánhangzók számát

def bruh(nap: str) -> int:
    db: int = 0
    mgh = "aáeéiíoóöőuúüű"
    for i in range (len(nap)):
      if nap[i] in mgh:
         db += 1
    return db
  
print(bruh("hétfő"))

#2

napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek"]
for elem in napok:
    print(bruh(elem))
    
maxcucc = 0 

for i in range (len(napok)):
    if(bruh(napok[i]) > bruh(napok[maxcucc])):
        maxcucc = i
        
print(napok[maxcucc])
    


    


    


    