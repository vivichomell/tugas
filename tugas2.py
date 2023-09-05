j = int(input("masukan jari jari: "))
t = int(input("masukan tinggi: "))
la = int(input("luas alas: "))
ka = int(input("masukan keliling alas: "))

phi = 22/7

luas = (2*la)+(ka*t)
volum = phi*j*j*j*t

print("luas tabung adalah: ", luas)
print("volum tabung adalah: ", volum)