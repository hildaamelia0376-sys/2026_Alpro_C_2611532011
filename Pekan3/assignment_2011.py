angka1_2011 = int(input("Input angka-1: "))
angka2_2011 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2011)
print("Nilai angka2 =", angka2_2011)

#Assignment biasa
hasil_2011 = angka1_2011
print("\nAssignment Biasa (=)")
print("Hasil =", hasil_2011)

#Assignment penambahan
hasil_2011 = angka1_2011
hasil_2011 += angka2_2011
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil_2011)

#Assignment pengurangan
hasil_2011 = angka1_2011
hasil_2011 -= angka2_2011
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_2011)

#Assignment perkalian
hasil_2011 = angka1_2011
hasil_2011 *= angka2_2011
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_2011)

#Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2011 != 0:
    hasil_2011 = angka1_2011
    hasil_2011 /= angka2_2011
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_2011)
    #Operator tambahan
    hasil_2011 = angka1_2011
    hasil_2011 //= angka2_2011
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2011)
    hasil_2011 = angka1_2011
    hasil_2011 %= angka2_2011
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2011)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")

#Operator tambahanb: Assignment perpangkatan
hasil_2011 = angka1_2011
hasil_2011 **= angka2_2011
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2011)