is_lulus = True
is_cumlaude = True

#Menggunakan Boolean
nilai_2011 = 85
batas_lulus = 75

#Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai_2011 >= batas_lulus #Hasilnya akan true

print("=== Check Kelulusan ===")
print("Nilai:", nilai_2011)
print("Apakah Lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda Lulus dengan predikat Cumlaude!")