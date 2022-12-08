#program menghasilkan n+n dengan panjng nilai  yang di tentukan inputan user

a = int(input("masukkan angka : "))

n = "  "
for i in range  (1,a):
	n = n + str (i) + ("+")
	print (n[:-1], end = " ")