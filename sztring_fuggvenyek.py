mondat = "valami filléres instagram bölcsesség"
#capitalize(): az első karaktert nagybetűsíti
print(mondat.capitalize())

#swapcase(): minden ngybetűt kicsivé tesz, és vice verza.
print(mondat.swapcase())

#title: a mondat minden szavának első betűjét naggyá teszi
print(mondat.title())

#startswith: igazat ad, ha a mondat a megadott szóval/betűvel kezdődik
print(mondat.startswith("pff"))

#endswith: igazat ad, ha a mondat a megadott szóval/betűvel végződik
print(mondat.endswith("g"))

#find: megkeresi a megadott kifejezés kezdetének indexét a mondatban, ha nincs benne, -1-et ad vissza
print(mondat.find("Moby Dick"))

# rfind():
print(mondat.rfind("iksz és dé"))

#index: megkeresi a megadott kifejezés kezdetének indexét a mondatban, ha nincs benne,HIBÁT AD VISSZA
#print(mondat.("Moby Dick"))

# rindex():
#print(mondat.rindex("iksz és dé"))


#isalnum():
print(mondat.isalnum())

#isalfa
print(mondat.isalpha())

#isnumeric
print(mondat.isnumeric())

#isspace():akkor ad igazat, ha minden karakter üres
print(mondat.isspace())
space= "     "
ujsorok = "\n\n\n"
print(space.isspace())
print(ujsorok.isspace())


