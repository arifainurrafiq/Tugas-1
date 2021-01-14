import math
r = float (input ("Masukkan jari-jari: "))

luas = math.pi*(r*r)
keliling = 2*math.pi*r

print ("Luas Lingkaran \t\t= ", luas)
print ("keliling Lingkaran\t= ", keliling)

print ("Luas Lingkaran 2digit \t= ",format(luas,'.2f'))
print ("Keliling Lingkaran 2digit \t= ",format(keliling,'.2f'))
