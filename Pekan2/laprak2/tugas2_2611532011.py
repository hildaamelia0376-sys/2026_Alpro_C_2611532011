print("===SISTEM REGISTRASI PRAKTIKUM ALPRO 2026===")
nama_2011 = input("Masukkan Nama Mahasiswa: ")
jenis_kelamin_2011 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2011 = int(input("Masukkan Umur: "))
nilai_2011 = float(input("Masukkan Skor Tes Awal: "))
alamat_2011 = """
    Kampus Unand,
    Kecamatan Pauh,
    Kota Padang
"""

id_token_2011 = 100 + 3j

Batas_lulus_2011 = 75.0
status_lulus_2011 = nilai_2011 >= Batas_lulus_2011

print("\n===DATA PRAKTIKUM DAN HASIL PEMERIKSAAN===")
print("Nama Mahasiswa: ", nama_2011, "| Tipe: ", type(nama_2011))
print("Jenis Kelamin: ", jenis_kelamin_2011, "| Tipe: ", type(jenis_kelamin_2011))
print("Alamat: ", alamat_2011, "| Tipe: ", type(alamat_2011))
print("Umur: ", umur_2011, "| Tipe: ", type(umur_2011))
print("Skor Tes Awal: ", nilai_2011, "| Tipe: ", type(nilai_2011))
print("ID Token Sinyal: ", id_token_2011, "| Tipe: ", type(id_token_2011))

print("\n===STATUS KELULUSAN PRAKTIKUM===")
print("Batas Minimum Nilai: ", Batas_lulus_2011)
print("Apakah Dinyatakan lulus?:" , status_lulus_2011, "| Tipe: ", type(status_lulus_2011))