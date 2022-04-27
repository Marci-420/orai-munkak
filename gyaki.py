class Eladott:
    ules: int
    tol: int
    ig: int
    
    def __init__(self, sor:str):
        adatok = sor.split(" ")
        self.ules = int(adatok[0])
        self.tol =  int(adatok[1])
        self.ig = int(adatok[2])
    
f1 = open("eladott.txt", "r")

gyaki: list[Eladott] = []

f1.readline()

for i in f1:
    cucc = Eladott(i.strip())
    gyaki.append(cucc)
    
print(len(gyaki))
