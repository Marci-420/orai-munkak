

a = int(input("Adjon meg egy egész számot: "))
b = int(input("Meg még egyet: "))

if a > b:
    print("A(z)", a, "nagyobb, mint a(z)", b, ".")
elif b > a:
    print("A(z)", b, "nagyobb, mint a(z)", a, ".")
else:
    print("A két szám egyenlő")