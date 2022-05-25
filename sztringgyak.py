szoveg = input( "Írj egy mondatot!")



tagolt_cucc = szoveg.split(" ")
print(tagolt_cucc)

for i in reversed(range(len(tagolt_cucc))):
    print(tagolt_cucc[i])
print(reversed(tagolt_cucc))