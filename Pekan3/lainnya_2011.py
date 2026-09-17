print("===================================")
print("1. OPERATOR KEANGGOTAAN")
print("===================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2011 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2011 = [int(angka_2011.strip()) for angka_2011 in input_data_2011.split(",")]

nilai_dicari_2011 = int(input("Masukkan angka yang ingin dicari; "))

#Operator in
hasil_2011 = nilai_dicari_2011 in data_2011
print("\nOperator keanggotaan in")
print(nilai_dicari_2011, "in", data_2011, "=", hasil_2011)

#Operator Not In
hasil_2011 = nilai_dicari_2011 not in data_2011
print("\nOperator keanggotaan Not In")
print(nilai_dicari_2011, "not in", data_2011, "=", hasil_2011)

print("===================================")
print("2. OPERATOR IDENTITAS")
print("===================================")

# Objek 1 menggunakan list dari pengguna
objek1_2011 = data_2011

#objek 2 merujuk pada objek yang sama dengan objek 1
objek2_2011 = objek1_2011

#objek 3 memiliki isi sama, tetapi merupakan objek baru
objek3_2011 = data_2011.copy()

print("objek1_2011 =", objek1_2011)
print("objek2_2011 =", objek2_2011)
print("objek3_2011 =", objek3_2011)

# operator is
hasil_2011 = objek1_2011 is objek2_2011
print("\nOperator identitas is")
print("objek1_2011 is objek2_2011 = ", hasil_2011)

#operator is not
hasil_2011 = objek1_2011 is not objek3_2011
print("\nOperator identitas is not")
print("objek1_2011 is not objek3_2011 = ", hasil_2011)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai:")
print("objek1_2011 is objek3_2011:", objek1_2011 is objek3_2011)
print("objek1_201 == objek3_2011:", objek1_2011 == objek3_2011)