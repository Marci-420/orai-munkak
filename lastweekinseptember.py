import math, os
a= int(input(" Egyik egész szám ( alap oldalhossz):"))
ma = int(input("Másik egész szám (magasság):"))

if ma > 0:                      
    Ta =pow (a, 2)                             #terület
    print("A terület:", Ta)
    V = (Ta * ma) / 3                           #térfogat
    print ("A térfogata:", V)
    b = a / 2                                  # háromszög b oldala
    C = ma**2 + b**2
    c= math.sqrt (C)                           # 3szög c oldalának kiszámítása
    T3 = (a * c) / 2
    A = 4 * T3 + Ta                            # felszín
    print("A felszíne: ", A)

else:
    print("Komolyan beírtad a nullát?")        #ejnyebejnye
if a == 0 and ma == 0:
     os.startfile(r'C:\puzsér.jpg')               #ssshhhh
elif (a == 1 or a == 2) and (ma == 1 or ma == 2):
    os.startfile('https://www.youtube.com/watch?v=QCSFBE3NZUE')     #corn