# Buta file dengan nama aritmatika_NIM_py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234

angka1_2011 = int(input("Input angka-1: "))
angka2_2011 = int(input("Input angka-2: "))

#Penjumlahan
hasil_2011 = angka1_2011 + angka2_2011
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2011)

#Pengurangan
hasil_2011 = angka1_2011 - angka2_2011
print("\nOperator Pengurangan")
print("Hasil =", hasil_2011)

#Perkalian
hasil_2011 = angka1_2011 * angka2_2011
print("\nOperator Perkalian")
print("Hasil =", hasil_2011)

#Pembagian, pembagian bulat, dan sisa bagi
if angka2_2011 != 0:
    hasil_2011 = angka1_2011 / angka2_2011
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2011)
     
    hasil_2011 = angka1_2011 // angka2_2011
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2011)

    hasil_2011 = angka1_2011 % angka2_2011
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2011)
else:
    print("Angka kedua tidak bernilai 0.")

 #Pangkat
hasil_2011 = angka1_2011 ** angka2_2011
print("\nOperator Pangkat")
print("Hasil =", hasil_2011)