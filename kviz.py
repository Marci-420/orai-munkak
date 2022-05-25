#feladat: kvíz

#(több) kérdés és a válasz
kerdesek =[ "Hány Star wars film készült a spin-off filmekkel együtt?",
           "Hány Marvel filmet csináltak a Pókember: Nincs Hazaútig?",
           "Ki rendezte az utolsó Transformers filmet?" ]
valaszok = ["11","26","Michael Bay"]

#eredmény pontszám tárolása
pontszam = 0

#kérdés feltevése és az aktuális válasz bekérése/tárolása

#ellenőrzés
for i in range(len(kerdesek)):
    adott_valasz = input(kerdesek[i])
    if adott_valasz == valaszok[i]:
     pontszam = pontszam + 1
     
print(pontszam)