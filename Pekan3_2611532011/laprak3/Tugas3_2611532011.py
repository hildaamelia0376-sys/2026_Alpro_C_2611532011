# Program Studi Kasus Terpadu: Sistem Simulasi Transaksi dan Validasi Akses Toko
# Nama File: tugas3_2611532011.py
# Mata Kuliah: Praktikum Algoritma dan Pemrograman

print("=== SISTEM TRANSAKSI TOKO ===")

# 2. Data Pelanggan dan Transaksi (Menggunakan input)
nama_2011 = input("Masukkan Nama Pelanggan : ")
status_pelanggan_2011 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_2011 = int(input("Masukkan Total Belanja : "))
jumlah_barang_2011 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2011 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan   :", nama_2011)
print("Status Pelanggan :", status_pelanggan_2011)
print("Total Belanja    : Rp", total_belanja_2011)
print("Jumlah Barang    :", jumlah_barang_2011)
print("Kode Promo       :", kode_promo_2011)

# 4. Operator Perbandingan
is_belanja_cukup_2011 = total_belanja_2011 >= 200000
is_barang_cukup_2011 = jumlah_barang_2011 >= 3
is_member_2011 = status_pelanggan_2011.strip().lower() == "member"

# 7. Operator Keanggotaan (Membership)
daftar_promo_2011 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
is_promo_tersedia_2011 = kode_promo_2011.strip().upper() in daftar_promo_2011

# 5. Operator Logika
is_dapat_diskon_2011 = is_member_2011 and is_belanja_cukup_2011
is_dapat_promo_2011 = is_promo_tersedia_2011 and is_barang_cukup_2011
member_access_2011 = is_member_2011 or is_belanja_cukup_2011
promo_access_2011 = is_dapat_promo_2011
free_shipping_access_2011 = is_promo_tersedia_2011 or is_barang_cukup_2011

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000   :", is_belanja_cukup_2011)
print("Jumlah Barang >= 3    :", is_barang_cukup_2011)
print("Status Member         :", is_member_2011)
print("Kode Promo Tersedia   :", is_promo_tersedia_2011)
print("Mendapatkan Diskon    :", is_dapat_diskon_2011)
print("Mendapatkan Promo     :", is_dapat_promo_2011)

# 3. Operator Aritmatika
if is_dapat_diskon_2011:
    diskon_2011 = int(total_belanja_2011 * 0.1)
else:
    diskon_2011 = 0

total_pembayaran_2011 = total_belanja_2011 - diskon_2011
rata_rata_2011 = total_belanja_2011 / jumlah_barang_2011 if jumlah_barang_2011 > 0 else 0

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                : Rp", diskon_2011)
print("Total Pembayaran      : Rp", total_pembayaran_2011)
print("Rata-rata Harga Barang: Rp", int(rata_rata_2011))

print("\n=== HAK AKSES PELANGGAN ===")
print("Member Access         :", member_access_2011)
print("Promo Access          :", promo_access_2011)
print("Free Shipping Access  :", free_shipping_access_2011)

# 6. Operator Penugasan (Assignment & Augmented Assignment)
poin_2011 = 100        # Assignment biasa
poin_2011 += 50        # Augmented assignment penambahan

# 8. Operator Identitas (Identity)
objek_a_2011 = ["Akses", "Toko"]
objek_b_2011 = objek_a_2011
objek_c_2011 = ["Akses", "Toko"]
cek_is_2011 = objek_a_2011 is objek_b_2011
cek_is_not_2011 = objek_a_2011 is not objek_c_2011

# 9. Operator Bitwise
# Nilai Bit: 0001 (Member), 0010 (Belanja >= 200k), 0100 (Jumlah barang >= 3), 1000 (Kode promo tersedia)
bit_member_2011 = 1 if is_member_2011 else 0
bit_belanja_2011 = 2 if is_belanja_cukup_2011 else 0
bit_barang_2011 = 4 if is_barang_cukup_2011 else 0
bit_promo_2011 = 8 if is_promo_tersedia_2011 else 0

kode_status_bit_2011 = bit_member_2011 | bit_belanja_2011 | bit_barang_2011 | bit_promo_2011

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print("Kode Biner  :", bin(kode_status_bit_2011)[2:].zfill(4))
print("Kode Desimal:", kode_status_bit_2011)

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(kode_status_bit_2011)[2:].zfill(4)} & 0001")
hasil_and_member_2011 = kode_status_bit_2011 & 1
print("Hasil Biner :", bin(hasil_and_member_2011)[2:].zfill(4))
print("Hasil Desimal:", hasil_and_member_2011)

print("\nCek Promo")
print(f"{bin(kode_status_bit_2011)[2:].zfill(4)} & 1000")
hasil_and_promo_2011 = kode_status_bit_2011 & 8
print("Hasil Biner :", bin(hasil_and_promo_2011)[2:].zfill(4))
print("Hasil Desimal:", hasil_and_promo_2011)

print("\n=== Perbandingan Status ===")
kode_referensi_2011 = 0b1011  # 11 dalam desimal
print("Kode Transaksi :", bin(kode_status_bit_2011)[2:].zfill(4))
print("Kode Referensi : 1011")
hasil_xor_2011 = kode_status_bit_2011 ^ kode_referensi_2011
print(f"{bin(kode_status_bit_2011)[2:].zfill(4)} ^ 1011")
print("Hasil Biner :", bin(hasil_xor_2011)[2:].zfill(4))
print("Hasil Desimal:", hasil_xor_2011)

print("\n=== Shift ===")
hasil_shift_2011 = kode_status_bit_2011 << 1
print(f"{bin(kode_status_bit_2011)[2:].zfill(4)} << 1")
print("Hasil Biner :", bin(hasil_shift_2011)[2:].zfill(4))
print("Hasil Desimal:", hasil_shift_2011)

print("\n=== SELESAI ===")