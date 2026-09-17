# Buta file dengan nama aritmatika_NIM_py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234

angka1_2011 = int(input("Input angka-1: "))
angka2_2011 = int(input("Input angka-2: "))

#Penjumlahan
hasil = angka1_2011 + angka2_2011
print("\nOperator Penjumlahan")
print("Hasil =", hasil)

#Pengurangan
hasil = angka1_2011 - angka2_2011
print("\Operator Pengurangan")
print("Hasil =", hasil)

#Perkalian
hasil = angka1_2011 * angka2_2011
print("\Operator Perkalian")
print("Hasil =", hasil)

#Pembagian, pembagian bulat, dan sisa bagi
if angka2_2011 != 0:
    hasil = angka1_2011 / angka2_2011
    print("\Operator Pembagian")
    print("Hasil =", hasil)
     
    hasil = angka1_2011 // angka2_2011
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_2011 % angka2_2011
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak bernilai 0.")

 #Pangkat
hail = angka1_2011 ** angka2_2011
print("\nOperator Pangkat")
print("Hasil =", hasil)