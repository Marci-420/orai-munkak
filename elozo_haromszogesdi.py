# OSZTÁLY:

class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    
    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int            :
        return self.a + self.b + self.c
    
    #hozz létre minden sorból egy Haromszog típusú objektumot
    #metódusa segítségével írd ki, hogy a számok háromszöget alkotnak-e
    
    #bekérsz a felhasználótól 3 számot (MegFeLElő AdaTSzeRkEZEtBeN), majd írd ki neki, hogy 3szöget alkotnak-e
    
a = int(input("Add meg az a oldalt: "))
b = int(input("Add meg a b oldalt: "))
c = int(input("Add meg a c oldalt: "))
    
def haromszogek(a, b, c) -> str:
    if a+b > c and a+c > b and b+c > a:
        print("good")
    else:
        print("no good")

haromszogek(a,b,c)