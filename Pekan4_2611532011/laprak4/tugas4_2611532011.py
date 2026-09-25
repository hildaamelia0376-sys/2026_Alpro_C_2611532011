# 1. Header dan input data pengunjung
print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_pengunjung_2011 = input("Masukkan Nama Pengunjung : ")
umur_2011 = int(input("Input Umur Anda : "))
simC_2011 = input("Apakah Anda Sudah Punya SIM C (y/t) : ").strip().lower()[0]

print("\nPilihan Paket Wahana (1-5)")
print("1. Safari Rimba          (Rp 50,000)")
print("2. Arung Jeram           (Rp 75,000)")
print("3. Motor ATV Ekstrim     (Rp 120,000)")
print("4. Roller Coaster Kilat  (Rp 100,000)")
print("5. All-Access VIP        (Rp 220,000)")

# 2. Pemilihan Paket Wahana (match-case)
while True:
    input_tiket_2011 = int(input("Masukkan nomor paket (1-5)     : "))

    match input_tiket_2011:
        case 1:
            jenis_wahana_2011 = "Wahana Safari Rimba"
            harga_2011 = 50000
            break
        case 2:
            jenis_wahana_2011 = "Wahana Arung Jeram"
            harga_2011 = 75000
            break
        case 3:
            jenis_wahana_2011 = "Wahana Motor ATV Ekstrim"
            harga_2011 = 120000
            break
        case 4:
            jenis_wahana_2011 = "Wahana Roller Coaster Kilat"
            harga_2011 = 100000
            break
        case 5:
            jenis_wahana_2011 = "Wahana All-Access VIP"
            harga_2011 = 220000
            break
        case _:
            print("\nNomor Paket Tidak Valid. Silakan Pilih Kembali!")

# 3. Jumlah tiket dan status tambahan
while True:
    jumlah_tiket_2011 = int(input("Masukkan Jumlah Tiket     : "))
    if (jumlah_tiket_2011 > 0):
        break
    else:
        print("\nJumlah Tiket Tidak Valid. Silahkan Masukkan Kembali!")

is_member_2011 = input("Apakah Anda Member? (y/t) : ").strip().lower()[0]
is_kode_promo_2011 = input("Apakah Kode Promo Valid? (y/t) : ").strip().lower()[0]

is_kondisi_2011 = True
total_diskon_2011 = 0

# 4. Validasi kelayakan pengendara wahana
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if (input_tiket_2011 == 3):
    if umur_2011 >= 17 and simC_2011 == "y":
        print(f"STATUS AKSES: Anda Sudah Dewasa dan Boleh Mengendarai {jenis_wahana_2011} Sendiri.")
    elif umur_2011 >= 17 and simC_2011 != "y":
        print(f"STATUS AKSES: Anda sudah dewasa tetapi tidak boleh bawa {jenis_wahana_2011} (wajib didampingi instruktur).")
    elif umur_2011 < 17 and simC_2011 =="y":
        print("Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Anda belum cukup umur dan tidak boleh bawa {jenis_wahana_2011}.")
        is_kondisi_2011 = False

else:
    if (umur_2011 >= 10):
         print(f"STATUS AKSES : Batas Umur Tercukupi dan Anda Boleh Menaiki {jenis_wahana_2011}.")
    else:
        print(f"STATUS AKSES : Anda Tidak Cukup Umur dan Tidak Boleh Menaiki {jenis_wahana_2011}.")
        is_kondisi_2011 = False



# 5. Akumulasi diskon dan rincian pembayaran
if is_kondisi_2011:
    if (harga_2011 * jumlah_tiket_2011 >= 200000):
        total_diskon_2011 += 10
    if (is_member_2011 == "y"):
        total_diskon_2011 += 5
    if (is_kode_promo_2011 == "y"):
        total_diskon_2011 += 15
    if (jumlah_tiket_2011 >= 5):
        total_diskon_2011 += 5

    print("\n--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp {harga_2011 * jumlah_tiket_2011:,.0f}")
    print(f"Total Diskon     : {total_diskon_2011}% (Rp {(harga_2011 * jumlah_tiket_2011) * (total_diskon_2011 / 100):,.0f})")
    print(f"Total Bayar       : Rp {(harga_2011 * jumlah_tiket_2011) - ((harga_2011 * jumlah_tiket_2011) * (total_diskon_2011 / 100)):,.0f}")
    if ((harga_2011 * jumlah_tiket_2011) - ((harga_2011 * jumlah_tiket_2011) * (total_diskon_2011 / 100)) > 300000):
            print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
    print("Catatan Layanan  : Terima kasih telah berkunjung.")
    

# 6. Penutup program
print("\nProgram Selesai")