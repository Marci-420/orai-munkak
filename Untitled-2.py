

egy = int(input("Adj meg egy évszámot: "))
ketto= int(input("Meg még egyet: "))
szoki=[]


#lista = [int(input("Adj meg egy számot")) for x in range(2)]

def szokoev(a: int , b: int):
    for i in range(a-1, b+1):
        if i % 400 ==0 or i % 100 != 0 and i % 4 == 0:
            szoki.append(i)
    
           
            
    

szokoev(egy, ketto)
print(szoki)