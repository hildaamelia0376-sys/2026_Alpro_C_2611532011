tinggi_2011 = int(input("Masukkan tinggi segitiga: "))

# perulangan untuk setiap baris segitiga
for i in range(1, tinggi_2011 + 1):
    print(" " * (tinggi_2011 - i) + "* " * i)